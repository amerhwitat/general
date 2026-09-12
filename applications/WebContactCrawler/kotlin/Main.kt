import java.io.File
fun main(a:Array<String>){if(a.isEmpty()){println("usage: WebContactCrawler <html-file>");return};val r=Regex("[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}",RegexOption.IGNORE_CASE);val e=r.findAll(File(a[0]).readText()).map{it.value.lowercase()}.toSortedSet();println("DONE unique_emails=${e.size}");e.forEach(::println)}
