#pragma once
#include <array>
#include <cstdint>
#include <string>
#include <vector>

namespace chimera3d4d::texture {
struct UV { float u{}, v{}; };
enum class Channel : std::uint8_t { BaseColor, Metallic, Roughness, Normal, Height, Emission, Opacity };
struct Layer { std::string name; Channel channel{Channel::BaseColor}; std::uint32_t width{}, height{}; std::vector<float> pixels; };
struct UVSet { std::string name{"UVMap"}; std::vector<UV> coordinates; };
struct TextureAsset { std::string uri; std::vector<Layer> layers; std::vector<UVSet> uvSets; };
} // namespace chimera3d4d::texture
