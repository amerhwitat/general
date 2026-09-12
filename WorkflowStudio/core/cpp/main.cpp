#include <string>
#include <vector>
#include <array>
namespace chimera::workflow {
struct WorkItem { std::string id,title,status="backlog"; int priority=3; };
struct SequenceInsight { double score{}; bool anomaly{}; };
class NeuralSequenceEngine { public: SequenceInsight score(const std::vector<double>& v) const { if(v.empty()) return {}; double m=0;for(double x:v)m+=x;m/=v.size();double d=v.back()-m;if(d<0)d=-d;return {d,d>1.0}; } };
struct VoiceCommand { std::string locale; std::string text; };
}
int main(){chimera::workflow::NeuralSequenceEngine e;auto r=e.score({1,1,2});return r.anomaly?0:0;}
