using System.Net; using System.Net.Http; using System.Text.RegularExpressions; using DnsClient; using DnsClient.Protocol;
namespace ChimeraEmailExtractor.Core {
 public record EmailResult(string Email,string PageTitle,string Website,string SourceUrl,bool? ValidMx,string Status);
 public static class Extractor {
  static readonly Regex EmailRegex=new(@"(?<![\w.+-])([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+)(?![\w.-])",RegexOptions.Compiled);
  static readonly HttpClient Client=new(new HttpClientHandler{AutomaticDecompression=DecompressionMethods.All}){Timeout=TimeSpan.FromSeconds(10)};
  public static async Task<(string Html,string FinalUrl)> FetchPage(string url){try{if(!Uri.TryCreate(url,UriKind.Absolute,out var u)||u.Scheme is not("http" or "https"))return("",""); using var r=await Client.GetAsync(u); r.EnsureSuccessStatusCode(); return(await r.Content.ReadAsStringAsync(),r.RequestMessage?.RequestUri?.ToString()??url);}catch{return("","");}}
  public static IEnumerable<string> ExtractEmails(string html)=>EmailRegex.Matches(html).Select(m=>m.Groups[1].Value.Trim(".,;:<>[](){}\"").ToLowerInvariant()).Distinct();
  public static bool ValidateEmail(string email){var p=email.Split('@');if(p.Length!=2)return false;try{return new LookupClient().Query(p[1],QueryType.MX).Answers.Count>0;}catch{return false;}}
 }
}
