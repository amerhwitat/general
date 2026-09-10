#pragma once
#include <cstdint>
#include <string>
#include <vector>
#include <functional>
namespace chimera::mobile {
enum class AppState { Created, Started, Resumed, Paused, Stopped, Killed };
struct AppInfo { std::string package_name; std::string activity; uint32_t uid{}; uint32_t memory_budget_mb{128}; bool foreground{false}; };
struct FrameBudget { uint64_t vsync_ns{16666666}; uint64_t deadline_ns{12000000}; uint32_t refresh_hz{60}; };
class Runtime {
public:
  explicit Runtime(FrameBudget budget = {});
  uint64_t register_app(AppInfo app);
  bool transition(uint64_t id, AppState state);
  bool foreground(uint64_t id);
  bool background(uint64_t id);
  std::vector<AppInfo> snapshot() const;
  FrameBudget frame_budget() const { return budget_; }
  void on_memory_pressure(uint32_t level);
private:
  struct Record { uint64_t id; AppInfo app; AppState state; uint64_t last_active_ns; };
  FrameBudget budget_;
  std::vector<Record> apps_;
  uint64_t next_id_{1};
};
}
