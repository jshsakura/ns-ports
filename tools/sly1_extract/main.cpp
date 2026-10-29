// Host (Linux) driver for ProjectCane 0.5.0's Switch installer extractor.
// Runs CaneExtract::ExtractGame exactly as the NRO does, without a Switch.
#include "iso_extractor.h"
#include <chrono>
#include <cstdio>
#include <exception>

int main(int argc, char** argv)
{
    if (argc != 3)
    {
        std::fprintf(stderr, "usage: %s <iso> <output ProjectCane folder>\n", argv[0]);
        return 2;
    }
    std::string lastStage;
    try
    {
        CaneExtract::ExtractGame(argv[1], argv[2], [&](const CaneExtract::Progress& p) {
            if (p.stage != lastStage)
            {
                lastStage = p.stage;
                std::printf("[%zu/%zu] %s %s\n", p.completed, p.total, p.stage.c_str(), p.file.c_str());
                std::fflush(stdout);
            }
            return true;
        });
    }
    catch (const std::exception& e)
    {
        std::fprintf(stderr, "ERROR: %s\n", e.what());
        return 1;
    }
    std::printf("IsReady=%d\n", CaneExtract::IsReady(argv[2]) ? 1 : 0);
    return CaneExtract::IsReady(argv[2]) ? 0 : 1;
}
