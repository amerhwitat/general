# Database and data exchange

The General integration consumes the canonical schema from `amerhwitat/nlp/ThamudicEpiPlatform` and supports:

- SQLite — embedded/default;
- PostgreSQL — server/enterprise deployment;
- MySQL/MariaDB — server deployment;
- JSON — portable flat-file interchange;
- CSV/TSV — spreadsheet and bulk interchange;
- Microsoft Access — optional ODBC bridge through `pyodbc` and a locally installed Access driver;
- application-specific adapters can add DuckDB, Parquet or other stores without changing the provenance contract.

Every import/export should retain source hash, rights/provenance, language/script identifiers, OCR confidence, translation mode, alternatives and review status.

Canonical schema: [nlp repository](https://github.com/amerhwitat/nlp/tree/main/ThamudicEpiPlatform/database).
