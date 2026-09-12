cmake_minimum_required(VERSION 3.20)
project(Chimera3D4D LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_library(chimera3d4d_core STATIC
  core/src/scene.cpp
  modeling/src/modeling.cpp
  sculpt/src/sculpt.cpp
  animation/src/animation.cpp)
target_include_directories(chimera3d4d_core PUBLIC core/include modeling/include sculpt/include animation/include)
add_executable(chimera3d4d_smoke tests/core_tests.cpp)
target_link_libraries(chimera3d4d_smoke PRIVATE chimera3d4d_core)
enable_testing()
add_test(NAME core_smoke COMMAND chimera3d4d_smoke)
