#include <stdio.h>
#include <regex.h>
int main(int argc,char**argv){if(argc<2)return 1;FILE*f=fopen(argv[1],"rb");if(!f)return 1;fseek(f,0,SEEK_END);long n=ftell(f);rewind(f);char*s=malloc((size_t)n+1);if(!s)return 1;fread(s,1,(size_t)n,f);s[n]=0;regex_t r;regcomp(&r,"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}",REG_EXTENDED|REG_ICASE);regmatch_t m;for(char*p=s;!regexec(&r,p,1,&m,0);p+=m.rm_eo)printf("%.*s\n",(int)(m.rm_eo-m.rm_so),p+m.rm_so);regfree(&r);free(s);}
