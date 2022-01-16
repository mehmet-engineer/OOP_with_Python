class Mp3Calar():
    def __init__(self, isim):
        self.durum = True
        self.isim = isim
        self.şarkı_list = []
        self.ses_düzeyi = 50
        self.oynatılan = "-"
        
        
    def menu(self):
        print("*** {} - MP3 Çalar ***\nŞarkı Listesi:".format(self.isim), end="")
        print(self.şarkı_list)
        print("Şuanda Çalan:", self.oynatılan)

        print("Ses Düzeyi:", self.ses_düzeyi, end="\n\n")
        
        print("1)Şarkı Seç\n2)Rastgele Seç\n3)Ses Artır\n4)Ses Azalt\n5)Şarkı Ekle\n6)Şarkı Sil\n7)Kapat\n")
        seçim = int(input("Seçiminiz: "))
        if seçim == 1:
            self.şarkı_seç()
        if seçim == 2:
            self.rastgele_seç()
        if seçim == 3:
            self.ses_artır()
        if seçim == 4:
            self.ses_azalt()
        if seçim == 5:
            self.şarkı_ekle()
        if seçim == 6:
            self.şarkı_sil()
        if seçim == 7:
            self.kapat()

    def şarkı_seç(self):
        if len(self.şarkı_list) == 0:
            print("Henüz şarkı eklemediniz.\n")
        else:
            print("Lütfen bir şarkı seçin:--------------------")    
            i = 1
            for a in self.şarkı_list:
                print(i,") ", a ,sep="")
                i = i + 1
            seç = int(input("Seçiminiz: "))
            self.oynatılan = self.şarkı_list[seç-1]

    def rastgele_seç(self):
        if len(self.şarkı_list) == 0:
            print("Henüz şarkı eklemediniz.\n")
        else:
            import random
            seçilen = random.sample(self.şarkı_list,1)
            self.oynatılan = seçilen

    def ses_artır(self):
        self.ses_düzeyi += 10

    def ses_azalt(self):
        self.ses_düzeyi -= 10

    def şarkı_ekle(self):
        şarkı = input("Şarkı ismi girin: ")
        self.şarkı_list.append(şarkı)

    def şarkı_sil(self):
        if len(self.şarkı_list) == 0:
            print("Henüz şarkı eklemediniz.")
        else:
            print("Lütfen bir şarkı seçin:--------------------")    
            i = 1
            for a in self.şarkı_list:
                print(i,") ", a ,sep="")
                i = i + 1
            secim = int(input("Seçiminiz: "))
            del self.şarkı_list[secim-1]
        
    def kapat(self):
        print("Başarıyla kapatıldı.")
        self.durum = False

a1 = Mp3Calar("Mehmet KAHRAMAN")
while a1.durum == True:
    a1.menu()
    print()

        