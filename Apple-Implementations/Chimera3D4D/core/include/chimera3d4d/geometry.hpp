#pragma once
#include <array>
#include <cstdint>
#include <vector>

namespace chimera3d4d {
struct Vec3 { double x{}, y{}, z{}; };
struct Transform { Vec3 translation{}; Vec3 rotation{}; Vec3 scale{1.0,1.0,1.0}; };
struct Vertex { Vec3 position{}; };
struct Triangle { std::uint32_t a{}, b{}, c{}; };
struct Mesh { std::vector<Vertex> vertices; std::vector<Triangle> triangles; };
}
