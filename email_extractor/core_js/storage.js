const sqlite3 = require('sqlite3').verbose();
const fs = require('node:fs');

const DB_FILE = 'emails.db';
const db = new sqlite3.Database(DB_FILE);

db.serialize(() => db.run('CREATE TABLE IF NOT EXISTS emails (email TEXT PRIMARY KEY, title TEXT, website TEXT)'));

function saveEmail(email, title = '', website = '') {
  return new Promise((resolve, reject) => {
    db.run('INSERT OR IGNORE INTO emails(email,title,website) VALUES (?,?,?)', [email, title, website], err => err ? reject(err) : resolve());
  });
}

function csv(value) { return `"${String(value ?? '').replaceAll('"', '""')}"`; }

function exportCsv(filename = 'emails.csv') {
  return new Promise((resolve, reject) => {
    db.all('SELECT email,title,website FROM emails', [], (err, rows) => {
      if (err) return reject(err);
      const data = ['Email,Title,Website', ...rows.map(r => [r.email, r.title, r.website].map(csv).join(','))].join('\n');
      fs.writeFileSync(filename, data, 'utf8'); resolve();
    });
  });
}

module.exports = { saveEmail, exportCsv };
