<?php
function init_db(string $dbFile = 'emails.db'): SQLite3 {
    $db = new SQLite3($dbFile);
    $db->exec('CREATE TABLE IF NOT EXISTS emails (email TEXT PRIMARY KEY, title TEXT, website TEXT)');
    return $db;
}
function save_email(string $email, string $title = '', string $website = '', string $dbFile = 'emails.db'): void {
    $db = init_db($dbFile);
    $stmt = $db->prepare('INSERT OR IGNORE INTO emails(email,title,website) VALUES (:e,:t,:w)');
    $stmt->bindValue(':e',$email,SQLITE3_TEXT); $stmt->bindValue(':t',$title,SQLITE3_TEXT); $stmt->bindValue(':w',$website,SQLITE3_TEXT); $stmt->execute(); $db->close();
}
function export_csv(string $filename = 'emails.csv', string $dbFile = 'emails.db'): void {
    $db = init_db($dbFile); $res = $db->query('SELECT email,title,website FROM emails');
    $f = fopen($filename, 'w'); fputcsv($f, ['Email','Title','Website']);
    while ($row = $res->fetchArray(SQLITE3_ASSOC)) fputcsv($f, [$row['email'],$row['title'],$row['website']]);
    fclose($f); $db->close();
}
