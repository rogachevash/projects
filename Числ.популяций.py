from tkinter import *


root = Tk()
root.title("Неограниченный рост")
root.geometry("500x500")

n_rost=Label(root,text="Неограниченный рост", bg = "white",width=60); n_rost.place(x=40,y=10)
a=Label(root, text='a',bg='white',width=3);a.place(x=5, y=40)
zn_a=Entry(root,width=5,bg='white', );zn_a.place(x=40, y=40)
kn_rost=Button(root,text='Неограниченный рост', width=25);kn_rost.place(x=80,y=40);kn_rost.bind('<Button-1>')
schot=Label(root,bg='white', width=25);schot.place(x=280,y=40)

og_rost=Label(root, text='Ограниченный рост', bg='white', width=60); og_rost.place(x=40,y=70)
b=Label(root, text='b',bg='white',width=2);b.place(x=5, y=95)
zn_b=Entry(root,width=5,bg='white' );zn_b.place(x=30, y=95)
kn_og=Button(root,text='Ограниченный рост', width=25);kn_og.place(x=80,y=100);kn_og.bind('<Button-1>')
schot_2=Label(root,bg='white', width=5);schot_2.place(x=275,y=95)

otl_rost=Label(root, text='Ограниченный рост с отловом', bg='white', width=60);otl_rost.place(x=40,y=130)
c=Label(root, text='c',bg='white',width=2);c.place(x=5, y=160)
zn_c=Entry(root,width=5,bg='white' );zn_c.place(x=30, y=160)
kn_otl=Button(root,text='Ограниченный рост с отловом', width=25);kn_otl.place(x=80,y=160);kn_otl.bind('<Button-1>')
schot_3=Label(root,bg='white', width=5);schot_3.place(x=275,y=160)

zh_kh=Label(root, text='Жертва-хищник', bg='white', width=60);zh_kh.place(x=40,y=190)
d=Label(root, text='d',bg='white',width=3);d.place(x=5, y=220)
zn_d=Entry(root,width=5,bg='white');zn_d.place(x=40,y=220)
f=Label(root, text='f',bg='white',width=2);f.place(x=80, y=220)
zn_f=Entry(root,width=5,bg='white');zn_f.place(x=115,y=220)
g=Label(root, text='g',bg='white',width=3);g.place(x=155, y=220)
zn_g=Entry(root,width=5,bg='white');zn_g.place(x=190,y=220)
knop_zher=Button(root,text='Жертва-хищник', width=20);knop_zher.place(x=270,y=220);knop_zher.bind('<Button-1>')

zhertv=Label(root, text='Жертвы',bg='white',width=10);zhertv.place(x=65, y=250)
zn_42=Label(root, bg='white',width=3);zn_42.place(x=150, y=250)
khish=Label(root, text='Хищники',bg='white',width=10);khish.place(x=240, y=250)
zn_123=Label(root,bg='white',width=3);zn_123.place(x=325, y=250)

spac=Label(root, text='Жертвы',bg='white',width=10);spac.place(x=2, y=290)
zn_spac=Entry(root,width=5,bg='white');zn_spac.place(x=130,y=290)

byka=Label(root, text='Хищники',bg='white',width=10);byka.place(x=2, y=320)
zn_byka=Entry(root,width=5,bg='white');zn_byka.place(x=130,y=320)

kolvo=Label(root, text='Кол. циклов',bg='white',width=13);kolvo.place(x=2, y=360)
zn_kolv=Entry(root,width=5,bg='white');zn_kolv.place(x=130,y=360)

grafic=Button(root,text='График', width=10);grafic.place(x=60,y=400)

def n_rost(event):
    A=float(zn_a.get())
    N=int(zn_kolv.get())
    gertv=int(zn_spac.get())

    for i in range(N):
        gertv=gertv*A

    schot["text"]=str(int(gertv))

kn_rost.bind("<Button-1>", n_rost)



root.mainloop()
