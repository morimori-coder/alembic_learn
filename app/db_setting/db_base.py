from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData

# 統一されたMetaDataオブジェクトを作成
metadata = MetaData()
Base = declarative_base(metadata=metadata)
