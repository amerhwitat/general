<?php
declare(strict_types=1);
function fetchPage(string $url): string { $p=parse_url($url); if(!$p||!in_array(strtolower($p['scheme']??''),['http','https'],true))return ''; $ch=curl_init($url); curl_setopt_array($ch,[CURLOPT_RETURNTRANSFER=>true,CURLOPT_FOLLOWLOCATION=>true,CURLOPT_MAXREDIRS=>5,CURLOPT_TIMEOUT=>10,CURLOPT_USERAGENT=>'ChimeraEmailExtractor/1.0']); $html=curl_exec($ch); curl_close($ch); return is_string($html)?$html:''; }
function extractEmails(string $html): array { preg_match_all("/(?<![\\w.+-])([a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\\.[a-zA-Z0-9-]+)+)(?![\\w.-])/",$html,$m); $out=array_map(fn($e)=>strtolower(trim($e,".,;:<>[](){}\"")),$m[1]??[]); return array_values(array_unique($out)); }
function extractPageTitle(string $html): string { return preg_match('/<title[^>]*>(.*?)<\\/title>/is',$html,$m)?trim(preg_replace('/\\s+/',' ',strip_tags($m[1]))):''; }
function validateEmail(string $email): bool { $parts=explode('@',$email,2); return count($parts)===2 && checkdnsrr(rtrim($parts[1],'.'),'MX'); }
