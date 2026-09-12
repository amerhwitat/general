$ErrorActionPreference='Stop'
py -m pip install -e '.[gui,documents]'
py -m SEO_Tool.gui
