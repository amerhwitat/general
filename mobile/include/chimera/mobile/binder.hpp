#pragma once
#include <cstdint>
#include <functional>
#include <mutex>
#include <string>
#include <unordered_map>
#include <vector>
namespace chimera::mobile {
using ServiceId = uint32_t;
struct Transaction { ServiceId service{}; uint32_t code{}; std::vector<uint8_t> payload; };
using Handler = std::function<std::vector<uint8_t>(const Transaction&)>;
class BinderBus {
public:
  ServiceId publish(std::string name, Handler handler);
  std::vector<uint8_t> transact(ServiceId service, uint32_t code, std::vector<uint8_t> payload) const;
  bool remove(ServiceId service);
private:
  mutable std::mutex mu_;
  ServiceId next_{1};
  std::unordered_map<ServiceId, Handler> handlers_;
  std::unordered_map<ServiceId, std::string> names_;
};
}
