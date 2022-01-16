class Araçlar():
    tip = "araba"
    model = "sedan"
    ücret = "dolar"

    def bilgileriyaz(self):            #'self' tüm nesneleri temsil eden genel isimdir.
        print(self.tip, "ve", self.model)

    def __init__(self):                #__init__ fonksiyonu her nesne eklendiğinde otomatik olarak çalışır.
        print("Araç objesi oluştu")

honda_civic = Araçlar()
ford_mustang = Araçlar()

honda_civic.bilgileriyaz()