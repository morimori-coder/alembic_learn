from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker

# 統一されたMetaDataオブジェクトを作成
metadata = MetaData()
Base = declarative_base(metadata=metadata)

# 接続情報を設定
DATABASE_URL = "mssql+pyodbc://sa:saPassword1234@172.22.0.3:1433/alembic-learn?driver=ODBC+Driver+17+for+SQL+Server"

# エンジンを作成
engine = create_engine(DATABASE_URL)

# セッションを作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
