#pragma once
#include <string>
#include <vector>
struct ProviderResult { bool ok; std::string status; std::string message; };
class DevOpsProvider { public: virtual ~DevOpsProvider()=default; virtual ProviderResult validate()=0; virtual ProviderResult start(const std::string& pipeline)=0; virtual ProviderResult cancel(const std::string& run)=0; virtual ProviderResult status(const std::string& run)=0; virtual ProviderResult logs(const std::string& run)=0; virtual ProviderResult artifacts(const std::string& run)=0; virtual ProviderResult deploy(const std::string& environment,const std::string& artifact)=0; };