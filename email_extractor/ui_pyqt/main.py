import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QProgressBar,QTableWidget,QTableWidgetItem,QPushButton,QVBoxLayout,QWidget,QLineEdit,QHBoxLayout
from PyQt5.QtCore import QThread,pyqtSignal
from core_py.extractor import fetch_page,extract_emails,extract_page_title,validate_email

class Worker(QThread):
    row=pyqtSignal(str,str,str,bool); progress=pyqtSignal(int)
    def __init__(self,urls): super().__init__(); self.urls=urls
    def run(self):
        total=max(1,len(self.urls))
        for i,url in enumerate(self.urls,1):
            html,final=fetch_page(url); title=extract_page_title(html)
            for email in extract_emails(html): self.row.emit(email,title,final or url,validate_email(email))
            self.progress.emit(i*100//total)

class EmailExtractorUI(QMainWindow):
    def __init__(self):
        super().__init__(); self.setWindowTitle('Chimera Email Extractor'); self.resize(900,600)
        self.urls=QLineEdit(); self.urls.setPlaceholderText('URLs, one per line'); self.pages=QProgressBar(); self.contacts=QProgressBar(); self.overall=QProgressBar()
        self.table=QTableWidget(0,5); self.table.setHorizontalHeaderLabels(['Email','Page Title','Website','MX','Status'])
        search=QPushButton('Search Now'); clear=QPushButton('Clear Grid')
        search.clicked.connect(self.start); clear.clicked.connect(lambda:self.table.setRowCount(0))
        box=QVBoxLayout(); box.addWidget(self.urls); box.addWidget(self.pages); box.addWidget(self.contacts); box.addWidget(self.overall); box.addWidget(self.table); box.addWidget(search); box.addWidget(clear)
        w=QWidget(); w.setLayout(box); self.setCentralWidget(w)
    def start(self):
        urls=[u.strip() for u in self.urls.text().splitlines() if u.strip()]
        self.worker=Worker(urls); self.worker.row.connect(self.add_row); self.worker.progress.connect(self.pages.setValue); self.worker.progress.connect(self.overall.setValue); self.worker.start()
    def add_row(self,email,title,url,mx):
        r=self.table.rowCount(); self.table.insertRow(r)
        for c,v in enumerate([email,title,url,'YES' if mx else 'NO','validated' if mx else 'unverified']): self.table.setItem(r,c,QTableWidgetItem(str(v)))
        self.contacts.setValue(min(100,r+1))

if __name__=='__main__':
    app=QApplication(sys.argv); win=EmailExtractorUI(); win.show(); sys.exit(app.exec_())
