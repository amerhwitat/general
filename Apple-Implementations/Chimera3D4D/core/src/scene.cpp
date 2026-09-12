#include "chimera3d4d/scene.hpp"
#include <algorithm>
#include <cmath>
#include <limits>

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

bool Scene::evaluate(std::uint64_t id, double time, Transform& out) const {
  const auto* object = find(id);
  if (!object || object->samples.empty() || !std::isfinite(time)) return false;
  const auto& samples = object->samples;
  if (time <= samples.front().time) { out = samples.front().transform; return true; }
  if (time >= samples.back().time) { out = samples.back().transform; return true; }
  for (std::size_t i=1; i<samples.size(); ++i) {
    const auto& a=samples[i-1]; const auto& b=samples[i];
    if (time <= b.time) {
      const double u=(time-a.time)/(b.time-a.time);
      auto lerp=[u](double x,double y){ return x+(y-x)*u; };
      out.translation={lerp(a.transform.translation.x,b.transform.translation.x),lerp(a.transform.translation.y,b.transform.translation.y),lerp(a.transform.translation.z,b.transform.translation.z)};
      out.rotation={lerp(a.transform.rotation.x,b.transform.rotation.x),lerp(a.transform.rotation.y,b.transform.rotation.y),lerp(a.transform.rotation.z,b.transform.rotation.z)};
      out.scale={lerp(a.transform.scale.x,b.transform.scale.x),lerp(a.transform.scale.y,b.transform.scale.y),lerp(a.transform.scale.z,b.transform.scale.z)};
      return true;
    }
  }
  return false;
}

bool Scene::validate() const {
  for (const auto& [id, object] : objects_) {
    if (id == 0 || object.id != id || !object.mesh.validate()) return false;
    double previous = -std::numeric_limits<double>::infinity();
    for (const auto& sample : object.samples) {
      if (!std::isfinite(sample.time) || sample.time < previous) return false;
      previous = sample.time;
    }
  }
  return true;
}
}
