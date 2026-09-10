#include "chimera/mobile/graphics.hpp"
namespace chimera::mobile { Compositor::Compositor(uint32_t hz):refresh_hz_(hz?hz:60){} bool Compositor::submit(Surface s){ return s.id!=0 && s.width>0 && s.height>0; } void Compositor::present(){ ++presented_; } }
