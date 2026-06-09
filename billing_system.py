from tkinter import *








app = Tk()
app.title('Invoice System')
app.geometry('1200x600')

cr=0
Gr=0
def widgets():
    global cr
    global Gr
    ll= Label(app,text= 'Enter the name of item',padx=10,pady=10,font=('calibri',15,'bold'))
    ll.grid(row=cr,column=0)
    en1 = Entry(app,width= 15)
    en1.grid(row=cr,column=1)
    l1 = Label(app,text= 'Enter the no of items',padx=10,pady=10,font=('calibri',15,'bold'))
    l1.grid(row=cr,column=2)
    en = Entry(app,width= 15)
    en.grid(row=cr,column=3)
    l2 = Label(app,text= 'Unit price',padx=10,pady=10,font=('calibri',15,'bold'))
    l2.grid(row=cr,column=4)
    en2 = Entry(app,width= 15)
    en2.grid(row=cr,column=5)
    tl =Label(app,text='Total ',padx=10,pady=10,font=('calibri',15,'bold'))
    tl.grid(row=cr,column=6)
      
    
    def calc():
        global Gr
        num1= en1.get()
        num2 =float(en.get())
        num3= float(en2.get())
        Total = num2*num3
        Gr += Total

        tl.config(text = f'Total = {Total}')
    
    def grand_total():
        global Gr
        gt.config(text=f'Grand Total {Gr}')

    t1 = Button(app,text = 'Total ',width=15,command=calc,padx=10,font=('calibri',15,'bold'))
    t1.grid(row=cr+1,column=5)
    bt1.grid_configure(row=cr+1,column=6)
    gg =Button(app,text = 'Grand Total ',command=grand_total,padx=10,font=('calibri',15,'bold'))
    gg.grid_configure(row=cr+1,column=4)
    gt =Label(app,font= ('calibri',25,'bold'),pady =10,padx=10)
    gt.grid(row=100,column=3,columnspan=5)
    cr+=2



bt1 = Button(app,text='Add more items',command=widgets,width=15,font=('calibri',15,'bold'))

bt1.grid_configure(row=cr+1,column=6)


mainloop()