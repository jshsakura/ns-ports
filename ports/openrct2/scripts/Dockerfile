# Builder image for the OpenRCT2 Switch port, reconstructed from the layers of the image that built the shipped NRO.
# Not rebuilt from scratch yet: if a step fails, compare with `docker history` of the original image.
FROM devkitpro/devkita64:latest
RUN apt-get update && apt-get install -y python3-distutils python3-setuptools nlohmann-json3-dev curl cmake \
 && cp -r /usr/include/nlohmann /opt/devkitpro/portlibs/switch/include/ && rm -rf /var/lib/apt/lists/*
RUN dkp-pacman -S --needed --noconfirm switch-portlibs
WORKDIR /tmp/libzip-src
RUN curl -L https://github.com/nih-at/libzip/releases/download/v1.12.1/libzip-1.12.1.tar.gz | tar -xz --strip-components=1 \
 && cmake -B build -S . -DCMAKE_TOOLCHAIN_FILE=/opt/devkitpro/cmake/Switch.cmake -DCMAKE_INSTALL_PREFIX=/opt/devkitpro/portlibs/switch \
      -DBUILD_SHARED_LIBS=OFF -DBUILD_TOOLS=OFF -DBUILD_REGRESS=OFF -DBUILD_EXAMPLES=OFF -DBUILD_DOC=OFF \
 && cmake --build build -j"$(nproc)" && cmake --install build && rm -rf /tmp/libzip-src
WORKDIR /source
