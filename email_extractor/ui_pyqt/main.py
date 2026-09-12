import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QProgressBar,QTableWidget,QTableWidgetItem,QPushButton,QVBoxLayout,QWidget,QLineEdit,QHBoxLayout,QFileDialog
from PyQt5.QtCore import QThread,pyqtSignal
from core_py.extractor import fetch_page,extract_emails,extract_page_title,validate_email
from utils.storage import init_db,save_email,export_csv

class Worker(QThread):
    row=pyqtSignal(str,str,str,bool); progress=pyqtSignal(int)
    def __init__(self,urls): super().__init__(); self.urls=urls
    def run(self):
        total=max(1,len(self.urls))
        for i,url in enumerate(self.urls,1):
            try:
                html,final=fetch_page(url); title=extract_page_title(html)
                for email in extract_emails(html):
                    mx=validate_email(email); save_email(email,title,final or url); self.row.emit(email,title,final or url,mx)
            finally: self.progress.emit(i*100//total)

class EmailExtractorUI(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle('Chimera Email Extractor'); self.resize(900,600); init_db()
        self.urls=QLineEdit(); self.urls.setPlaceholderText('URLs, one per line'); self.pages=QProgressBar(); self.contacts=QProgressBar(); self.overall=QProgressBar()
        self.table=QTableWidget(0,5); self.table.setHorizontalHeaderLabels(['Email','Page Title','Website','MX','Status'])
        search=QPushButton('Search Now'); clear=QPushButton('Clear Grid'); save=QPushButton('Save Session'); export=QPushButton('Export CSV')
        search.clicked.connect(self.start); clear.clicked.connect(lambda:self.table.setRowCount(0)); save.clicked.connect(self.save_session); export.clicked.connect(self.export_session)
        buttons=QHBoxLayout(); [buttons.addWidget(b) for b in (search,clear,save,export)]
        box=QVBoxLayout(); [box.addWidget(x) for x in (self.urls,self.pages,self.contacts,self.overall,self.table)]; box.addLayout(buttons)
        w=QWidget(); w.setLayout(box); self.setCentralWidget(w)
    def start(self):
        urls=[u.strip() for u in self.urls.text().splitlines() if u.strip()]
        self.worker=Worker(urls); self.worker.row.connect(self.add_row); self.worker.progress.connect(self.pages.setValue); self.worker.progress.connect(self.overall.setValue); self.worker.start()
    def add_row(self,email,title,url,mx):
        r=self.table.rowCount(); self.table.insertRow(r)
        for c,v in enumerate([email,title,url,'YES' if mx else 'NO','validated' if mx else 'unverified']): self.table.setItem(r,c,QTableWidgetItem(str(v)))
        self.contacts.setValue(min(100,r+1))
    def save_session(self):
        for r in range(self.table.rowCount()): save_email(self.table.item(r,0).text(),self.table.item(r,1).text(),self.table.item(r,2).text())
    def export_session(self):
        filename,_=QFileDialog.getSaveFileName(self,'Export CSV','emails.csv','CSV files (*.csv)')
        if filename: export_csv(filename)

if __name__=='__main__':
    app=QApplication(sys.argv); win=EmailExtractorUI(); win.show(); sys.exit(app.exec_())
