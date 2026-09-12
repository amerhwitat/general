#include "dynamics.hpp"

namespace chimera3d4d::dynamics {
void Solver::step(double dt) { if (dt > 0.0) lastDt = dt; }
}
