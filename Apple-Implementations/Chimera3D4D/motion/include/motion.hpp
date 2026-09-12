#pragma once
#include "chimera3d4d/geometry.hpp"
#include <cstdint>
#include <vector>
namespace chimera3d4d::motion { struct Sample { double time{}; std::uint32_t joint{}; Transform transform{}; }; using Stream=std::vector<Sample>; }
