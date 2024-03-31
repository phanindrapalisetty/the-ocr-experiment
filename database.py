#%%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sys

if __name__ == '__main__':
    sys.path.append("..")
    from config.configure import credential
else:
    from config.configure import credential

rdsConfig = credential['dbConfig']
#%%
SQLALCHEMY_DATABASE_URL = f'postgressql://{rdsConfig['user']}:{rdsConfig['password']}@{rdsConfig['host']}:{str(rdsConfig['port'])}/{rdsConfig['database']}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
# %%
