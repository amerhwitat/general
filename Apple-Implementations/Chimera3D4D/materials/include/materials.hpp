#pragma once
#include <array>
#include <string>
namespace chimera3d4d::materials { struct PBR { std::array<float,4> baseColor{1,1,1,1}; float metallic{}; float roughness{0.5f}; float emission{}; }; struct Material { std::string name; PBR pbr; }; }
