#pragma once
#include <cstdint>
namespace chimera::mobile {
struct Surface { uint64_t id{}; uint32_t width{}; uint32_t height{}; bool visible{true}; uint64_t z{}; };
class Compositor {
public:
  explicit Compositor(uint32_t refresh_hz = 60);
  bool submit(Surface s);
  uint32_t refresh_hz() const { return refresh_hz_; }
  uint64_t presented_frames() const { return presented_; }
  void present();
private:
  uint32_t refresh_hz_; uint64_t presented_{0};
};
}
