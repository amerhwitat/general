package main
import("encoding/json";"log";"net/http";"sync")
type Project struct{ID string `json:"id"`; Name string `json:"name"`; Methodology string `json:"methodology"`}
var mu sync.RWMutex; var projects=map[string]Project{}
func main(){http.HandleFunc("/health",func(w http.ResponseWriter,_ *http.Request){json.NewEncoder(w).Encode(map[string]string{"status":"ok"})});http.HandleFunc("/api/projects",func(w http.ResponseWriter,r *http.Request){mu.Lock();defer mu.Unlock();if r.Method==http.MethodPost{var p Project;if json.NewDecoder(r.Body).Decode(&p)!=nil||p.ID==""{http.Error(w,"bad project",400);return};projects[p.ID]=p;w.WriteHeader(201);json.NewEncoder(w).Encode(p);return};list:=[]Project{};for _,p:=range projects{list=append(list,p)};json.NewEncoder(w).Encode(list)});log.Fatal(http.ListenAndServe(":8080",nil))}
