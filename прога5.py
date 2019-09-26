from math import *
from tkinter import *

root = Tk()
root.geometry("400x150")

def f_calc(event):
    s = ''
    v_0 = int(ent_c.get())
    g = 9.8
    l = int(ent_l.get())
    h = int(ent_h.get())
    for a in range(1,90):
        if 0<=s*tan(radians(a)) - (g*(s**2))/(2*v_0**2*cos(radians(a))**2) <=h:
            lb_grad["text"]+=str(a)+'  '

lb_c = Label(root); lb_c["text"] = "V0"; ent_c = Entry(root,width=5,bg = "white"); lb_c_r = Label(root); lb_c_r["text"] = "м/c";
lb_c.place(x=15,y=5);lb_c_r.place(x=85,y=5);ent_c.place(x=35,y=5)

lb_l = Label(root); lb_l["text"] = "S"; ent_l = Entry(root,width=5,bg = "white"); lb_l_r = Label(root); lb_l_r["text"] = "м";
lb_l.place(x=15,y=35);lb_l_r.place(x=85,y=35);ent_l.place(x=35,y=35)

lb_h = Label(root); lb_h["text"] = "H"; ent_h = Entry(root,width=5,bg = "white"); lb_h_r = Label(root); lb_h_r["text"] = "м";
lb_h.place(x=15,y=65);lb_h_r.place(x=85,y=65);ent_h.place(x=35,y=65)

lb_n_gr = Label(root, text="A"); lb_n_gr.place(x=15,y=105);
lb_gr= Label(root,width=25,bg = "white"); lb_gr.place(x=35,y=105);
lb_gr_r = Label(root, text="град");lb_gr_r.place(x=195,y=105);


bt_calc = Button(root,text = "Диапазон углов",width=30, height=2)
bt_calc.bind("<Button-1>", f_calc)
bt_calc.place(x=135,y=35)


root.mainloop()
