class Çalışan():
    personel = []
    
    def __init__(self, isim):
        self.isim = isim
        self.personele_ekle()
        
    def personele_ekle(self):
        self.personel.append(self.isim)
        print('{} adlı kişi personele eklendi'.format(self.isim))

    @classmethod
    def personeli_görüntüle(cls):
        print('Personel listesi:')
        for kişi in cls.personel:
            print(kişi)

ç1 = Çalışan("Mehmet")
ç1.isim = "Ahmet"        #Kodlarımı hiç bozmadan tek bir değişiklik yapabildim.

Çalışan.personeli_görüntüle()     #ama liste değişmedi. değiştirme fonksiyonu bile yapabilirim (aşağıda)

"""def isim_değiştir(self, yeni_isim):
       kişi = self.personel.index(self.isim)
       self.personel[kişi] = yeni_isim
       self.isim = yeni_isim """    #değişiklik için --> ç1.isim_değiştir("Ahmet")

#sürekli değişiklik gereken ve ortak noktalara sahip olan bir konuda OOP yöntemi kullanılması uygundur.
#ve bir metottaki değişkenin her yerde global kullanılması için self.variable yani bu yöntem gereklidir.
