#include <string>
#include <unordered_map>
#include <regex>
#include <cmath>
#include <algorithm>
#include <cctype>
struct Contact{std::string email,name,status="active",consent="unknown",source,tags;};
class RNNLLM{double state=0;public:double score(const std::string&s){for(unsigned char c:s)state=std::tanh(.86*state+.14*(c%97)/96.0);return(state+1)/2;}};
class EmailListManager{std::unordered_map<std::string,Contact> contacts;RNNLLM ai;public:bool add(Contact c){std::transform(c.email.begin(),c.email.end(),c.email.begin(),[](unsigned char x){return char(std::tolower(x));});if(!std::regex_match(c.email,std::regex(R"(^[^@\s]+@[^@\s]+\.[^@\s]+$)")))return false;return contacts.emplace(c.email,std::move(c)).second;}double rank(const std::string&e){auto i=contacts.find(e);return i==contacts.end()?0:ai.score(i->second.email+" "+i->second.tags);}size_t size()const{return contacts.size();}};
