import tkinter   
pencerem = tkinter.Tk()    #pencerem nesnesini tkinter modülünün Tk() sınıfına örnekle.
pencerem.geometry('300x100')      #Tk() sınıfındaki geometry(self, sınırlar) metodunu kullan.

etiket = tkinter.Label(text='Merhaba, Ben Mehmet KAHRAMAN')   #etiket nesnesi Label sınıfına...
etiket.pack()
düğme = tkinter.Button(text='Tamam', command=pencerem.destroy)
düğme.pack()

pencerem.mainloop()    