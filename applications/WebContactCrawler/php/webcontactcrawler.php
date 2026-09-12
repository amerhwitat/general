<?php
if($argc<2){fwrite(STDERR,"usage: php webcontactcrawler.php <html-file>\n");exit(1);} $s=file_get_contents($argv[1]);preg_match_all('/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i',$s,$m);$out=array_values(array_unique(array_map('strtolower',$m[0])));echo 'DONE unique_emails='.count($out).PHP_EOL;echo implode(PHP_EOL,$out).PHP_EOL;
