class Araba():
    def __init__(self,marka,model,fiyat):  #nesne eklendiğinde yapılacak ilk işlem tanımlama...
        self.tanımlı_marka = marka
        self.tanımlı_model = model
        self.tanımlı_fiyat = fiyat

    def bilgiler(self):
        print(self.tanımlı_marka, self.tanımlı_model)

    def fiyat_indirimi_yap(self, fiyat_girdisi):
        self.tanımlı_fiyat = fiyat_girdisi

araba_1 = Araba("Tesla", "Model S", 800_000)
araba_1.bilgiler()

araba_1.fiyat_indirimi_yap("500_000 dolar")    #tıpkı metin.replace("a") gibi kendi class'ımız...
print(araba_1.tanımlı_fiyat)

a = "mehmet"
print(dir(a))
print("-------------------------------------------------------")
print(dir(araba_1))      #araba_1 nesnesinin alabileceği metotlar...

