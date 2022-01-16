class Deneme():

    def __str__(self):       #print(obje) kullandığımızda...
        return "Bu bir print() fonksiyon uzantısıdır"

    def __len__(self):           #len(obje) fonksiyonunu kullandığımızda...
        print("len() fonksiyonu hacklendi :)")
        return 1 
    
    def __add__(self, other):     # '+' artı operatörünü kullandığımızda bu metot tetiklenecek
        return 10 + other

a0 = Deneme()
print(a0)

a1 = Deneme()
len(a1)

a2 = Deneme()
print(a2 + 100)