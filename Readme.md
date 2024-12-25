Proyekte baxmaq isteyen sadece
docker-compose-default.yml faylini endirsin.
Endirdiyi qovluqda
Bu komandani yazsin ise salsın
```
docker compose -f docker-compose-default.yml up -d
```
İşləməsi üçün sadəcə "docker" və "docker compose" olmasi kifayətdir
İnfrastruktur ozu qurulacaq
localhost:8000 ilə baxa bilər

port dəyişmək lazımdirsa docker-compose faylinin icindeən dəyişə bilər

ilkin giriş üçün login parolu da zedelenmelere girib python manage.py create superuser ilə yara da bilər.

sonrasında bütün idarə etmə üeb interfeysi üzərindən olacaq.

databazanın credentialları isə docker compose faylinin icindən təyin edisiniz.

.env fayli istəyə baglı əlavə edilə bilər