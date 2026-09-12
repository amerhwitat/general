using System.Data.SQLite;

namespace EmailExtractor.Core;

public static class Storage
{
    private const string DbFile = "emails.db";
    private const string ConnectionString = "Data Source=" + DbFile;

    public static void Init()
    {
        if (!File.Exists(DbFile)) SQLiteConnection.CreateFile(DbFile);
        using var conn = new SQLiteConnection(ConnectionString);
        conn.Open();
        using var cmd = new SQLiteCommand("CREATE TABLE IF NOT EXISTS emails (email TEXT PRIMARY KEY, title TEXT, website TEXT)", conn);
        cmd.ExecuteNonQuery();
    }

    public static void SaveEmail(string email, string title, string website)
    {
        using var conn = new SQLiteConnection(ConnectionString);
        conn.Open();
        using var cmd = new SQLiteCommand("INSERT OR IGNORE INTO emails(email,title,website) VALUES (@e,@t,@w)", conn);
        cmd.Parameters.AddWithValue("@e", email); cmd.Parameters.AddWithValue("@t", title); cmd.Parameters.AddWithValue("@w", website);
        cmd.ExecuteNonQuery();
    }

    public static void ExportCsv(string filename = "emails.csv")
    {
        Init();
        using var conn = new SQLiteConnection(ConnectionString); conn.Open();
        using var cmd = new SQLiteCommand("SELECT email,title,website FROM emails", conn);
        using var reader = cmd.ExecuteReader(); using var sw = new StreamWriter(filename);
        sw.WriteLine("Email,Title,Website");
        while (reader.Read()) sw.WriteLine($"{Csv(reader[0])},{Csv(reader[1])},{Csv(reader[2])}");
    }

    private static string Csv(object value) => "\"" + value.ToString()!.Replace("\"", "\"\"") + "\"";
}
