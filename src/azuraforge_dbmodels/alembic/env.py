# ========== YENİ DOSYA: dbmodels/alembic/env.py ==========
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, create_engine
from sqlalchemy.pool import NullPool

from alembic import context

# Modellerimizin bulunduğu paketi import ediyoruz
from azuraforge_dbmodels import Base

# Alembic Config nesnesi
config = context.config

# .ini dosyasını Python loglaması için yorumla
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Modellerimizin MetaData nesnesini Alembic'e tanıtıyoruz
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Migrations'ı 'offline' modda çalıştırır."""
    url = os.getenv("DATABASE_URL")
    if not url:
        raise ValueError("DATABASE_URL ortam değişkeni 'offline' mod için ayarlanmamış!")
    
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Migrations'ı 'online' modda çalıştırır."""
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL ortam değişkeni 'online' mod için ayarlanmamış!")
        
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()