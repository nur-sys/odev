class AkilliEv:
    def __init__(self):
        self.isiklar = {}
        self.termostat = {"sicaklik": 22, "mod": "otomatik"}  # Varsayılan 22°C
        self.guvenlik_sistemi = {"durum": "devre dışı"}
        self.cihazlar = {}

    # Işık yönetimi
    def isik_ekle(self, oda):
        self.isiklar[oda] = False
        print(f"{oda} odasına ışık eklendi.")

    def isik_kontrol(self, oda, durum):
        if oda in self.isiklar:
            self.isiklar[oda] = durum
            print(f"{oda} odasındaki ışık {'açıldı' if durum else 'kapandı'}.")
        else:
            print(f"{oda} odasında ışık bulunamadı.")

    # Termostat yönetimi
    def sicaklik_ayarla(self, sicaklik):
        self.termostat["sicaklik"] = sicaklik
        print(f"Termostat {sicaklik}°C'ye ayarlandı.")

    def mod_ayarla(self, mod):
        if mod in ["otomatik", "soğutma", "ısıtma", "kapalı"]:
            self.termostat["mod"] = mod
            print(f"Termostat modu {mod} olarak ayarlandı.")
        else:
            print("Geçersiz mod. 'otomatik', 'soğutma', 'ısıtma' veya 'kapalı' kullanabilirsiniz.")

    # Güvenlik sistemi yönetimi
    def guvenlik_etkinlestir(self):
        self.guvenlik_sistemi["durum"] = "etkin"
        print("Güvenlik sistemi etkinleştirildi.")

    def guvenlik_devre_disibirak(self):
        self.guvenlik_sistemi["durum"] = "devre dışı"
        print("Güvenlik sistemi devre dışı bırakıldı.")

    # Cihaz yönetimi
    def cihaz_ekle(self, ad):
        self.cihazlar[ad] = False
        print(f"{ad} cihazı eklendi.")

    def cihaz_kontrol(self, ad, durum):
        if ad in self.cihazlar:
            self.cihazlar[ad] = durum
            print(f"{ad} {'açıldı' if durum else 'kapandı'}.")
        else:
            print(f"{ad} adlı cihaz bulunamadı.")

    # Sistem durumu gösterimi
    def durum(self):
        print("\n--- Akıllı Ev Durumu ---")
        print("Işıklar:", self.isiklar)
        print("Termostat:", self.termostat)
        print("Güvenlik Sistemi:", self.guvenlik_sistemi["durum"])
        print("Cihazlar:", self.cihazlar)
        print("--------------------------\n")


# Örnek Kullanım
ev = AkilliEv()

# Işık yönetimi
ev.isik_ekle("Oturma Odası")
ev.isik_kontrol("Oturma Odası", True)
ev.isik_kontrol("Yatak Odası", False)

# Termostat yönetimi
ev.sicaklik_ayarla(24)
ev.mod_ayarla("soğutma")

# Güvenlik sistemi yönetimi
ev.guvenlik_etkinlestir()
ev.guvenlik_devre_disibirak()

# Cihaz yönetimi
ev.cihaz_ekle("Çamaşır Makinesi")
ev.cihaz_kontrol("Çamaşır Makinesi", True)

# Sistem durumu gösterimi
ev.durum()
