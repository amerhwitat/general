#include "sculpt.hpp"
#include <cmath>
namespace chimera3d4d::sculpt { void apply(Mesh& m, Vec3 c, Vec3 d, const Brush& b){ for(auto& v:m.vertices){ double dx=v.position.x-c.x,dy=v.position.y-c.y,dz=v.position.z-c.z; double dist=std::sqrt(dx*dx+dy*dy+dz*dz); if(dist<=b.radius){ double t=1.0-dist/b.radius; v.position.x+=d.x*b.strength*t; v.position.y+=d.y*b.strength*t; v.position.z+=d.z*b.strength*t; } } } }
