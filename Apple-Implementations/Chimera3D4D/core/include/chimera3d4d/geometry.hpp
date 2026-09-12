#pragma once

#include <array>
#include <cmath>
#include <cstdint>
#include <limits>
#include <vector>

namespace chimera3d4d {

struct Vec3 {
  double x{}, y{}, z{};
  constexpr Vec3 operator+(const Vec3& r) const noexcept { return {x+r.x,y+r.y,z+r.z}; }
  constexpr Vec3 operator-(const Vec3& r) const noexcept { return {x-r.x,y-r.y,z-r.z}; }
  constexpr Vec3 operator*(double s) const noexcept { return {x*s,y*s,z*s}; }
  constexpr Vec3 operator/(double s) const noexcept { return {x/s,y/s,z/s}; }
  constexpr double dot(const Vec3& r) const noexcept { return x*r.x+y*r.y+z*r.z; }
  constexpr Vec3 cross(const Vec3& r) const noexcept { return {y*r.z-z*r.y,z*r.x-x*r.z,x*r.y-y*r.x}; }
  double length() const noexcept { return std::sqrt(dot(*this)); }
  Vec3 normalized() const noexcept { const double n=length(); return n>1e-12 ? *this/n : Vec3{}; }
};

struct Transform {
  Vec3 translation{};
  Vec3 rotation{}; // Euler radians; quaternion support belongs to animation/rigging.
  Vec3 scale{1.0,1.0,1.0};
  Vec3 apply(const Vec3& p) const noexcept { return {p.x*scale.x+translation.x,p.y*scale.y+translation.y,p.z*scale.z+translation.z}; }
};

struct Vertex { Vec3 position{}; Vec3 normal{}; std::array<float,2> uv{}; };
struct Triangle { std::uint32_t a{}, b{}, c{}; };

struct AABB {
  Vec3 min{std::numeric_limits<double>::infinity()};
  Vec3 max{-std::numeric_limits<double>::infinity()};
  void expand(const Vec3& p) noexcept;
  bool valid() const noexcept;
};

struct Mesh {
  std::vector<Vertex> vertices;
  std::vector<Triangle> triangles;
  bool validate() const noexcept;
  AABB bounds() const noexcept;
};

} // namespace chimera3d4d
