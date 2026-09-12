import csv

def import_emails_txt(path):
    with open(path,encoding='utf-8') as f:return sorted({x.strip().lower() for x in f if x.strip()})

def import_emails_csv(path,column='email'):
    with open(path,newline='',encoding='utf-8') as f:return sorted({r[column].strip().lower() for r in csv.DictReader(f) if r.get(column,'').strip()})

def export_emails_txt(emails,path):
    with open(path,'w',encoding='utf-8') as f:f.write('\n'.join(sorted(set(map(str.lower,emails))))+'\n')

def export_emails_csv(emails,path):
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['email']);w.writerows([[e] for e in sorted(set(map(str.lower,emails)))])
