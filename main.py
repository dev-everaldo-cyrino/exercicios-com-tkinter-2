from tkinter import *
from tkinter import messagebox


        
        
        
        
root = Tk()
root.geometry('500x500+0+0')
root.title('testando as messagebox')


def msgn(ms):
    if ms =='1':
        messagebox.showinfo(title='mensagem de informação',message='informamos que vc colocou o numero 1')
    elif ms =='2':
        messagebox.showwarning(title='mensagem de alerta',message='alertamos que vc colocou o numero 2')
    elif ms =='3':
        messagebox.showerror(title='mensagem de erro',message='erro vc colocou o numero 3')
    elif ms =='4':
        messagebox.askyesno(title='mensagem de pergunta',message='vc colocou o numero 4?')
    elif ms =='5':
        messagebox.askquestion(title='mensagem de pergunta',message='vc colocou o numero 5?')
    elif ms =='6':
        a = messagebox.askokcancel(title='mensagem de confirmar ou cancelar',message='tudo bem fechar a tela?')
        if a == True:
            root.quit
            print('deu certo aqui')
            
            
            
Label(root,text='digite um numero de 1 - 6').pack()
entrada = Entry(root)
entrada.pack()

btn = Button(root,text='testar',command=lambda:msgn(entrada.get()))
btn.pack()

root.mainloop()