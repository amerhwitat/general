#pragma once
#include "Provider.hpp"
#include <map>
#include <memory>
class ProviderRegistry { std::map<std::string,std::shared_ptr<DevOpsProvider>> providers_; public: void add(std::string name,std::shared_ptr<DevOpsProvider> provider){providers_[std::move(name)]=std::move(provider);} std::shared_ptr<DevOpsProvider> get(const std::string& name) const {auto i=providers_.find(name); return i==providers_.end()?nullptr:i->second;} };