#Parent
class Hayvanlar():    
    def __init__(self):
        print("Örnek Hayvan oluşturuldu")

    def hayvan_özellikleri(self):
        print("hayvanların duyuları vardır")

#Child
class Köpekler(Hayvanlar):     #Hayvanlar sınıfından kalıtımı aktifleştir.
    def __init__(self):
        super().__init__(self)     #super()._init_(ana sınıfın parametreleri) ile hayvanlar sınıfının _init_ tanımlarını kullan.
        print("Örnek Köpek oluşturuldu")


örn_1 = Köpekler()
print()
örn_1.hayvan_özellikleri()     #Hayvanlar sınıfından metodu başka sınıfta kullanma