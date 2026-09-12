#pragma once
#include <cstdint>
namespace chimera3d4d::compositor { struct Image { std::uint32_t width{},height{}; }; struct Pass { Image input; Image output; }; }
