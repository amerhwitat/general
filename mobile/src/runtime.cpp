#include "chimera/mobile/runtime.hpp"
#include <algorithm>
#include <chrono>
namespace chimera::mobile {
static uint64_t now_ns(){ return std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::steady_clock::now().time_since_epoch()).count(); }
Runtime::Runtime(FrameBudget budget):budget_(budget){}
uint64_t Runtime::register_app(AppInfo app){ Record r{next_id_++,std::move(app),AppState::Created,now_ns()}; apps_.push_back(std::move(r)); return apps_.back().id; }
bool Runtime::transition(uint64_t id, AppState state){ for(auto& r:apps_) if(r.id==id){ r.state=state; r.last_active_ns=now_ns(); r.app.foreground=(state==AppState::Resumed); return true;} return false; }
bool Runtime::foreground(uint64_t id){ for(auto& r:apps_) r.app.foreground=(r.id==id); return transition(id,AppState::Resumed); }
bool Runtime::background(uint64_t id){ return transition(id,AppState::Paused); }
std::vector<AppInfo> Runtime::snapshot() const { std::vector<AppInfo> out; out.reserve(apps_.size()); for(auto const& r:apps_) if(r.state!=AppState::Killed) out.push_back(r.app); return out; }
void Runtime::on_memory_pressure(uint32_t level){ if(level<50) return; for(auto& r:apps_) if(!r.app.foreground && level>=90) r.state=AppState::Stopped; }
}
