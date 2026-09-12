const { contextBridge, ipcRenderer } = require('electron');
contextBridge.exposeInMainWorld('api', {
  fetchPage: url => ipcRenderer.invoke('fetchPage', url),
  extractEmails: html => ipcRenderer.invoke('extractEmails', html),
  extractPageTitle: html => ipcRenderer.invoke('extractPageTitle', html),
  validateEmail: email => ipcRenderer.invoke('validateEmail', email),
  saveEmail: result => ipcRenderer.invoke('saveEmail', result),
  exportCsv: file => ipcRenderer.invoke('exportCsv', file)
});
