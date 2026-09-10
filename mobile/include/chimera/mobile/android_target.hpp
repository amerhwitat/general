#pragma once
#include <string>
namespace chimera::mobile { struct AndroidTarget { std::string image="waydroid-compatible"; bool namespaces=true; bool binder_bridge=true; bool apk=true; bool direct_hardware=false; bool sandbox=true; }; }
