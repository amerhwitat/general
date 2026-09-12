#pragma once
#include "chimera3d4d/geometry.hpp"
#include <cstdint>
namespace chimera3d4d::rendering { enum class Backend { Metal, OpenGL, WebGPU }; struct Camera { Vec3 position{}; Vec3 target{}; double fov{60}; }; struct Frame { std::uint32_t width{}, height{}; Backend backend{Backend::OpenGL}; }; }
