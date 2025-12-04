from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import Http404

KARGOLAR = [
    {
        "takip_no": "FK123456789TR",
        "alici": "Esin şener",
        "adres": "İstanbul / Kadıköy",
        "durum": "TESLIM",
        "fiyat": 89.90,
        "olusturma": datetime.now() - timedelta(days=2),
        "guncelleme": datetime.now() - timedelta(hours=5),
        "gecmis": [
            {"tarih": datetime.now() - timedelta(days=2), "konum" : "İstanbul / Kadıköy", "durum": "Kargo alındı"}, 
            {"tarih": datetime.now() - timedelta(days=1), "konum" : "İstanbul / Pendik", "durum": "Kargo yolda"}, 
            {"tarih": datetime.now() - timedelta(hours=5), "konum" : "İstanbul / Kadıköy", "durum": "Kargo teslim edildi"},
        ]},
    {
        "takip_no": "FK987654321TR",
        "alici": "Ayşe demirci",
        "adres": "Ankara / Çankaya",
        "durum": "DAGITIMDA",
        "fiyat": 120.50,
        "olusturma": datetime.now() - timedelta(days=1),
        "guncelleme": datetime.now() - timedelta(hours=1),
    },
    {
        "takip_no": "FK555999777TR",
        "alici": "Mehmet Kurioğlu",
        "adres": "İzmir / Karşıyaka",
        "durum": "YOLDA",
        "fiyat": 75.00,
        "olusturma": datetime.now() - timedelta(days=3),
        "guncelleme": datetime.now() - timedelta(days=1),
    },
]

def cargo_list(request):
    return render(request, "cargo_list.html", {"kargolar": KARGOLAR})


def cargo_info(request, takip_no):
    detay = next((k for k in KARGOLAR if k["takip_no"] == takip_no), None)

    if not detay:
        raise Http404("Kargo bulunamadı.")

    return render(request, "cargo_info.html", {"kargo": detay})

def cargo_create(request):
    return render(request, "cargo_create.html")
