#pragma once
#include <string>
namespace chimera3d4d::usd { class Adapter { public: virtual ~Adapter()=default; virtual bool exportScene(const std::string& path)=0; virtual bool importScene(const std::string& path)=0; }; }
