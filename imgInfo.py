import tkinter as tk
import tkinter.filedialog as fd
from PIL import ImageTk, Image
import time

class imgInfo():

    fileName = "Ini"
    maxProducts = 9
    coluna = 4
    urlBackground = "background.png"
    urlTopo =  "topo_quarta_padaria.png"
    urlProdutos = [(""),]
    wid_todos = 300
    margin_top = 30

    def __init__(self):
        pass

    def set_fileName(self, x):
        self.fileName = x

    def set_maxPro(self,x):
        self.maxProducts = int(x)
    
    def set_coluna(self,x):
        self.coluna = int(x)

    def set_urlBackground(self,x):
        self.urlBackground = x
        print(self.urlBackground)

    def set_urlProdutos(self,x):
        self.urlProdutos = x

    def set_urlTopo(self,x):
        self.urlTopo = x

    def get_fileName(self):
        return(self.fileName)

    def get_urlBackground(self):
        return(self.urlBackground)
    
    def get_urlProdutos(self):
        return(self.urlProdutos)

    def get_prod(self,x):
        return(self.urlProdutos[x-1])

    def get_urlTopo(self):
        return(self.urlTopo)

    def get_maxProducts(self):
        return(self.maxProducts)

    def get_coluna(self):
        return(self.coluna)

    def get_width(self,x):
        return(self.wid_todos)
    
    def set_width(self,value):
        self.wid_todos = value
    
    def set_marginTop(self,x):
        self.margin_top = x

    def get_marginTop(self):
        return(self.margin_top)

    def createImage(self):

        def infos():
            print("********************************")
            print("arquivo: ",self.fileName)
            print("background: ",self.urlBackground)
            print("topo: ",self.urlTopo)
            print("produtos: ",self.urlProdutos)
            print("********************************")
 

        #url_produto = self.urls
        #infos()
        col = self.get_coluna()
        colunas = col
        work_w = 1000
        work_h = 1250
        
        max_prod = self.get_maxProducts()
        
        linhas = int(max_prod/col)
        rlinhas = max_prod%col

        if(rlinhas): linhas +=1
 
    
        w = self.get_width(col)
        space = int(w/2)
        fix = int(work_w/2)
        margem = 10
        fix_X = fix-((w+margem)*col/2)
        fix_Y = 350
        background_img = Image.open(self.get_urlBackground()).resize((work_w,work_h))

        prod_ini=1
        mTop = self.get_marginTop()

        for y in range(0,linhas):
            if((y==(linhas-1)) and (rlinhas != 0)):
                fix_X += (space+(margem/2))*(colunas-rlinhas)
                colunas = rlinhas
            for x in range(0,colunas):
                p1 = Image.open(self.get_prod(prod_ini)).resize((w,w))
                cord_X = int(fix_X+(x*(w+margem)))
                cord_Y = int(fix_Y+((w+margem)*y))
                background_img.paste(p1,(cord_X,cord_Y+mTop))
                prod_ini += 1
    
        topo = Image.open(self.get_urlTopo()).resize((1000,350))
        background_img.paste(topo,(0,10),topo)
        auxFile = "./"+self.get_fileName()
        background_img.save(auxFile)
        background_img.save("preview.png")
        time.sleep(0.01)


