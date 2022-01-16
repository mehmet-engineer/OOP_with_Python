class Çalışanlar():
    personel_list = []        #sınıf niteliği

    def __init__(self, isim):     #oto tetiklenen örnek tanımlaması 
        self.isim = isim
        self.yetenek = []
        self.personel_ekle()

    @classmethod                            
    def personelleri_goster(cls):         #sınıf metodu
        print("Personel Listesi= -----------------------------")
        for kişi in cls.personel_list:
            print(kişi)
    
    def personel_ekle(self):          #örnek metodu 1
        self.personel_list.append(self.isim)       
        print("{} adlı kişi personele eklendi.\n".format(self.isim))
 
    def yetenek_ekle(self, yetenek):      #örnek metodu 2
        self.yetenek.append(yetenek)
        print("\n{} yeteneği {} adlı kişiye eklendi.\n".format(yetenek,self.isim))

    def personel_info(self):          #örnek metodu 3
        print("{} adlı personel bilgisi:".format(self.isim))
        isim_list = self.isim.split()
        print("Adı:", isim_list[0])
        print("Soyadı:", isim_list[1])
        print("Yetenekler:", self.yetenek)

örnek_1 = Çalışanlar("Mehmet KAHRAMAN")
örnek_2 = Çalışanlar("Ahmet KAHRAMAN")
örnek_3 = Çalışanlar("Sinan KAHRAMAN")

örnek_1.yetenek_ekle("Mekatronikçi")
örnek_1.yetenek_ekle("Yazılımcı")
örnek_2.yetenek_ekle("Bilgisayarcı")

örnek_1.personel_info()            #örnek metodu kullanma...

Çalışanlar.personelleri_goster()    #sınıf metodu kullanma...