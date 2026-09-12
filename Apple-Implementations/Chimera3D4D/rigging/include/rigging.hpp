#pragma once
#include "chimera3d4d/geometry.hpp"
#include <string>
#include <vector>
namespace chimera3d4d::rigging { struct Joint { std::string name; int parent{-1}; Transform bind; }; struct Skeleton { std::vector<Joint> joints; }; }
