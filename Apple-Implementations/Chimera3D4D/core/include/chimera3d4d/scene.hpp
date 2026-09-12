#pragma once
#include "geometry.hpp"
#include <cstdint>
#include <string>
#include <unordered_map>
#include <vector>

namespace chimera3d4d {
struct TimeSample { double time{}; Transform transform{}; };
struct SceneObject { std::uint64_t id{}; std::string name; Mesh mesh; std::vector<TimeSample> samples; std::array<float,128> state128{}; };
class Scene {
public:
  std::uint64_t addObject(SceneObject object);
  const SceneObject* find(std::uint64_t id) const;
  bool validate() const;
  std::size_t size() const noexcept { return objects_.size(); }
private:
  std::uint64_t nextId_{1};
  std::unordered_map<std::uint64_t, SceneObject> objects_;
};
}
