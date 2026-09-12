use rusqlite::{params, Connection};
use std::fs::File;
use std::io::Write;

pub fn init_db(db: &str) -> rusqlite::Result<()> {
    let conn = Connection::open(db)?;
    conn.execute("CREATE TABLE IF NOT EXISTS emails (email TEXT PRIMARY KEY, title TEXT, website TEXT)", [])?;
    Ok(())
}
pub fn save_email(db: &str, email: &str, title: &str, website: &str) -> rusqlite::Result<()> {
    let conn = Connection::open(db)?;
    conn.execute("INSERT OR IGNORE INTO emails(email,title,website) VALUES (?1,?2,?3)", params![email,title,website])?;
    Ok(())
}
fn csv(s: &str) -> String { format!("\"{}\"", s.replace('"', "\"\"")) }
pub fn export_csv(db: &str, filename: &str) -> Result<(), Box<dyn std::error::Error>> {
    init_db(db)?; let conn = Connection::open(db)?;
    let mut stmt = conn.prepare("SELECT email,title,website FROM emails")?;
    let rows = stmt.query_map([], |r| Ok((r.get::<_,String>(0)?, r.get::<_,String>(1)?, r.get::<_,String>(2)?)))?;
    let mut file = File::create(filename)?; writeln!(file, "Email,Title,Website")?;
    for row in rows { let (e,t,w) = row?; writeln!(file, "{},{},{}", csv(&e),csv(&t),csv(&w))?; }
    Ok(())
}
