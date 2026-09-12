#pragma once
#include "chimera3d4d/geometry.hpp"
namespace chimera3d4d::sculpt { struct Brush { double radius{0.1}; double strength{0.5}; bool symmetry{false}; }; void apply(Mesh&, Vec3 center, Vec3 direction, const Brush&); }
