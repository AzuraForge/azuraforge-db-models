# dbmodels/src/azuraforge_dbmodels/database.py
import os
from sqlalchemy import create_engine as sa_create_engine, Column, String, JSON, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    def __repr__(self): return f"<User(username='{self.username}')>"

class Experiment(Base):
    __tablename__ = "experiments"
    id = Column(String, primary_key=True, index=True)
    task_id = Column(String, index=True, nullable=False)
    batch_id = Column(String, index=True, nullable=True)
    batch_name = Column(String, nullable=True)
    pipeline_name = Column(String, index=True, nullable=False)
    status = Column(String, index=True, default="PENDING")
    model_path = Column(String, nullable=True)
    config = Column(JSON, nullable=True)
    results = Column(JSON, nullable=True)
    error = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    failed_at = Column(DateTime(timezone=True), nullable=True)
    def __repr__(self): return f"<Experiment(id='{self.id}', status='{self.status}')>"

def get_session_local(engine):
    """Verilen bir engine'e bağlı bir SessionLocal fabrikası döndürür."""
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Veritabanı tablolarını ortam değişkeninden aldığı URL ile oluşturur."""
    # DİKKAT: Artık doğrudan ortam değişkenini okuyoruz.
    # Bu fonksiyon sadece API tarafından çağrılacak ve API'nin ortamı güvenilir.
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("init_db called, but DATABASE_URL environment variable is not set!")
    
    temp_engine = sa_create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=temp_engine)
    temp_engine.dispose()