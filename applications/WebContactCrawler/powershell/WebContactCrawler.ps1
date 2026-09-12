param([Parameter(Mandatory=$true)][string]$HtmlFile,[string]$Output='emails.txt')
$text=Get-Content -Raw $HtmlFile;$emails=[regex]::Matches($text,'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}','IgnoreCase')|%{$_.Value.ToLower()}|Sort-Object -Unique;$emails|Set-Content -Encoding UTF8 $Output;Write-Host "DONE unique_emails=$($emails.Count) output=$Output"
