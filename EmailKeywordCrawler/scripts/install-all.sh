#!/usr/bin/env bash
set -e
python3 -m pip install -r EmailKeywordCrawler/python/requirements.txt
[ -f EmailKeywordCrawler/go/go.mod ] && (cd EmailKeywordCrawler/go && go mod tidy) || true
[ -f EmailKeywordCrawler/rust/Cargo.toml ] && (cd EmailKeywordCrawler/rust && cargo fetch) || true
npm --prefix EmailKeywordCrawler/typescript install || true
mvn -f EmailKeywordCrawler/java/pom.xml dependency:go-offline || true
