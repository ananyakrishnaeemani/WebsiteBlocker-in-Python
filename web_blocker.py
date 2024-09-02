from tkinter import*
m=Tk()
m.geometry('550x250')
m.resizable(0,0)
m.title("Website Blocker")
a=Label(m,text="Website blocker",font ='arial 20 bold')
a.place(x=160,y=10)
b=Label(m,text='Enter Website:',font ='arial 13 bold')
b.place(x=25,y=70)
Websites=Text(m,font='arail 10',height='2',width='40')
Websites.place(x=160,y=70)

ip="127.0.0.1"
host_path="C:\windows\system32\drivers\etc\hosts"
def msg():
    messagebox.showinfo("Block","SUCCESSFULLY BLOCKED")
def Blocker():
    website_lists=Websites.get(1.0,END)
    Website=list(website_lists.split(","))
    with open (host_path,'r+') as host_file:
        file_content=host_file.read()
        for web in Website:
            if web in file_content:
                Label(m,text="ALREADY BLOCKED",font='arial 12 bold').place(x=230,y=180)
                pass
            else:
                host_file.write('\n'+ip+" "+web)
                Label(m,text="Blocked",font='arial 12 bold').place(x=230,y=180)
block=Button(m,text="BLOCK",font='arial 12 bold',pady=5,command=Blocker,width=6,bg='royal blue1',activebackground='sky blue')
block.place(x=230,y=130)
m.mainloop()