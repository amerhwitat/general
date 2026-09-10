#include "chimera/mobile/power.hpp"
namespace chimera::mobile {
PowerDecision PowerPolicy::evaluate(const PowerSample& s) const {
  PowerDecision d;
  if(s.temperature_mc>=85000){ d.mode=PowerMode::BatterySaver; d.cpu_ceiling_pct=60; d.gpu_ceiling_pct=55; d.background_quota_pct=15; }
  else if(s.battery_pct<=10){ d.mode=PowerMode::BatterySaver; d.cpu_ceiling_pct=55; d.gpu_ceiling_pct=45; d.background_quota_pct=10; }
  else if(s.cpu_load_pct>=90 && s.gpu_load_pct>=75){ d.mode=PowerMode::SustainedPerformance; d.cpu_ceiling_pct=100; d.gpu_ceiling_pct=100; d.background_quota_pct=35; }
  else if(s.cpu_load_pct>=80){ d.mode=PowerMode::LaunchBoost; d.cpu_ceiling_pct=100; d.gpu_ceiling_pct=90; d.background_quota_pct=25; }
  return d;
}
}
