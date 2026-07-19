from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="Gezgin Platformu API",
    description="Kullanıcıların seyahat rotalarını yönettiği gelişmiş backend servisi.",
    version="2.0.0"
)

# --- VERİ MODELLERİ (PYDANTIC) ---
class RotaBase(BaseModel):
    mekan_adi: str = Field(..., title="Mekanın Adı", min_length=2, max_length=100)
    sehir: str = Field(..., title="Bulunduğu Şehir")
    kategori: str = Field(..., title="Mekan Kategorisi", example="Doğa, Tarihi, Cozy")
    puan: float = Field(..., ge=0, le=5, title="Kullanıcı Puanı")

class RotaCreate(RotaBase):
    pass

class RotaResponse(RotaBase):
    id: int
    olusturulma_tarihi: datetime

class RotaUpdate(BaseModel):
    mekan_adi: Optional[str] = None
    sehir: Optional[str] = None
    kategori: Optional[str] = None
    puan: Optional[float] = None

# --- SAHTE VERİTABANI (MOCK DB) ---
# Gerçek bir veritabanı bağlanana kadar verileri hafızada tutuyoruz
fake_db = {
    1: {"id": 1, "mekan_adi": "Moda Sahili", "sehir": "İstanbul", "kategori": "Huzurlu", "puan": 4.8, "olusturulma_tarihi": datetime.now()},
    2: {"id": 2, "mekan_adi": "Kapadokya", "sehir": "Nevşehir", "kategori": "Manzara", "puan": 4.9, "olusturulma_tarihi": datetime.now()}
}
rota_id_sayaci = 3

# --- ENDPOINTLER (CRUD İŞLEMLERİ) ---

@app.get("/", tags=["Sistem"])
def sistem_durumu():
    return {"mesaj": "Gezgin API Sistemleri Aktif", "zaman": datetime.now()}

@app.get("/api/rotalar", response_model=List[RotaResponse], tags=["Rotalar"])
def tum_rotalari_getir():
    """Tüm kayıtlı seyahat rotalarını listeler."""
    return list(fake_db.values())

@app.get("/api/rotalar/{rota_id}", response_model=RotaResponse, tags=["Rotalar"])
def tek_rota_getir(rota_id: int):
    """Spesifik bir rotanın detaylarını getirir."""
    rota = fake_db.get(rota_id)
    if not rota:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Rota bulunamadı.")
    return rota

@app.post("/api/rotalar", response_model=RotaResponse, status_code=status.HTTP_201_CREATED, tags=["Rotalar"])
def yeni_rota_ekle(rota: RotaCreate):
    """Sisteme yeni bir seyahat rotası ekler."""
    global rota_id_sayaci
    yeni_rota = rota.model_dump()
    yeni_rota["id"] = rota_id_sayaci
    yeni_rota["olusturulma_tarihi"] = datetime.now()
    
    fake_db[rota_id_sayaci] = yeni_rota
    rota_id_sayaci += 1
    return yeni_rota

@app.put("/api/rotalar/{rota_id}", response_model=RotaResponse, tags=["Rotalar"])
def rota_guncelle(rota_id: int, guncel_veri: RotaUpdate):
    """Mevcut bir rotanın bilgilerini günceller."""
    rota = fake_db.get(rota_id)
    if not rota:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Güncellenecek rota bulunamadı.")
    
    guncellenecek_alanlar = guncel_veri.model_dump(exclude_unset=True)
    rota.update(guncellenecek_alanlar)
    return rota

@app.delete("/api/rotalar/{rota_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Rotalar"])
def rota_sil(rota_id: int):
    """Bir rotayı sistemden kalıcı olarak siler."""
    if rota_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Silinecek rota bulunamadı.")
    del fake_db[rota_id]