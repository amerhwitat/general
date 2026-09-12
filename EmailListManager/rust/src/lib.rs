use std::collections::HashMap;
#[derive(Clone,Debug)]pub struct Contact{pub email:String,pub name:String,pub status:String,pub consent:String,pub source:String,pub tags:String}
pub struct RnnLlm{state:f64}
impl RnnLlm{pub fn new()->Self{Self{state:0.0}}pub fn score(&mut self,s:&str)->f64{for c in s.chars(){self.state=(0.86*self.state+0.14*((c as u32%97)as f64/96.0)).tanh();}(self.state+1.0)/2.0}}
pub struct EmailListManager{pub contacts:HashMap<String,Contact>,pub ai:RnnLlm}
impl EmailListManager{pub fn new()->Self{Self{contacts:HashMap::new(),ai:RnnLlm::new()}}pub fn add(&mut self,mut c:Contact)->bool{c.email=c.email.trim().to_lowercase();if !c.email.contains('@')||!c.email.contains('.') {return false}self.contacts.insert(c.email.clone(),c);true}pub fn rank(&mut self,email:&str)->Option<f64>{self.contacts.get(email).map(|c|self.ai.score(&(c.email.clone()+" "+&c.tags)))}}
