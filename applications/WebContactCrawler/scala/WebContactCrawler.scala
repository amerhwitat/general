import scala.io.Source
object WebContactCrawler extends App { val s=Source.fromFile(args(0)).mkString; val r="(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,}".r; val e=r.findAllIn(s).map(_.toLowerCase).toSet.toSeq.sorted; println(s"DONE unique_emails=${e.size}"); e.foreach(println) }
