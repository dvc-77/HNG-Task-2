from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.postgresql import psycopg2
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv


DATABASE_URL = "postgresql://ohene:ohene12345@postgresql-145522-0.cloudclusters.net:18019/ohene"

# postgresql://username:password@host:port/database_name
engine = create_engine(DATABASE_URL)

SessionManager = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()