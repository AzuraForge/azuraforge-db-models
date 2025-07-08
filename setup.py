from setuptools import setup, find_packages

setup(
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    # === YENİ SATIRLAR ===
    # Bu ayar, paketin veri dosyalarını içermesini sağlar.
    include_package_data=True,
    # Bu sözlük, hangi paketin hangi veri dosyalarını içereceğini belirtir.
    # Bu, alembic.ini ve alembic/ dizinini pakete dahil edecektir.
    package_data={
        "azuraforge_dbmodels": ["alembic.ini", "alembic/*", "alembic/versions/*"],
    },
    # === BİTTİ ===
)