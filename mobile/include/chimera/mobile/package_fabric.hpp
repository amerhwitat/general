#pragma once
#include <string>
#include <vector>
namespace chimera::mobile {
enum class PackageFormat { Native, Deb, Dpkg, Apt, Rpm, Dnf, Yum, Pacman, Apk, Nix, Flatpak, Snap, AppImage, ApkAndroid, SwiftPM, GitSource, Unknown };
enum class PackageTarget { Arm64, AndroidContainer, SwiftRuntime, ChimeraNBit, HostTool };
enum class SignatureState { Missing, Invalid, Verified };
struct PackageRecord { std::string name, version, architecture, path, sha256; PackageFormat format{PackageFormat::Unknown}; PackageTarget target{PackageTarget::Arm64}; SignatureState signature{SignatureState::Missing}; bool privileged{false}; };
struct InstallPlan { PackageRecord package; std::vector<std::string> dependencies; bool transactional{true}; bool sandboxed{true}; };
class PackageFabric { public: static PackageFormat detect_format(const std::string& path); static bool compatible(PackageFormat, PackageTarget); bool validate(const PackageRecord&) const; InstallPlan plan(const PackageRecord&, const std::vector<std::string>&) const; };
}
