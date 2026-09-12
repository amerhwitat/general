@echo off
setlocal
py -m pip install -e ".[gui,documents]"
py -m SEO_Tool.gui
