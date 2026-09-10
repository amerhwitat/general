#pragma once
#include <string>
#include <unordered_map>
#include <vector>
namespace chimera::mobile {
struct Package { std::string name; std::string version; std::string entry_activity; std::string abi; bool signed_package{false}; };
class PackageManager {
public:
  bool install(Package p);
  bool uninstall(const std::string& name);
  const Package* find(const std::string& name) const;
  std::vector<Package> list() const;
private:
  std::unordered_map<std::string, Package> packages_;
};
}
