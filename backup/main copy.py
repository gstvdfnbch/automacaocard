from tkinter import *
from tkinter import Tk, Text
from tkinter.ttk import Frame, Button, Label, Style
from win32api import GetSystemMetrics
from PIL import ImageTk, Image

class Screen:
    w = int(GetSystemMetrics(0)/3)
    h = int(GetSystemMetrics(1))    

class CreateImage:
    def __init__(self,name,urls,save):
        self.name = name
        self.urls = urls
        self.save = save
        self.max_prod = 10
        self.colunas = 4

    def run(self,ini, max_prod,colunas,topo,margin_top):
        url_produto = self.urls
        col = colunas
        work_w = 1000
        work_h = 1250

        linhas = int(max_prod/col)
        rlinhas = max_prod%col

        print(linhas, rlinhas)

        if(rlinhas): 
            linhas +=1
            print("mais uma linhas")
        
        #               1   2   3   4   5   6 
        wid_todos = [0,300,300,250,215,170,130]
        
        w = wid_todos[col]
        space = int(w/2)
        fix = int(work_w/2)
        margem = 10
        fix_X = fix-((w+margem)*col/2)
        fix_Y = 350
        background_img = Image.open("./background.png").resize((work_w,work_h))

        prod_ini=ini
        for y in range(0,linhas):
            if((y==(linhas-1)) and (rlinhas != 0)):
                fix_X += (space+(margem/2))*(colunas-rlinhas)
                colunas = rlinhas
            for x in range(0,colunas):
                p1 = Image.open("./"+str(prod_ini)+".jpg").resize((w,w))
                cord_X = int(fix_X+(x*(w+margem)))
                cord_Y = int(fix_Y+((w+margem)*y))
                background_img.paste(p1,(cord_X,cord_Y+margin_top))
                prod_ini += 1

        #topo = Image.open("./topo_quarta_padaria.png").resize((1000,350))
        topo = Image.open(topo).resize((1000,350))
        background_img.paste(topo,(0,30),topo)
        background_img.save(str(self.name)+".jpg")

        zoom = 0.5
        #multiple image size by zoom
        pixels_x, pixels_y = tuple([int(zoom * x)  for x in background_img.size])
        img = ImageTk.PhotoImage(background_img.resize((pixels_x, pixels_y))) 

        return(img)


class Layout(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.ini = 3


    def update_preview(self):
        print('update')
        #self.ini +=1
        #url = ['./background.png','./1.png','./1.png','./1.png']
        #img = CreateImage('gus2.png',url,TRUE).run(10,self.ini)
        #self.imgLabel.configure(image=img)
        #self.imgLabel.image = img

    def initUI(self):
                
        self.master.title("automaton")
        self.pack(fill=BOTH, expand=True)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=15)

        self.rowconfigure(0, weight=15)
        self.rowconfigure(1, weight=1)

        self.button_back = Button(self, text="Update", command = self.update_preview)
        self.button_back.grid(row=1, column=0)

        self.button_save = Button(self, text="Save")
        self.button_save.grid(row=1, column=2)
        
        self.url = ['./background.png','./1.png','./1.png','./1.png']
        # 27 = 
        self.img = CreateImage("9_A",self.url,TRUE).run(1,9,3,"./topo_sexta_bebidas.png",10)
        #self.img = CreateImage("24_B",self.url,TRUE).run(13,12,4,"./topo_super_rancho.png",30)
        
        self.imgLabel = Label(self, image=self.img)
        self.imgLabel.image = self.img
        self.imgLabel.grid(row=0,column=0)

        

def main():
    resol = Screen()
    root = Tk()
    root.geometry(str(resol.h)+"x"+str(resol.h-100)+"+0+0")
    layout = Layout()
    root.mainloop()


if __name__ == '__main__':
    main()
