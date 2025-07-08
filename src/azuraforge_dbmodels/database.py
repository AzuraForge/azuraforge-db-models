# dbmodels/src/azuraforge_dbmodels/database.py
"""
Bu modül, AzuraForge ekosistemindeki tüm servisler tarafından paylaşılan
SQLAlchemy ORM modellerini ve temel veritabanı yardımcılarını tanımlar.
"""
import os
import uuid
from sqlalchemy import (
    create_engine as sa_create_engine,
    Column,
    String,
    JSON,
    DateTime
)
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """Kullanıcı bilgilerini temsil eden ORM modeli."""
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<User(username='{self.username}')>"

class Experiment(Base):
    """Bir ML deneyinin tüm meta verilerini ve sonuçlarını temsil eden ORM modeli."""
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

    def __repr__(self):
        return f"<Experiment(id='{self.id}', status='{self.status}')>"

def get_session_local(engine):
    """
    Verilen bir SQLAlchemy engine'e bağlı, thread-local olmayan bir 
    SessionLocal fabrikası döndürür.
    """
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)

# init_db fonksiyonu buradan kaldırıldı. Artık Alembic tarafından yönetiliyor.