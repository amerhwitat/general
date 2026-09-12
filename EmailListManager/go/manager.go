package main

import("bufio";"encoding/csv";"math";"os";"regexp";"strings")
type Contact struct{Email,Name,Status,Consent,Source,Tags string}
type RNNLLM struct{State float64}
func(r *RNNLLM) Score(s string)float64{for _,c:=range s{r.State=math.Tanh(.86*r.State+.14*float64(int(c)%97)/96)};return(r.State+1)/2}
type Manager struct{Contacts map[string]Contact; AI RNNLLM}
func NewManager()*Manager{return &Manager{Contacts:map[string]Contact{}}}
func(m *Manager)Add(c Contact)bool{c.Email=strings.ToLower(strings.TrimSpace(c.Email));if !regexp.MustCompile(`^[^@\s]+@[^@\s]+\.[^@\s]+$`).MatchString(c.Email){return false};m.Contacts[c.Email]=c;return true}
func(m *Manager)ImportCSV(path string)int{f,e:=os.Open(path);if e!=nil{return 0};defer f.Close();r:=csv.NewReader(bufio.NewReader(f)); rows,_:=r.ReadAll();n:=0;for i,row:=range rows{if i==0||len(row)==0{continue};c:=Contact{Email:row[0]};if len(row)>1{c.Name=row[1]};if m.Add(c){n++}};return n}
func(m *Manager)Rank(email string)float64{return m.AI.Score(email+" "+m.Contacts[email].Tags)}
