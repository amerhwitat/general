#pragma once
#include <string>
#include <vector>
struct TransitionResult { bool accepted; std::string state; std::string error; std::vector<std::string> events; };
class StateMachine { public: explicit StateMachine(std::string workflow); TransitionResult transition(const std::string& from,const std::string& to,const std::string& actor) const; private: std::string workflow_; bool allowed(const std::string& from,const std::string& to) const; };