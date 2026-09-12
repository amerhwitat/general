#include <iostream>
extern "C" int email_extractor_native_version();
int main() { std::cout << "EmailExtractor native " << email_extractor_native_version() << '\n'; }
