#include "chimera3d4d/scene.hpp"
#include "chimera3d4d/geometry.hpp"
#include <cassert>
#include <cmath>

using namespace chimera3d4d;

int main() {
  const Vec3 a{1, 0, 0}, b{0, 1, 0};
  const auto cross = a.cross(b);
  assert(cross.z == 1.0);
  assert(std::abs(a.length() - 1.0) < 1e-12);

  Scene scene;
  SceneObject object;
  object.name = "CubePreview";
  object.mesh.vertices = {{{0,0,0}}, {{1,0,0}}, {{0,1,0}}};
  object.mesh.triangles = {{{0,1,2}}};
  object.samples.push_back({0.0, {}});
  object.samples.push_back({1.0, {{1,0,0},{0,0,0},{1,1,1}}});
  const auto id = scene.addObject(std::move(object));

  assert(id == 1 && scene.size() == 1 && scene.validate());
  assert(scene.find(id) != nullptr);
  const auto box = scene.find(id)->mesh.bounds();
  assert(box.valid() && box.min.x == 0.0 && box.max.x == 1.0);

  Transform mid;
  assert(scene.evaluate(id, 0.5, mid));
  assert(std::abs(mid.translation.x - 0.5) < 1e-12);
  assert(std::abs(mid.scale.x - 1.0) < 1e-12);

  SceneObject invalid;
  invalid.mesh.vertices = {{{0,0,0}}, {{1,0,0}}};
  invalid.mesh.triangles = {{{0,1,2}}};
  scene.addObject(std::move(invalid));
  assert(!scene.validate());
  return 0;
}
