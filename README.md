# AzuraForge: Veritabanı Modelleri

Bu kütüphane, AzuraForge ekosisteminde kullanılan **SQLAlchemy ORM modellerini** merkezi bir yerde barındırır.

## 🎯 Ana Sorumluluklar

*   **Tek Doğruluk Kaynağı (Single Source of Truth):** `Experiment` gibi tüm veritabanı tablolarının nesne tanımlarını içerir. Bu, `api` ve `worker` gibi farklı servislerin aynı veritabanı şeması üzerinde tutarlı bir şekilde çalışmasını sağlar.
*   Kod tekrarını önler ve veritabanı modelinde bir değişiklik yapıldığında, bu değişikliğin tüm bağımlı servislere kolayca yansıtılmasını sağlar.

Gelecekte, veritabanı şema geçişlerini (migrations) yönetmek için **Alembic** yapılandırması da bu repoda yer alacaktır.

---

## 🏛️ Ekosistemdeki Yeri

Bu kütüphane, veritabanına erişim ihtiyacı duyan tüm servisler (`api`, `worker` vb.) tarafından bir bağımlılık olarak kullanılır. Projenin genel mimarisini, vizyonunu ve geliştirme rehberini anlamak için lütfen ana **[AzuraForge Platform Dokümantasyonuna](https://github.com/AzuraForge/platform/tree/main/docs)** başvurun.

---

## 🛠️ Kurulum ve Geliştirme

Bu kütüphane, diğer AzuraForge servisleri tarafından bir bağımlılık olarak kullanılır. Yerel geliştirme ortamı kurulumu için ana platformun **[Geliştirme Rehberi](https://github.com/AzuraForge/platform/blob/main/docs/DEVELOPMENT_GUIDE.md)**'ni takip edin.