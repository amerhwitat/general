cmake_minimum_required(VERSION 3.20)
project(chimera_mobile LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_library(chimera_mobile STATIC
  src/runtime.cpp
  src/binder.cpp
  src/power.cpp
  src/graphics.cpp
  src/package_manager.cpp)
target_include_directories(chimera_mobile PUBLIC include)
add_executable(chimera_mobile_test tests/mobile_runtime_test.cpp)
target_link_libraries(chimera_mobile_test PRIVATE chimera_mobile)
add_executable(chimera_mobile_nbit_test tests/nbit_runtime_test.cpp)
target_link_libraries(chimera_mobile_nbit_test PRIVATE chimera_mobile)
enable_testing()
add_test(NAME chimera_mobile COMMAND chimera_mobile_test)
add_test(NAME chimera_mobile_nbit COMMAND chimera_mobile_nbit_test)
