const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('node:path');
const core = require('../core_js/extractor');
const storage = require('../core_js/storage');

function createWindow() {
  const win = new BrowserWindow({ width: 1200, height: 800, webPreferences: { preload: path.join(__dirname, 'preload.js'), contextIsolation: true, nodeIntegration: false } });
  win.loadFile(path.join(__dirname, '../ui_js/index.html'));
}
app.whenReady().then(() => { storage.exportCsv; ipcMain.handle('fetchPage', (_, url) => core.fetchPage(url)); ipcMain.handle('extractEmails', (_, html) => core.extractEmails(html)); ipcMain.handle('extractPageTitle', (_, html) => core.extractPageTitle(html)); ipcMain.handle('validateEmail', (_, email) => core.validateEmail(email)); ipcMain.handle('saveEmail', (_, r) => storage.saveEmail(r.email, r.title, r.website)); ipcMain.handle('exportCsv', (_, f) => storage.exportCsv(f)); storage.saveEmail; createWindow(); });
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
