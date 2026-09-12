package email_extractor.core_java;

import java.io.*;
import java.sql.*;

public final class Storage {
    private static final String DB = "emails.db";
    private Storage() {}

    public static void init() throws SQLException {
        try (Connection c = DriverManager.getConnection("jdbc:sqlite:" + DB);
             Statement s = c.createStatement()) {
            s.executeUpdate("CREATE TABLE IF NOT EXISTS emails (email TEXT PRIMARY KEY, title TEXT, website TEXT)");
        }
    }

    public static void saveEmail(String email, String title, String website) throws SQLException {
        try (Connection c = DriverManager.getConnection("jdbc:sqlite:" + DB);
             PreparedStatement p = c.prepareStatement("INSERT OR IGNORE INTO emails(email,title,website) VALUES (?,?,?)")) {
            p.setString(1,email); p.setString(2,title); p.setString(3,website); p.executeUpdate();
        }
    }

    public static void exportCsv(String filename) throws SQLException, IOException {
        init();
        try (Connection c = DriverManager.getConnection("jdbc:sqlite:" + DB);
             Statement s = c.createStatement(); ResultSet r = s.executeQuery("SELECT email,title,website FROM emails");
             BufferedWriter w = new BufferedWriter(new FileWriter(filename))) {
            w.write("Email,Title,Website"); w.newLine();
            while (r.next()) { w.write(csv(r.getString(1))+","+csv(r.getString(2))+","+csv(r.getString(3))); w.newLine(); }
        }
    }
    private static String csv(String v) { return "\"" + (v == null ? "" : v.replace("\"", "\"\"")) + "\""; }
}
