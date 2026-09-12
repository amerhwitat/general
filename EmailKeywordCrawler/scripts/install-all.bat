@echo off
python -m pip install -r EmailKeywordCrawler\python\requirements.txt
if exist EmailKeywordCrawler\typescript\package.json call npm --prefix EmailKeywordCrawler\typescript install
if exist EmailKeywordCrawler\java\pom.xml call mvn -f EmailKeywordCrawler\java\pom.xml dependency:go-offline
if exist EmailKeywordCrawler\go\go.mod call go -C EmailKeywordCrawler\go mod tidy
if exist EmailKeywordCrawler\rust\Cargo.toml call cargo fetch --manifest-path EmailKeywordCrawler\rust\Cargo.toml
