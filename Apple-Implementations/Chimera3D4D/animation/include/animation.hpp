#pragma once
#include <string>
#include <vector>
namespace chimera3d4d::animation { struct Keyframe { double time{}; double value{}; }; struct Track { std::string channel; std::vector<Keyframe> keys; }; double sample(const Track&, double time); }
