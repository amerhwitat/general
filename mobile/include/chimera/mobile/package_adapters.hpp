#pragma once
#include "chimera/mobile/package_fabric.hpp"
#include <string>
namespace chimera::mobile {
enum class Manager { Chimera, Pacman, Dpkg, Apt, AptGet, Aptitude, Rpm, Dnf, Yum, Apk, Nix, Flatpak, Snap, AppImage, Git, Github };
struct AdapterCommand { Manager manager; std::string command; PackageFormat format; bool sandboxed; };
class PackageAdapters { public: static AdapterCommand route(const std::string& command); static const char* canonical(Manager); };
}
