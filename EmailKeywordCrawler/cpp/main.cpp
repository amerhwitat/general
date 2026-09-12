#include <curl/curl.h>
#include <fstream>
#include <iostream>
#include <regex>
#include <set>
static size_t write_cb(void* p,size_t s,size_t n,void* u){((std::string*)u)->append((char*)p,s*n);return s*n;}
int main(int argc,char**argv){std::set<std::string> out;std::regex re(R"([A-Za-z0-9._%+-]+\s*(?:@|\[at\]|\(at\))\s*[A-Za-z0-9.-]+\s*(?:\.|\[dot\]|\(dot\))\s*[A-Za-z]{2,})");curl_global_init(CURL_GLOBAL_DEFAULT);for(int i=1;i<argc;i++){std::string t;CURL*c=curl_easy_init();curl_easy_setopt(c,CURLOPT_URL,argv[i]);curl_easy_setopt(c,CURLOPT_USERAGENT,"EmailKeywordCrawler/1.0");curl_easy_setopt(c,CURLOPT_WRITEFUNCTION,write_cb);curl_easy_setopt(c,CURLOPT_WRITEDATA,&t);auto rc=curl_easy_perform(c);curl_easy_cleanup(c);if(rc!=CURLE_OK)continue;for(std::sregex_iterator it(t.begin(),t.end(),re),e;it!=e;++it)out.insert(it->str());std::cout<<"page "<<argv[i]<<" emails="<<out.size()<<"\n";}std::ofstream f("emails.txt");for(auto&e:out)f<<e<<'\n';curl_global_cleanup();}
