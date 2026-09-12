#pragma once
namespace chimera3d4d::dynamics { struct Step { double time{}; double dt{1.0/60.0}; }; class Solver { public: virtual ~Solver()=default; virtual void step(const Step&)=0; }; }
