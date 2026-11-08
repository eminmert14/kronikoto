"""PostgreSQL DDL'ini SQLAlchemy modellerinden üretir:  python -m app.export_schema > ../docs/schema.postgres.sql"""
from sqlalchemy.dialects import postgresql
from sqlalchemy.schema import CreateIndex, CreateTable

from .models import Base

for table in Base.metadata.sorted_tables:
    print(str(CreateTable(table).compile(dialect=postgresql.dialect())).strip() + ";\n")
    for idx in table.indexes:
        print(str(CreateIndex(idx).compile(dialect=postgresql.dialect())).strip() + ";")
    print()
