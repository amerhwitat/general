#pragma once
#include <cstdint>
#include <string>
namespace chimera::mobile { struct ArchMobileProfile{std::string architecture="aarch64";std::string rootfs="archlinux-arm";std::string package_manager="pacman";std::string init="systemd-compatible";uint32_t page_size=16384;bool wayland=true;bool aurora=true;bool chimera_hal=true;bool nbit=true;}; }
