#include "chimera/mobile/android_target.hpp"
#include "chimera/mobile/swift_target.hpp"
#include "chimera/mobile/app_store.hpp"
#include <cassert>
using namespace chimera::mobile;
int main(){AndroidTarget a;assert(a.namespaces&&a.binder_bridge&&a.apk&&a.sandbox&&!a.direct_hardware);SwiftTarget s;assert(s.foundation&&s.swift_nio&&s.proprietary_ios_frameworks==false);AppStore st;PackageRecord p{"hello","1","arm64","hello.deb","hash",PackageFormat::Deb,PackageTarget::Arm64,SignatureState::Verified,false};st.publish({p,"chimera-main","stable","default"});assert(st.find("hello")!=nullptr);assert(st.search("hel").size()==1);return 0;}
