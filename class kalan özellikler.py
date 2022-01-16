class Deneme():
    def __init__(self):
        self.versiyon = 0.1

    @staticmethod       #normal fonksiyon gibi
    def pi_değeri():    #self gerekmez çünkü onla işi yok
        return 3.14

    @property            #property --> özellik / nitelik yap...       
    def version(self):
        return self.versiyon

örn_1 = Deneme()
print(örn_1.version)     #fonksiyon, self.isim gibi bir nitelikmiş gibi kullanılabiliyor @property sayesinde

print(örn_1.pi_değeri)

print(örn_1.versiyon)    #self.versiyon ifadesini bozmadan "version" adlı nitelikle aynı işi yapmak istiyorsak
print(örn_1.version)     #ya da sonradan "örn_1.versiyon = ahmet" gibi değişim istemiyorsak @property kullanırız.