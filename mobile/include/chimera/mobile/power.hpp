#pragma once
#include <cstdint>
namespace chimera::mobile {
enum class PowerMode { Balanced, BatterySaver, SustainedPerformance, FixedPerformance, LaunchBoost };
struct PowerSample { uint32_t battery_pct{}; int32_t temperature_mc{}; uint32_t cpu_load_pct{}; uint32_t gpu_load_pct{}; };
struct PowerDecision { PowerMode mode{PowerMode::Balanced}; uint32_t cpu_ceiling_pct{100}; uint32_t gpu_ceiling_pct{100}; uint32_t background_quota_pct{100}; };
class PowerPolicy {
public:
  PowerDecision evaluate(const PowerSample& s) const;
};
}
