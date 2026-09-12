#pragma once
#include <string>
#include <vector>
namespace chimera3d4d::nodes { struct Node { std::string type; std::vector<int> inputs; }; struct Graph { std::vector<Node> nodes; }; }
