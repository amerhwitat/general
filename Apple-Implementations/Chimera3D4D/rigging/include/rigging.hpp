#pragma once
#include "chimera3d4d/geometry.hpp"
#include <string>
#include <vector>

namespace chimera3d4d::rigging {
struct Joint { std::string name; int parent{-1}; Transform bind; Transform pose; };
struct Skeleton { std::vector<Joint> joints; bool valid() const noexcept; };
enum class ConstraintType { Parent, Point, Aim, IK, Limit };
struct Constraint { ConstraintType type{ConstraintType::Parent}; std::uint32_t joint{}; std::uint32_t target{}; double weight{1.0}; };
struct RetargetMap { std::vector<std::pair<std::string,std::string>> sourceToTarget; };
} // namespace chimera3d4d::rigging
