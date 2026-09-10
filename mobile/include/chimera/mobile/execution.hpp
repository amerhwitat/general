#pragma once
#include <algorithm>
#include <cstdint>
namespace chimera::mobile { enum class ExecutionClass{Arm64Native,ChimeraR8192,ChimeraC8192,Vector,Tensor,Emulated}; struct ExecutionProfile{ExecutionClass kind{ExecutionClass::Arm64Native};uint32_t logical_bits{64};uint32_t lanes{1};bool lazy_state{true};}; class ExecutionSelector{public:ExecutionProfile select(uint64_t bits,bool vector,bool tensor)const{if(tensor)return{ExecutionClass::Tensor,8192,128,true};if(vector&&bits>256)return{ExecutionClass::Vector,(uint32_t)bits,std::max<uint32_t>(1,8192/(uint32_t)bits),true};if(bits>=8192)return{ExecutionClass::ChimeraR8192,8192,128,true};if(bits>=4096)return{ExecutionClass::ChimeraC8192,4096,64,true};return{ExecutionClass::Arm64Native,64,1,true};}}; }
