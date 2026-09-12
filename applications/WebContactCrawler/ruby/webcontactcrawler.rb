text=File.read(ARGV.fetch(0)); emails=text.scan(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i).map(&:downcase).uniq; puts "DONE unique_emails=#{emails.length}"; puts emails
