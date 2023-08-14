## Özellikler

- Alan adları gibi çeşitli IoC türlerinin zenginleştirilmesi.
- VirusTotal, Censys, URLScan gibi çeşitli tehdit istihbarat hizmetleriyle entegrasyon.
- Tarihsel analiz için PostgreSQL veritabanını kullanarak veri depolama ve alımı.
- Gibi çok fazla özellikler mevcuttur.

## Başlangıç

IoC Zenginleştirme API'sını yerel makinenizde kurmak için aşağıdaki adımları izleyin:

1. Docker ve Docker Compose'u sisteminize kurun.
2. Bu depoyu aşağıdaki komutu kullanarak yerel makinenize kopyalayın:

```
git clone https://github.com/Varp0s/ioc_lover.git
```

3. Proje dizinine gidin:

```
cd ioc_lover
```

4. Eğer yerel makinenizde çalıştırmak istiyorsanız, aşağıdaki komutlardan birini kullanın:

```
python3 main.py
uvicorn main:app --reload
```

5. Docker konteynerlerini oluşturup çalıştırın:

```
docker-compose up --build -d
```

6. Konteynerler çalıştığında, API'ye `http://localhost:1453` adresinden erişebilirsiniz.

## API Uç Noktaları

- `GET /`: Sunucunun çalıştığını doğrulamak için basit bir mesaj döndürür.
- `GET /search?ioc_value=<IOC_DEĞERİ>`: Sağlanan IoC değeri için analiz yapar. `<IOC_DEĞERİ>`'ni analiz etmek istediğiniz alan adı ile değiştirin.

## Yapılandırma

API ayarlarını `envs` dizinindeki `.env.template` dosyasını değiştirerek yapılandırabilirsiniz. Bu dosya, API ana bilgisini içerir ve çeşitli tehdit istihbarat hizmetleri için API anahtarlarını içerir.