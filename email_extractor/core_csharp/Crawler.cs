using System.Collections.Concurrent;
using System.Net.Http;
using System.Text.RegularExpressions;

namespace EmailExtractor.Core;
public static class Crawler
{
    private static readonly Regex EmailRegex = new(@"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", RegexOptions.Compiled);
    public static async Task<HashSet<string>> CrawlAsync(IEnumerable<string> urls, Action<int,int>? progress = null, int concurrency = 8, CancellationToken ct = default)
    {
        using var client = new HttpClient(); client.DefaultRequestHeaders.UserAgent.ParseAdd("ChimeraEmailExtractor/1.0");
        var contacts = new ConcurrentDictionary<string, byte>(); int completed = 0;
        using var gate = new SemaphoreSlim(concurrency);
        var tasks = urls.Select(async url => { await gate.WaitAsync(ct); try { if (!Uri.TryCreate(url, UriKind.Absolute, out var u) || (u.Scheme != "http" && u.Scheme != "https")) return; var html = await client.GetStringAsync(u, ct); foreach (Match m in EmailRegex.Matches(html)) contacts.TryAdd(m.Value.ToLowerInvariant(), 0); } catch { } finally { gate.Release(); var n = Interlocked.Increment(ref completed); progress?.Invoke(n, contacts.Count); } });
        await Task.WhenAll(tasks); return contacts.Keys.ToHashSet();
    }
}
