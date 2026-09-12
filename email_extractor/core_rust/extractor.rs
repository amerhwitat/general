use regex::Regex;
use reqwest::Client;
use trust_dns_resolver::{TokioAsyncResolver, config::*};

pub async fn fetch_page(url:&str)->String{if !(url.starts_with("http://")||url.starts_with("https://")){return String::new()} let c=Client::builder().timeout(std::time::Duration::from_secs(10)).user_agent("ChimeraEmailExtractor/1.0").build().unwrap(); match c.get(url).send().await{Ok(r)=>r.text().await.unwrap_or_default(),Err(_)=>String::new()}}
pub fn extract_emails(html:&str)->Vec<String>{let re=Regex::new(r"(?i)(?<![\w.+-])([a-z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-z0-9-]+(?:\.[a-z0-9-]+)+)(?![\w.-])").unwrap();let mut v:Vec<String>=re.captures_iter(html).map(|c|c[1].trim_matches(|x:char|".,;:<>[](){}\"".contains(x)).to_lowercase()).collect();v.sort();v.dedup();v}
pub async fn validate_email(email:&str)->bool{let Some(domain)=email.split('@').nth(1)else{return false};let resolver=match TokioAsyncResolver::tokio(ResolverConfig::default(),ResolverOpts::default()){Ok(r)=>r,Err(_)=>return false};resolver.mx_lookup(domain).await.map(|r|!r.is_empty()).unwrap_or(false)}
