#include "animation.hpp"
#include <algorithm>
namespace chimera3d4d::animation { double sample(const Track& t,double x){ if(t.keys.empty()) return 0; if(x<=t.keys.front().time)return t.keys.front().value; if(x>=t.keys.back().time)return t.keys.back().value; for(size_t i=1;i<t.keys.size();++i){auto&a=t.keys[i-1];auto&b=t.keys[i];if(x<=b.time){double u=(x-a.time)/(b.time-a.time);return a.value+(b.value-a.value)*u;}} return 0;} }
