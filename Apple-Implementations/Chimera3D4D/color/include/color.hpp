#pragma once
#include <string>
namespace chimera3d4d::color {
enum class Transfer { Linear, SRGB, Rec709, PQ, HLG };
struct ColorSpace { std::string name{"Linear-sRGB"}; Transfer transfer{Transfer::Linear}; };
struct ColorValue { float r{}, g{}, b{}, a{1.0f}; ColorSpace space{}; };
} // namespace chimera3d4d::color
