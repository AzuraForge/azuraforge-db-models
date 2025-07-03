import os
from sqlalchemy import create_engine as sa_create_engine, Column, String, JSON, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

# Bu engine, sadece `init_db` için veya tekil scriptlerde kullanılır.
# Servisler kendi engine'lerini kendileri yönetir.
_engine = None
_SessionLocal = None

Base = declarative_base()

class Experiment(Base):
    __tablename__ = "experiments"
    id = Column(String, primary_key=True, index=True)
    task_id = Column(String, index=True, nullable=False)
    batch_id = Column(String, index=True, nullable=True)
    batch_name = Column(String, nullable=True)
    pipeline_name = Column(String, index=True, nullable=False)
    status = Column(String, index=True, default="PENDING")
    config = Column(JSON, nullable=True)
    results = Column(JSON, nullable=True)
    error = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    failed_at = Column(DateTime(timezone=True), nullable=True)

    def __repr__(self):
        return f"<Experiment(id='{self.id}', status='{self.status}')>"

def get_session_local(engine):
    """
    Verilen bir engine'e bağlı bir SessionLocal fabrikası döndürür.
    Bu, her servisin (api, worker) kendi engine'i ile çalışmasını sağlar.
    """
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Veritabanı tablolarını ortam değişkeninden aldığı URL ile oluşturur."""
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL ortam değişkeni ayarlanmamış!")
    
    temp_engine = sa_create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=temp_engine)
    temp_engine.dispose()