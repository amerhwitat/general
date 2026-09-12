#include "rigging.hpp"
namespace chimera3d4d::rigging {
bool Skeleton::valid() const noexcept {
  for (std::size_t i=0; i<joints.size(); ++i) {
    if (joints[i].parent < -1 || joints[i].parent >= static_cast<int>(joints.size()) || joints[i].parent == static_cast<int>(i)) return false;
  }
  return true;
}
}
