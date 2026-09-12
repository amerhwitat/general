<?php
function crawl(array $urls, callable $progressCallback, int $concurrency = 8): array {
    $contacts=[]; $completed=0; $queue=array_values($urls);
    while($queue){ $batch=array_splice($queue,0,$concurrency); $mh=curl_multi_init(); $handles=[];
        foreach($batch as $url){$p=parse_url($url); if(!$p||!in_array(strtolower($p['scheme']??''),['http','https'],true))continue; $ch=curl_init($url); curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_TIMEOUT=>10,CURLOPT_USERAGENT=>'ChimeraEmailExtractor/1.0',CURLOPT_MAXFILESIZE=>5000000]); curl_multi_add_handle($mh,$ch); $handles[]=$ch;}
        do{$status=curl_multi_exec($mh,$running); if($status===CURLM_CALL_MULTI_PERFORM)continue; while($info=curl_multi_info_read($mh)){ $html=curl_multi_getcontent($info['handle']); preg_match_all('/[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/',$html,$m); foreach($m[0]??[] as $e)$contacts[strtolower($e)]=true; $completed++; $progressCallback($completed,count($contacts)); curl_multi_remove_handle($mh,$info['handle']); curl_close($info['handle']); } if($running)curl_multi_select($mh,1.0); }while($running); curl_multi_close($mh);
    } return array_keys($contacts);
}
