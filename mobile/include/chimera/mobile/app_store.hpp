#pragma once
#include "chimera/mobile/package_fabric.hpp"
#include <string>
#include <vector>
namespace chimera::mobile { struct StoreEntry { PackageRecord package; std::string repository; std::string channel="stable"; std::string sandbox="default"; }; class AppStore { std::vector<StoreEntry> entries_; public: void publish(StoreEntry e); std::vector<StoreEntry> search(const std::string&term) const; const StoreEntry* find(const std::string&name) const; }; }
