#pragma once
#include <array>
#include <cstdint>
#include <stdexcept>
#include <string>
#include <vector>
namespace chimera::mobile {
template <std::size_t Bits> class RegisterN {
 static_assert(Bits>0 && Bits%64==0,"RegisterN width must be a positive multiple of 64");
public:
 static constexpr std::size_t bit_width=Bits, word_count=Bits/64;
 std::array<std::uint64_t,word_count> w{};
 RegisterN()=default; explicit RegisterN(std::uint64_t x){w[0]=x;}
 bool is_zero()const{for(auto x:w)if(x)return false;return true;} std::uint64_t low64()const{return w[0];}
 RegisterN& add_assign(const RegisterN& r){unsigned __int128 c=0;for(size_t i=0;i<word_count;++i){auto s=(unsigned __int128)w[i]+r.w[i]+c;w[i]=(uint64_t)s;c=s>>64;}return *this;}
 RegisterN operator+(const RegisterN&r)const{auto o=*this;return o.add_assign(r);} 
 RegisterN operator-(const RegisterN&r)const{auto o=*this;uint64_t b=0;for(size_t i=0;i<word_count;++i){auto a=o.w[i],x=r.w[i],t=a-x-b;b=b?(a<=x):(a<x);o.w[i]=t;}return o;}
 RegisterN operator&(const RegisterN&r)const{RegisterN o;for(size_t i=0;i<word_count;++i)o.w[i]=w[i]&r.w[i];return o;}
 RegisterN operator|(const RegisterN&r)const{RegisterN o;for(size_t i=0;i<word_count;++i)o.w[i]=w[i]|r.w[i];return o;}
 RegisterN operator^(const RegisterN&r)const{RegisterN o;for(size_t i=0;i<word_count;++i)o.w[i]=w[i]^r.w[i];return o;}
 RegisterN shl(size_t n)const{RegisterN o;if(n>=Bits)return o;size_t q=n/64,r=n%64;for(size_t i=word_count;i-- >0;){if(i<q)continue;o.w[i]=w[i-q]<<r;if(r&&i>q)o.w[i]|=w[i-q-1]>>(64-r);}return o;}
 RegisterN shr(size_t n)const{RegisterN o;if(n>=Bits)return o;size_t q=n/64,r=n%64;for(size_t i=0;i<word_count-q;++i){o.w[i]=w[i+q]>>r;if(r&&i+q+1<word_count)o.w[i]|=w[i+q+1]<<(64-r);}return o;}
 std::string hex()const{static constexpr char h[]="0123456789abcdef";std::string s;s.reserve(Bits/4);for(size_t i=word_count;i-- >0;)for(int b=60;b>=0;b-=4)s.push_back(h[(w[i]>>b)&15]);auto p=s.find_first_not_of('0');return p==std::string::npos?"0":s.substr(p);}
};
using U64=RegisterN<64>;using U128=RegisterN<128>;using U256=RegisterN<256>;using U512=RegisterN<512>;using U1024=RegisterN<1024>;using U2048=RegisterN<2048>;using U4096=RegisterN<4096>;using U8192=RegisterN<8192>;using U16384=RegisterN<16384>;
class WideInt{std::size_t bits_;std::vector<uint64_t> limbs_;public:explicit WideInt(size_t bits=64):bits_(bits),limbs_((bits+63)/64){}size_t bit_width()const{return bits_;}auto& limbs(){return limbs_;}const auto& limbs()const{return limbs_;}static WideInt from_u64(uint64_t x,size_t bits=64){WideInt v(bits);v.limbs_[0]=x;return v;}WideInt add(const WideInt&r)const{if(bits_!=r.bits_)throw std::invalid_argument("N-bit width mismatch");WideInt o(bits_);unsigned __int128 c=0;for(size_t i=0;i<limbs_.size();++i){auto s=(unsigned __int128)limbs_[i]+r.limbs_[i]+c;o.limbs_[i]=(uint64_t)s;c=s>>64;}return o;}};
}
