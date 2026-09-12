#include "modeling.hpp"
namespace chimera3d4d::modeling {
Mesh cube(double s){ const double h=s*.5; Mesh m; m.vertices={{{-h,-h,-h}},{{h,-h,-h}},{{h,h,-h}},{{-h,h,-h}},{{-h,-h,h}},{{h,-h,h}},{{h,h,h}},{{-h,h,h}}}; m.triangles={{{0,1,2}},{{0,2,3}},{{4,6,5}},{{4,7,6}},{{0,4,5}},{{0,5,1}},{{3,2,6}},{{3,6,7}},{{1,5,6}},{{1,6,2}},{{0,3,7}},{{0,7,4}}}; return m; }
void translate(Mesh& m, Vec3 d){ for(auto& v:m.vertices){v.position.x+=d.x;v.position.y+=d.y;v.position.z+=d.z;} }
}
