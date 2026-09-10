#include <cassert>
#include "chimera/mobile/runtime.hpp"
#include "chimera/mobile/binder.hpp"
#include "chimera/mobile/power.hpp"
#include "chimera/mobile/package_manager.hpp"
int main(){ using namespace chimera::mobile; Runtime rt; auto id=rt.register_app({"org.chimera.demo","Main",10001,128,false}); assert(rt.foreground(id)); assert(rt.snapshot().size()==1); BinderBus bus; auto s=bus.publish("activity",[](auto const& t){ return t.payload; }); assert(bus.transact(s,1,{1,2,3}).size()==3); PowerPolicy pp; assert(pp.evaluate({5,35000,20,10}).mode==PowerMode::BatterySaver); PackageManager pm; assert(pm.install({"org.chimera.demo","1.0","Main","arm64-v8a",true})); assert(pm.find("org.chimera.demo")); return 0; }
