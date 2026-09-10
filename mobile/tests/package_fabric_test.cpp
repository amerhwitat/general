#include "chimera/mobile/package_fabric.hpp"
#include "chimera/mobile/package_adapters.hpp"
#include <cassert>
using namespace chimera::mobile;
int main(){assert(PackageFabric::detect_format("x.deb")==PackageFormat::Deb);assert(PackageFabric::compatible(PackageFormat::Deb,PackageTarget::Arm64));PackageRecord p{"demo","1.0","arm64","x.deb","abc",PackageFormat::Deb,PackageTarget::Arm64,SignatureState::Verified,false};PackageFabric f;assert(f.validate(p));auto plan=f.plan(p,{"libc6"});assert(plan.transactional&&plan.sandboxed);assert(PackageAdapters::route("apt-get").manager==Manager::AptGet);assert(PackageAdapters::route("dnf").manager==Manager::Dnf);return 0;}
