$ErrorActionPreference='Stop'
py -m pip install -e '.[gui,documents,audit]'
py -m pytest -q SEO-Tool/tests
