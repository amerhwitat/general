cmake_minimum_required(VERSION 3.20)
project(Chimera3D4D LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

set(CHIMERA3D4D_INCLUDE_DIRS
  core/include modeling/include sculpt/include texture/include
  animation/include rigging/include motion/include dynamics/include
  rendering/include materials/include color/include vfx/include
  nodes/include compositor/include usd/include)

add_library(chimera3d4d_core STATIC
  core/src/scene.cpp
  core/src/geometry.cpp
  modeling/src/modeling.cpp
  sculpt/src/sculpt.cpp
  texture/src/texture.cpp
  animation/src/animation.cpp
  rigging/src/rigging.cpp
  motion/src/motion.cpp
  dynamics/src/dynamics.cpp
  rendering/src/rendering.cpp
  materials/src/materials.cpp
  color/src/color.cpp
  vfx/src/vfx.cpp
  nodes/src/nodes.cpp
  compositor/src/compositor.cpp
  usd/src/usd_adapter.cpp)

target_include_directories(chimera3d4d_core PUBLIC ${CHIMERA3D4D_INCLUDE_DIRS})
target_compile_features(chimera3d4d_core PUBLIC cxx_std_20)

if(MSVC)
  target_compile_options(chimera3d4d_core PRIVATE /W4 /permissive-)
else()
  target_compile_options(chimera3d4d_core PRIVATE -Wall -Wextra -Wpedantic)
endif()

add_executable(chimera3d4d_smoke tests/core_tests.cpp)
target_link_libraries(chimera3d4d_smoke PRIVATE chimera3d4d_core)

enable_testing()
add_test(NAME core_smoke COMMAND chimera3d4d_smoke)
