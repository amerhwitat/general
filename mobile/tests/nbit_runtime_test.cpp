#include "chimera/mobile/nbit.hpp"
#include "chimera/mobile/execution.hpp"
#include <cassert>
int main(){using namespace chimera::mobile;U4096 a(7),b(9);auto c=a+b;assert(c.low64()==16);assert(c.shl(64).shr(64).low64()==16);assert(U8192::bit_width==8192&&U16384::bit_width==16384);auto x=WideInt::from_u64(42,12345);auto y=x.add(WideInt::from_u64(1,12345));assert(y.limbs()[0]==43);ExecutionSelector s;assert(s.select(8192,false,false).logical_bits==8192);return 0;}
