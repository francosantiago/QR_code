from cProfile import label
from email.mime import image
from tkinter import Entry, image_names, messagebox, PhotoImage, Frame,Label, Tk, Button, Image, Canvas, Toplevel
import qrcode
from PIL import Image




def mensaje():
   
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("500x300")
    ventana_nueva1.title("IMAGEN A QR")
    ventana_nueva1.iconbitmap("icono.ico")
    ventana_nueva1.resizable(False,False)

    def convertir():
        ruta_imagen = './'
        imagen= qrcode.make(text2)
       
    
   
    text = Entry(ventana_nueva1, bg="gray", width=40)
    text.place(x=175,y=100)
    imagenQR = qrcode.make(text)
    
    text2 = Label(ventana_nueva1, text="ingrese lo que quiere convertir: ", fg="black")
    text2.place(x=20,y=100)


    nombre1 = Label(ventana_nueva1, text="Nombre del QR: "input(""), fg="black").place(x=20,y=150)

    boton = Button(ventana_nueva1, text="    CONVERTIR    ", bg="green", command=convertir).place(x=150,y=200)

    text1 = Entry(ventana_nueva1, bg="gray", width=50). place(x=150,y=150)
    archivo_imagen = open(nombre1, 'wb')
    imagenQR.save(archivo_imagen)
    archivo_imagen.close()


    

  












def destruir():
    messagebox.showinfo(message="NOoOoOoOo te vayas:(:(:(")
    ventana.destroy()


ventana = Tk()
ventana.title("Convertidor a QR")
ventana.resizable(False,False)
ventana.iconbitmap("icono.ico")
ventana.geometry("750x500")
ventana.config(bg="gray")




frame1 = Frame(ventana)
frame1.pack()
frame1.config(bg="pale turquoise",width= 730, height= 480 )
frame1.place(x= 10, y= 10 )
frame1.config(bd=3)
frame1.config(relief="groove")

c = Canvas(frame1, width=720, height=470)
c.place(x=0, y=0)
c.config(bg="pale turquoise", bd=0)

img = PhotoImage(file="puntero.png")
puntero = c.create_image(300,300, image=img,anchor="center")


label3=Label(frame1, text="CONVERTIDOR DE MULTIMEDIA A CODIGO QR", fg="black", font=("Comic Sans MS", 18))
label3.place(x= 90,y= 20)
label3.config(bg="pale turquoise")

label1=Label(frame1, text="TODO TIPO DE MULTIMEDIA", fg="black", font=("Comic Sans MS", 18))
label1.place(x= 180,y= 80)
label1.config(bg="pale turquoise")

label2=Label(frame1, text="-seleccione la opcion que desee: ", fg="black", font=("Arial", 15))
label2.place(x= 50,y= 150)
label2.config(bg="pale turquoise")






bt1=Button(frame1, text="    PNG - JPG   ", command=mensaje)
bt1.place(x=200,y=200)

bt2=Button(frame1, text="       MP3      ", command=mensaje)
bt2.place(x=200,y=270)

bt3=Button(frame1, text="      URL      ", command=mensaje)
bt3.place(x=500,y=200)

bt4=Button(frame1, text="     TEXTO     ", command=mensaje)
bt4.place(x=500,y=270)

bt5=Button(frame1, text="     CERRAR     ", command=destruir)
bt5.place(x=635,y=445)







ventana.mainloop()


