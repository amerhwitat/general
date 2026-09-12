#include "StateMachine.hpp"
StateMachine::StateMachine(std::string workflow):workflow_(std::move(workflow)){}
bool StateMachine::allowed(const std::string& f,const std::string& t) const {
 if(f==t) return false;
 if(workflow_=="scrum"||workflow_=="kanban"||workflow_=="scrumban"||workflow_=="hybrid") return (f=="backlog"&&t=="ready")||(f=="ready"&&t=="in_progress")||(f=="in_progress"&&(t=="review"||t=="blocked"))||(f=="review"&&t=="done")||(f=="blocked"&&t=="in_progress");
 if(workflow_=="itil_incident") return (f=="new"&&t=="triaged")||(f=="triaged"&&t=="in_progress")||(f=="in_progress"&&t=="resolved")||(f=="resolved"&&t=="closed")||(f=="in_progress"&&t=="blocked");
 return (f=="backlog"&&t=="ready")||(f=="ready"&&t=="in_progress")||(f=="in_progress"&&t=="done");
}
TransitionResult StateMachine::transition(const std::string& f,const std::string& t,const std::string& actor) const { if(actor.empty()) return {false,f,"actor required",{}}; if(!allowed(f,t)) return {false,f,"transition not allowed",{}}; return {true,t,{}, {"workflow."+workflow_+".transitioned"}}; }