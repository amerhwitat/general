#include <fstream>
#include <iostream>
#include <regex>
#include <set>
#include <string>
int main(int argc,char**argv){if(argc<2){std::cerr<<"usage: webcontactcrawler <html-file>\n";return 1;}std::ifstream f(argv[1]);std::string s((std::istreambuf_iterator<char>(f)),{});std::regex r(R"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})");std::set<std::string> out;for(std::sregex_iterator i(s.begin(),s.end(),r),e;i!=e;++i)out.insert(i->str());std::cout<<"DONE unique_emails="<<out.size()<<"\n";for(auto&x:out)std::cout<<x<<"\n";}
