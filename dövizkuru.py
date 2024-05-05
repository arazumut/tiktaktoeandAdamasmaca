import requests
from bs4 import BeautifulSoup
import tkinter as tk

def doviz_kurlari():
    url = "https://www.doviz.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    kurlar = {}
    
    kur_tablosu = soup.find("table", class_="table table-hover table-striped table-financial")
    
    if kur_tablosu:
        kur_satirlari = kur_tablosu.find_all("tr")
        
        for satir in kur_satirlari[1:]:
            hucreler = satir.find_all("td")
            d�viz_adi = hucreler[0].text.strip()
            alis_kuru = hucreler[2].text.strip()
            satis_kuru = hucreler[3].text.strip()
            kurlar[d�viz_adi] = {"Al��": alis_kuru, "Sat��": satis_kuru}
            
    return kurlar

def doviz_kuru_goster():
    d�viz = entry_doviz.get().upper()
    kurlar = doviz_kurlari()
    
    if kurlar:
        if d�viz in kurlar:
            alis_kuru = kurlar[d�viz]["Al��"]
            satis_kuru = kurlar[d�viz]["Sat��"]
            label_sonuc.config(text=f"{d�viz} Al��: {alis_kuru}, Sat��: {satis_kuru}")
        else:
            label_sonuc.config(text=f"{d�viz} d�vizi bulunamad�.")
    else:
        label_sonuc.config(text="D�viz tablosu bulunamad�.")

# Tkinter aray�z� olu�turma
root = tk.Tk()
root.title("D�viz Kuru Sorgulama")

label_doviz = tk.Label(root, text="D�viz Ad�:")
label_doviz.grid(row=0, column=0)

entry_doviz = tk.Entry(root)
entry_doviz.grid(row=0, column=1)

button_sorgula = tk.Button(root, text="Sorgula", command=doviz_kuru_goster)
button_sorgula.grid(row=1, column=0, columnspan=2)

label_sonuc = tk.Label(root, text="")
label_sonuc.grid(row=2, column=0, columnspan=2)

root.mainloop()

