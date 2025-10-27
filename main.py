import requests
import tkinter as tk
from io import BytesIO
from PIL import ImageTk, Image
#arayüz tasarımı
back_ground_color="#003161"
text_color="#FFF4B7"
window=tk.Tk()
window.geometry('800x600')
window.title('film ve dizi')
window.configure(background=back_ground_color)

baslik=tk.Label(window, text='film ve dizi ara' ,font=('Arial',20,'bold'))
baslik.pack(side=tk.TOP)
baslik.configure(background=back_ground_color,foreground=text_color)

film_adi=tk.Label(window, text='Film adı :',font=('Arial',16,'bold'))
film_adi.place(x=200,y=60)
film_adi.configure(background=back_ground_color,foreground=text_color)

film_entry=tk.Entry(window,font=('Arial',12,'bold'))
film_entry.place(x=300,y=62)

#veri çekme fonksiyonu
def click():
    film=film_entry.get()
    url = f"http://www.omdbapi.com/?apikey=bd83af76&t={film}"
    response = requests.get(url)
    data = response.json()
    film_bilgileri=tk.Label(text=f"Film ismi : {data['Title']}\n"
                            f"Film yılı :{data['Year']}\n"
                            f"Vizyon tarihi : {data['Released']}\n"
                            f"IMDB : {data['imdbRating']}\n",font=('Arial',12,'bold'),foreground=text_color,background=back_ground_color)
    film_bilgileri.place(x=305,y=430)

    #resim ekleme
    poster_url=data['Poster']
    if poster_url and poster_url != "N/A":
        img_data = requests.get(poster_url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((200, 300))
        poster = ImageTk.PhotoImage(img)
        resim = tk.Label(window, image=poster,background=back_ground_color)
        resim.place(x=300, y=100)
        resim.image = poster

#butona tıklandığında fonksiyonu çalıştırma
ara_button=tk.Button(window,text='Ara',command=click,font=('Arial',10,'bold'))
ara_button.place(x=500,y=60)

window.mainloop()

