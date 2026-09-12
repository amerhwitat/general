#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub enum Mode { Offline, Client, Server, Host, P2P, Hybrid }

#[derive(Clone, Debug)]
pub struct Profile { pub nickname: String, pub avatar_ref: Option<String> }

#[derive(Clone, Debug)]
pub struct Config {
    pub mode: Mode,
    pub host: String,
    pub port: u16,
    pub application_id: String,
    pub room: String,
    pub profile: Profile,
    pub enable_p2p: bool,
    pub tls: bool,
}

#[derive(Clone, Debug)]
pub struct Envelope {
    pub version: u8,
    pub kind: String,
    pub id: String,
    pub room: String,
    pub sender: String,
    pub timestamp_ms: u64,
    pub payload: Vec<u8>,
}

pub trait Transport {
    fn start(&mut self, config: &Config) -> Result<(), String>;
    fn stop(&mut self);
    fn send(&mut self, message: &Envelope) -> Result<(), String>;
    fn running(&self) -> bool;
}

pub fn normalize_nickname(input: &str) -> String {
    let value = input.split_whitespace().collect::<Vec<_>>().join(" ");
    let value = if value.is_empty() { "Player" } else { &value };
    value.chars().take(32).collect()
}
