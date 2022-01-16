import sınıf_modülü

LED = sınıf_modülü.sınıfım()     #örneklendi..
KABLO = sınıf_modülü.sınıfım()
PİL = sınıf_modülü.sınıfım()

LED.ürün = "Rgb 1.2V renkli led"
LED.stok = 50
LED.fiyat = 2

LED.renkler = ["mavi", "kırmızı", "yeşil"]   #özellik eklendi..
a = " ".join(LED.renkler)

print("Renkler:", a)
print(KABLO.renkler)
