#pragma once
#include <string>
namespace chimera::mobile { struct SwiftTarget { std::string runtime="swift"; std::string package_manager="swiftpm"; bool foundation=true; bool foundation_networking=true; bool swift_nio=true; bool proprietary_ios_frameworks=false; }; }
