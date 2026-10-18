#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <sys/stat.h>

static unsigned char decode_buffer[1024];
static unsigned char* decode_buffer_position;
static unsigned char* decode_buffer_end;
static unsigned int decode_bytes_left;
static int ring_buffer_index;
static unsigned char ring_buffer[4116];

static inline void lzss_fill_decode_buffer(FILE* stream)
{
    size_t bytes_to_read;
    size_t bytes_read;

    if (decode_bytes_left != 0 && decode_buffer_end - decode_buffer_position <= 16) {
        if (decode_buffer_position == decode_buffer_end) {
            decode_buffer_end = decode_buffer;
        } else {
            memmove(decode_buffer, decode_buffer_position, decode_buffer_end - decode_buffer_position);
            decode_buffer_end = decode_buffer + (decode_buffer_end - decode_buffer_position);
        }

        decode_buffer_position = decode_buffer;

        bytes_to_read = 1024 - (decode_buffer_end - decode_buffer);
        if (bytes_to_read > decode_bytes_left) {
            bytes_to_read = decode_bytes_left;
        }

        bytes_read = fread(decode_buffer_end, 1, bytes_to_read, stream);
        decode_buffer_end += bytes_read;
        decode_bytes_left -= bytes_read;
    }
}

static inline void lzss_decode_chunk_to_buf(unsigned int type, unsigned char** dest, unsigned int* length)
{
    unsigned char low;
    unsigned char high;
    int dict_offset;
    int dict_index;
    int chunk_length;
    int index;

    if (type != 0) {
        *length -= 1;
        *(*dest) = *decode_buffer_position++;
        ring_buffer[ring_buffer_index] = *(*dest)++;
        ring_buffer_index += 1;
        ring_buffer_index &= 0xFFF;
    } else {
        *length -= 2;
        low = *decode_buffer_position++;
        high = *decode_buffer_position++;
        dict_offset = low | ((high & 0xF0) << 4);
        chunk_length = (high & 0x0F) + 3;

        for (index = 0; index < chunk_length; index++) {
            dict_index = (dict_offset + index) & 0xFFF;
            *(*dest) = ring_buffer[dict_index];
            ring_buffer[ring_buffer_index] = *(*dest)++;
            ring_buffer_index += 1;
            ring_buffer_index &= 0xFFF;
        }
    }
}

int lzss_decode_to_buf(FILE* in, unsigned char* dest, unsigned int length)
{
    unsigned char* curr = dest;
    unsigned char byte;

    memset(ring_buffer, ' ', 4078);
    ring_buffer_index = 4078;
    decode_buffer_end = decode_buffer;
    decode_buffer_position = decode_buffer;
    decode_bytes_left = length;

    while (length > 16) {
        lzss_fill_decode_buffer(in);

        length -= 1;
        byte = *decode_buffer_position++;
        lzss_decode_chunk_to_buf(byte & 0x01, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x02, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x04, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x08, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x10, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x20, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x40, &curr, &length);
        lzss_decode_chunk_to_buf(byte & 0x80, &curr, &length);
    }

    while (length > 0) {
        lzss_fill_decode_buffer(in);
        length -= 1;
        byte = *decode_buffer_position++;

        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x01, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x02, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x04, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x08, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x10, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x20, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x40, &curr, &length);
        if (length == 0) break;
        lzss_decode_chunk_to_buf(byte & 0x80, &curr, &length);
    }

    return curr - dest;
}

static int fread_short(FILE* stream, unsigned short* s) {
    int high = fgetc(stream);
    if (high == -1) return -1;
    int low = fgetc(stream);
    if (low == -1) return -1;
    *s = (low & 0xFF) | (high << 8);
    return 0;
}

static uint32_t read_be32(FILE* f) {
    unsigned char b[4];
    if (fread(b, 1, 4, f) != 4) return 0;
    return (b[0] << 24) | (b[1] << 16) | (b[2] << 8) | b[3];
}

static void mkdir_p(const char* dir) {
    char tmp[512];
    snprintf(tmp, sizeof(tmp), "%s", dir);
    size_t len = strlen(tmp);
    for (size_t i = 1; i < len; i++) {
        if (tmp[i] == '/') {
            tmp[i] = 0;
            mkdir(tmp, 0755);
            tmp[i] = '/';
        }
    }
    mkdir(tmp, 0755);
}

int main(int argc, char** argv) {
    if (argc < 3) {
        printf("Usage: %s <master.dat> <out_base_dir>\n", argv[0]);
        return 1;
    }

    FILE* dat = fopen(argv[1], "rb");
    if (!dat) { perror("dat"); return 1; }

    uint32_t dir_count = read_be32(dat);
    fseek(dat, 16, SEEK_SET);

    char (*dirs)[256] = malloc(dir_count * 256);
    for (uint32_t i = 0; i < dir_count; i++) {
        uint8_t len = fgetc(dat);
        fread(dirs[i], 1, len, dat);
        dirs[i][len] = 0;
    }

    int extracted = 0;

    for (uint32_t i = 0; i < dir_count; i++) {
        uint32_t file_count = read_be32(dat);
        fseek(dat, 12, SEEK_CUR);

        int is_text = (strstr(dirs[i], "TEXT\\ENGLISH") != NULL);

        for (uint32_t j = 0; j < file_count; j++) {
            uint8_t len = fgetc(dat);
            char fname[256];
            fread(fname, 1, len, dat);
            fname[len] = 0;

            uint32_t flags = read_be32(dat);
            uint32_t offset = read_be32(dat);
            uint32_t de_length = read_be32(dat);
            uint32_t field_C = read_be32(dat);

            if (is_text) {
                long saved_pos = ftell(dat);

                char target_folder[512];
                // lowercase dirs[i]
                char dir_lower[256];
                strcpy(dir_lower, dirs[i]);
                for (char* p = dir_lower; *p; p++) {
                    if (*p == '\\') *p = '/';
                    if (*p >= 'A' && *p <= 'Z') *p += 32;
                }
                char fname_lower[256];
                strcpy(fname_lower, fname);
                for (char* p = fname_lower; *p; p++) {
                    if (*p >= 'A' && *p <= 'Z') *p += 32;
                }

                snprintf(target_folder, sizeof(target_folder), "%s/%s", argv[2], dir_lower);
                mkdir_p(target_folder);

                char file_path[512];
                snprintf(file_path, sizeof(file_path), "%s/%s", target_folder, fname_lower);

                FILE* out = fopen(file_path, "wb");
                if (out) {
                    fseek(dat, offset, SEEK_SET);

                    if ((flags & 0xF0) == 64 || flags == 64) {
                        unsigned char* buf = malloc(de_length + 4096);
                        unsigned char* ptr = buf;
                        unsigned char* end = buf + de_length;

                        while (ptr < end) {
                            unsigned short v4;
                            if (fread_short(dat, &v4) == 0) {
                                if ((v4 & 0x8000) != 0) {
                                    v4 &= ~0x8000;
                                    fread(ptr, 1, v4, dat);
                                    ptr += v4;
                                } else {
                                    int n = lzss_decode_to_buf(dat, ptr, v4);
                                    ptr += n;
                                }
                            } else {
                                break;
                            }
                        }
                        fwrite(buf, 1, ptr - buf, out);
                        free(buf);
                    } else if ((flags & 0xF0) == 16 || flags == 16 || flags == 0) {
                        unsigned char* buf = malloc(de_length + 4096);
                        int n = lzss_decode_to_buf(dat, buf, field_C);
                        fwrite(buf, 1, n, out);
                        free(buf);
                    } else {
                        // plain
                        unsigned char buf[4096];
                        uint32_t left = de_length;
                        while (left > 0) {
                            size_t to_read = left > sizeof(buf) ? sizeof(buf) : left;
                            size_t r = fread(buf, 1, to_read, dat);
                            fwrite(buf, 1, r, out);
                            left -= r;
                        }
                    }

                    fclose(out);
                    extracted++;
                }

                fseek(dat, saved_pos, SEEK_SET);
            }
        }
    }

    free(dirs);
    fclose(dat);
    printf("Extracted %d English text files successfully!\n", extracted);
    return 0;
}
