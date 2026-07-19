# Yapay Zeka ve Teknoloji Akademisi - Bootcamp 2026

## Takım Bilgileri
* **Takım İsmi:** Grup-118
* **Dnem/Cohort:** 5. Akademi Dönemi

## Takım Elemanları ve Rolleri
* **Yağmur İNCİ:** Scrum Master (İletişim Sorumlusu)
* **Ayşe Mesrure SARI:** Product Owner (Ürün Sahibi)
* **Ecem ŞİMŞEK:** Developer (Geliştirici)

---

## Ürün Bilgileri
* **Ürün İsmi:** Gezgin
* **Ürün Açıklaması:** Seyehat edilen yerleri kaydedip paylaşabileceğin bir platform.

### Ürün Özellikleri
* Özellik 1 (Örn: Kullanıcı giriş sistemi)
* Özellik 2 (Örn: Yapay zeka tabanlı tahmin motoru)
* Özellik 3 (Örn: Veri görselleştirme paneli)

### Hedef Kitle
* Seyehat etmeyi seven, sevmese de gittiği yerleri düzenli bir şekilde kaydetmek isteyen ve öneriler almak isteyen insanlar

---

## Proje Yönetimi
* **Product Backlog URL:** [https://trello.com/b/6a4aad74933a7dcf66c1bd13/sprint-2](https://trello.com/b/6a4aad74933a7dcf66c1bd13/sprint-2)

---
## Sprint 1
### 1. Backlog Dağıtma Mantığı
Bu sprintte uygulamanın teknik altyapı araştırmalarına ve proje yönetimi iskeletinin kurulmasına öncelik verilmiştir. Görevler, mimari kararların alınabilmesi adına teknoloji ve tasarım araştırmaları etrafında şekillendirilmiş ve ekip üyelerine dağıtılmıştır.

### 2. Sprint Board Updates
Görevlerin güncel durumunu gösteren Sprint 1 tahtamız:

<img width="1067" height="467" alt="image" src="https://github.com/user-attachments/assets/8d4549d8-6543-4356-b5d3-8b1926b74fa7" />

### 3. Ürün Durumu
Bu sprintte, uygulamanın çekirdek mimarisi ve kullanıcı deneyimi konseptleri üzerine yoğunlaşılmıştır. Hangi framework ve teknolojilerin kullanılacağının fizibilite çalışmaları yapılmış; istemci ile sunucu arasındaki veri akış senaryoları planlanmıştır. 

<img width="521" height="305" alt="image" src="https://github.com/user-attachments/assets/9faa165d-6e4a-4630-b033-3987e186ac75" />


## Sprint 2

### 1. Sprint Hedefi ve Backlog Dağıtma Mantığı
Bu sprintte öncelik uygulamanın arka uç (backend) mimarisinin ayağa kaldırılmasına ve veri doğrulama (validation) süreçlerinin kurgulanmasına verilmiştir. Görevler; RESTful API uç noktalarının (endpoint) yazılması, veri modellerinin oluşturulması ve React tabanlı arayüzün bu mimariye entegre edilecek şekilde iskeletinin kurulması etrafında ekibe dağıtılmıştır.

* **Product Backlog URL:** [https://trello.com/b/6a4aad74933a7dcf66c1bd13/sprint-2](https://trello.com/b/6a4aad74933a7dcf66c1bd13/sprint-2)
  
### 2. Daily Scrum Notları
Ekip üyelerimizin asenkron çalışma düzeni nedeniyle iletişim kuralamamış ve Daily Scrum toplantıları yapılamamıştır.

### 3. Sprint Board Updates
Görevlerin güncel durumunu gösteren Sprint 2 tahtası:

<img width="1074" height="501" alt="image" src="https://github.com/user-attachments/assets/4d5b78bd-1862-49ca-91bc-534058ae65e1" />

### 4. Ürün Durumu
Bu sprintte FastAPI kullanılarak gelişmiş bir backend servisi oluşturulmuştur. Pydantic modelleri kullanılarak veri doğrulama işlemleri kurgulanmış; rotaları listeleme, ekleme, güncelleme ve silme (CRUD) operasyonlarını barındıran donanımlı bir mimari kurulmuştur. Hazırlanan bu yapı, Swagger UI üzerinden test edilebilir ve dökümante edilmiş hale getirilmiştir. Frontend tarafında ise React proje iskeleti kurulmuş olup, bileşen (component) geliştirme sürecine başlanmıştır.

<img width="1358" height="825" alt="image" src="https://github.com/user-attachments/assets/b8550662-b3f8-45a1-98c3-c1457d3c8da0" />


### 5. Sprint Review (Sprint Değerlendirmesi)
* **Tamamlanan İşler:** Geliştirme ortamları kuruldu, backend veri akış iskeleti tasarlandı ve ilk API servisleri başarıyla çalıştırıldı.
* **Bekleyen İşler:** Uygulamanın genel görsel konsepti ve renk paleti denemeleri planlanandan uzun sürdüğü için Sprint 3'e aktarılmıştır.
* **Gözden Geçirme:** Arayüz (Frontend) ve arka uç (Backend) entegrasyonu için gerekli veri modelleri (JSON yapıları) netleştirildi.

### 6. Sprint Retrospective (Sprint Retrospektifi)
* **Ne iyi gitti?** Teknolojik altyapı kararları (React & FastAPI) hızlıca alındı ve sunucu taraflı ilk kurulumlar takım içi koordinasyonla sorunsuz tamamlandı.
* **Ne kötü gitti?** Tasarım araştırmaları ve konsept belirleme süreçlerinin efor tahminlemesinde sapmalar yaşandı.
* **Neyi iyileştireceğiz?** Bir sonraki sprint planlamasında tasarım süreçleri gibi soyut görevlere daha geniş zaman ayrılacak ve kodlama ile eşzamanlı yürütülecektir.

