from django.db import models

DURUM_SECENEKLERI = (
    ('YOLDA', 'Yolda / İşleniyor'),
    ('DAGITIMDA', 'Dağıtımda'),
    ('TESLIM', 'Teslim Edildi'),
    ('IPTAL', 'İptal Edildi'),
)

class Cargo(models.Model):
    takip_no = models.CharField(max_length=50, unique=True, verbose_name="Takip Numarası")
    alici = models.CharField(max_length=100, verbose_name="Alıcı Adı Soyadı")
    adres = models.TextField(verbose_name="Alıcı Adresi")
    durum = models.CharField(max_length=10, choices=DURUM_SECENEKLERI, default='YOLDA', verbose_name="Mevcut Durum")
    fiyat = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Kargo Ücreti (₺)", default=0.00)
    olusturma = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    guncelleme = models.DateTimeField(auto_now=True, verbose_name="Son Güncelleme")

    class Meta:
        verbose_name = "Kargo Gönderisi"
        verbose_name_plural = "Kargo Gönderileri"
        ordering = ['-olusturma']

    def __str__(self):
        return f"{self.takip_no} - {self.alici}"

class CargoHistory(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='gecmis', verbose_name="İlgili Kargo")
    konum = models.CharField(max_length=150, verbose_name="Konum/Şube")
    detay = models.CharField(max_length=255, verbose_name="Durum Detayı")
    tarih = models.DateTimeField(auto_now_add=True, verbose_name="Tarih ve Saat")

    class Meta:
        verbose_name = "Kargo Geçmiş Adımı"
        verbose_name_plural = "Kargo Geçmiş Adımları"
        ordering = ['tarih']

    def __str__(self):
        return f"{self.cargo.takip_no} - {self.konum}"

class Ticket(models.Model):
    DURUM_SECENEKLERI = (
        ('ACIK', 'Açık (Yeni)'),
        ('BEKLEMEDE', 'Yanıt Bekleniyor'),
        ('KAPALI', 'Çözüldü/Kapandı'),
    )
    
    TICKET_KONULARI = (
        ('TESLIMAT', 'Teslimat Sorunu'),
        ('IADE', 'İade/Değişim Talebi'),
        ('DIGER', 'Diğer'),
    )

    konu = models.CharField(max_length=50, choices=TICKET_KONULARI, verbose_name="Ticket Konusu")
    email = models.EmailField(verbose_name="Kullanıcı E-posta")
    mesaj = models.TextField(verbose_name="Mesaj")
    
    durum = models.CharField(max_length=20, choices=DURUM_SECENEKLERI, default='ACIK', verbose_name="Durum")
    
    olusturma = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    guncelleme = models.DateTimeField(auto_now=True, verbose_name="Son Güncelleme")

    class Meta:
        verbose_name = "Destek Bileti (Ticket)"
        verbose_name_plural = "Destek Biletleri (Tickets)"
        ordering = ['durum', '-olusturma']

    def __str__(self):
        return f"[{self.get_durum_display()}] - {self.konu}"