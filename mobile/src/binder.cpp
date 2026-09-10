#include "chimera/mobile/binder.hpp"
namespace chimera::mobile {
ServiceId BinderBus::publish(std::string name, Handler handler){ std::lock_guard lk(mu_); auto id=next_++; handlers_.emplace(id,std::move(handler)); names_.emplace(id,std::move(name)); return id; }
std::vector<uint8_t> BinderBus::transact(ServiceId service,uint32_t code,std::vector<uint8_t> payload) const { std::lock_guard lk(mu_); auto it=handlers_.find(service); if(it==handlers_.end()) return {}; return it->second(Transaction{service,code,std::move(payload)}); }
bool BinderBus::remove(ServiceId service){ std::lock_guard lk(mu_); names_.erase(service); return handlers_.erase(service)!=0; }
}
