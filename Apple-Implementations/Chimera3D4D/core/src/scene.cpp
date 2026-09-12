#include "chimera3d4d/scene.hpp"

namespace chimera3d4d {
std::uint64_t Scene::addObject(SceneObject object) {
  if (object.id == 0) object.id = nextId_++;
  else if (object.id >= nextId_) nextId_ = object.id + 1;
  const auto id = object.id;
  objects_[id] = std::move(object);
  return id;
}
const SceneObject* Scene::find(std::uint64_t id) const {
  const auto it = objects_.find(id);
  return it == objects_.end() ? nullptr : &it->second;
}
bool Scene::validate() const {
  for (const auto& [id, object] : objects_) {
    if (id == 0 || object.id != id) return false;
    for (const auto& tri : object.mesh.triangles) {
      if (tri.a >= object.mesh.vertices.size() || tri.b >= object.mesh.vertices.size() || tri.c >= object.mesh.vertices.size()) return false;
    }
  }
  return true;
}
}
