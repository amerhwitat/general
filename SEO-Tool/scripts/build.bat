@echo off
setlocal
py -m pip install -e ".[gui,documents,audit]"
py -m pytest -q SEO-Tool/tests
