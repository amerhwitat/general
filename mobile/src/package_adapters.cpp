#include "chimera/mobile/package_adapters.hpp"
namespace chimera::mobile {
AdapterCommand PackageAdapters::route(const std::string&c){
 if(c=="pacman")return{Manager::Pacman,"pacman",PackageFormat::Pacman,true};
 if(c=="dpkg")return{Manager::Dpkg,"dpkg",PackageFormat::Dpkg,true};
 if(c=="apt")return{Manager::Apt,"apt",PackageFormat::Apt,true};
 if(c=="apt-get")return{Manager::AptGet,"apt-get",PackageFormat::Apt,true};
 if(c=="aptitude")return{Manager::Aptitude,"aptitude",PackageFormat::Apt,true};
 if(c=="rpm")return{Manager::Rpm,"rpm",PackageFormat::Rpm,true};
 if(c=="dnf")return{Manager::Dnf,"dnf",PackageFormat::Dnf,true};
 if(c=="yum")return{Manager::Yum,"yum",PackageFormat::Yum,true};
 if(c=="apk")return{Manager::Apk,"apk",PackageFormat::Apk,true};
 if(c=="nix")return{Manager::Nix,"nix",PackageFormat::Nix,true};
 if(c=="flatpak")return{Manager::Flatpak,"flatpak",PackageFormat::Flatpak,true};
 if(c=="snap")return{Manager::Snap,"snap",PackageFormat::Snap,true};
 if(c=="appimage")return{Manager::AppImage,"AppImage",PackageFormat::AppImage,true};
 if(c=="git")return{Manager::Git,"git",PackageFormat::GitSource,true};
 if(c=="gh")return{Manager::Github,"gh",PackageFormat::GitSource,true};
 return{Manager::Chimera,"chimera-pkg",PackageFormat::Native,true};}
const char*PackageAdapters::canonical(Manager m){switch(m){case Manager::Pacman:return"pacman";case Manager::Dpkg:return"dpkg";case Manager::Apt:return"apt";case Manager::AptGet:return"apt-get";case Manager::Aptitude:return"aptitude";case Manager::Rpm:return"rpm";case Manager::Dnf:return"dnf";case Manager::Yum:return"yum";case Manager::Apk:return"apk";case Manager::Nix:return"nix";case Manager::Flatpak:return"flatpak";case Manager::Snap:return"snap";case Manager::AppImage:return"AppImage";case Manager::Git:return"git";case Manager::Github:return"gh";default:return"chimera-pkg";}}
}
