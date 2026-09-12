#include "chimera3d4d/scene.hpp"
#include <cassert>
using namespace chimera3d4d;
int main() {
  Scene scene;
  SceneObject cube;
  cube.name = "Cube";
  cube.mesh.vertices = {{{0,0,0}}, {{1,0,0}}, {{0,1,0}}};
  cube.mesh.triangles = {{{0,1,2}}};
  cube.samples.push_back({0.0, {}});
  cube.samples.push_back({1.0, {{1,0,0},{0,0,0},{1,1,1}}});
  const auto id = scene.addObject(std::move(cube));
  assert(id == 1 && scene.size() == 1 && scene.validate());
  assert(scene.find(id) != nullptr);
  return 0;
}
