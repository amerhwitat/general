#!/usr/bin/env python3
"""Local WebContactCrawler GUI/API server."""
from __future__ import annotations
import json,mimetypes,threading,time,uuid
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from webcontactcrawler import Crawler,export,import_csv,import_txt
ROOT=Path(__file__).resolve().parents[1]/"web";MAX_BODY=2*1024*1024;JOBS={};LOCK=threading.RLock()
def _json(handler,status,payload):
    raw=json.dumps(payload,ensure_ascii=False).encode();handler.send_response(status);handler.send_header("Content-Type","application/json; charset=utf-8");handler.send_header("Content-Length",str(len(raw)));handler.end_headers();handler.wfile.write(raw)
def _body(handler):
    length=int(handler.headers.get("Content-Length","0"))
    if length<=0 or length>MAX_BODY:raise ValueError("request body is empty or too large")
    data=json.loads(handler.rfile.read(length).decode());
    if not isinstance(data,dict):raise ValueError("JSON body must be an object")
    return data
def _safe_url(value):
    p=urlparse(value.strip())
    if p.scheme not in {"http","https"} or not p.hostname or p.username or p.password:raise ValueError("url must be a public http:// or https:// URL")
    return value.strip()
def _job_snapshot(job):
    last={};event_file=Path(job["events"])
    if event_file.exists():
        try:
            lines=event_file.read_text(encoding="utf-8").splitlines()
            if lines:last=json.loads(lines[-1])
        except (OSError,ValueError):pass
    return {"id":job["id"],"state":job["state"],"created":job["created"],"started":job.get("started"),"finished":job.get("finished"),"output":job["output"],"events":job["events"],"error":job.get("error"),"progress":last}
def _events(job,after=0):
    path=Path(job["events"])
    if not path.exists():return []
    try:lines=path.read_text(encoding="utf-8").splitlines()[max(0,int(after)):];return [json.loads(x) for x in lines[-1000:]]
    except (OSError,ValueError):return []
def _run_job(job_id,cfg):
    with LOCK:job=JOBS[job_id];job["state"]="running";job["started"]=time.time()
    try:
        events=Path(cfg["events"]);events.parent.mkdir(parents=True,exist_ok=True);crawler=Crawler([cfg["url"]],cfg["keywords"],cfg["max_pages"],cfg["max_depth"],cfg["delay"],cfg["timeout"],cfg["max_bytes"],event_file=events,stop_event=job["stop_event"]);rows=crawler.run();output=Path(cfg["output"]);output.parent.mkdir(parents=True,exist_ok=True);export(rows,output)
        with LOCK:job["state"]="cancelled" if job["stop_event"].is_set() else "done";job["result"]={"pages":crawler.pages,"emails":len(rows),"output":str(output)}
    except Exception as exc:
        with LOCK:job["state"]="error";job["error"]=str(exc)
    finally:
        with LOCK:job["finished"]=time.time()
class Handler(BaseHTTPRequestHandler):
    server_version="WebContactCrawlerGUI/1.2"
    def log_message(self,fmt,*args):print("GUI "+(fmt%args),flush=True)
    def do_GET(self):
        path=urlparse(self.path).path
        if path=="/api/jobs":
            with LOCK:return _json(self,200,{"jobs":[_job_snapshot(j) for j in JOBS.values()]})
        if path.startswith("/api/jobs/"):
            parts=path.split("/");job_id=parts[3] if len(parts)>3 else ""
            with LOCK:job=JOBS.get(job_id)
            if not job:return _json(self,404,{"error":"job not found"})
            if len(parts)>4 and parts[4]=="events":
                try:after=int(self.headers.get("X-Event-Offset","0"))
                except ValueError:after=0
                return _json(self,200,{"events":_events(job,after),"offset":after})
            return _json(self,200,_job_snapshot(job))
        rel="index.html" if path in {"","/"} else path.lstrip("/");target=(ROOT/rel).resolve()
        if ROOT not in target.parents and target!=ROOT:return _json(self,403,{"error":"forbidden"})
        if not target.is_file():return _json(self,404,{"error":"not found"})
        data=target.read_bytes();self.send_response(200);self.send_header("Content-Type",mimetypes.guess_type(str(target))[0] or "application/octet-stream");self.send_header("Content-Length",str(len(data)));self.end_headers();self.wfile.write(data)
    def do_POST(self):
        path=urlparse(self.path).path
        try:
            data=_body(self)
            if path=="/api/scan":
                url=_safe_url(str(data.get("url","")));output=Path(str(data.get("output","emails.csv")).strip() or "emails.csv").expanduser()
                if output.is_dir():output=output/"emails.csv"
                if output.suffix.lower() not in {".csv",".txt"}:raise ValueError("output must end in .csv or .txt")
                job_id=uuid.uuid4().hex[:12];events=output.parent/(output.stem+".events.jsonl");cfg={"url":url,"output":str(output),"events":str(events),"keywords":[str(x) for x in data.get("keywords",[]) if str(x).strip()],"max_pages":max(1,min(int(data.get("max_pages",100)),100000)),"max_depth":max(0,min(int(data.get("max_depth",3)),32)),"delay":max(0.0,float(data.get("delay",0.5))),"timeout":max(1.0,min(float(data.get("timeout",10)),120)),"max_bytes":max(1024,min(int(data.get("max_bytes",2000000)),50000000))};job={"id":job_id,"state":"queued","created":time.time(),"output":str(output),"events":str(events),"stop_event":threading.Event()}
                with LOCK:JOBS[job_id]=job
                threading.Thread(target=_run_job,args=(job_id,cfg),daemon=True).start();return _json(self,202,_job_snapshot(job))
            if path.startswith("/api/jobs/") and path.endswith("/cancel"):
                job_id=path.split("/")[3]
                with LOCK:
                    job=JOBS.get(job_id)
                    if not job:return _json(self,404,{"error":"job not found"})
                    job["stop_event"].set()
                    if job["state"]=="queued":job["state"]="cancelled"
                return _json(self,200,_job_snapshot(job))
            if path=="/api/import":
                name=str(data.get("name","import.txt")).lower();text=str(data.get("content",""));tmp=Path.cwd()/f".webcontactcrawler-import-{uuid.uuid4().hex}";tmp.write_text(text,encoding="utf-8")
                try:emails=import_csv(tmp) if name.endswith(".csv") else import_txt(tmp)
                finally:tmp.unlink(missing_ok=True)
                return _json(self,200,{"emails":emails,"count":len(emails)})
            return _json(self,404,{"error":"unknown endpoint"})
        except (ValueError,TypeError,json.JSONDecodeError) as exc:return _json(self,400,{"error":str(exc)})
def main(host="127.0.0.1",port=5088):
    httpd=ThreadingHTTPServer((host,port),Handler);print(f"WebContactCrawler GUI: http://{host}:{port}",flush=True)
    try:httpd.serve_forever()
    except KeyboardInterrupt:pass
    finally:httpd.server_close()
if __name__=="__main__":main()
