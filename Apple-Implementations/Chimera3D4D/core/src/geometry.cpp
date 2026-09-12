#include "chimera3d4d/geometry.hpp"
#include <algorithm>

namespace chimera3d4d {

void AABB::expand(const Vec3& p) noexcept {
  min.x=std::min(min.x,p.x); min.y=std::min(min.y,p.y); min.z=std::min(min.z,p.z);
  max.x=std::max(max.x,p.x); max.y=std::max(max.y,p.y); max.z=std::max(max.z,p.z);
}

bool AABB::valid() const noexcept {
  return min.x<=max.x && min.y<=max.y && min.z<=max.z;
}

bool Mesh::validate() const noexcept {
  for (const auto& t : triangles) {
    if (t.a>=vertices.size() || t.b>=vertices.size() || t.c>=vertices.size()) return false;
    if (t.a==t.b || t.b==t.c || t.a==t.c) return false;
  }
  return true;
}

AABB Mesh::bounds() const noexcept {
  AABB box;
  for (const auto& v : vertices) box.expand(v.position);
  return box;
}

} // namespace chimera3d4d
