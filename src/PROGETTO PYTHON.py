import cImage as image

#Convertire in toni di grigio una porzione dell’immagine originale,
# facendo scegliere all’utente la porzione mediante due click del mouse
# (corrispondenti ai pixel in alto a sinistra e in basso a destra).

def trasforma_immagine(img,win):
    c= win.captureClicks(2)
    (x1,y1)= c[0]
    (x2,y2)= c[1]
    if x1 > x2 and y2 > y1:
        (x2,y1)= c[0]
        (x1,y2)= c[1]
    elif x2 > x1 and y1 > y2:
        (x1,y2)= c[0]
        (x2,y1)= c[1]
    elif x1 > x2 and y1 > y2:
        (x2,y2)= c[0]
        (x1,y1)= c[1]
    elif x1 == x2 and y1 == y2:
        (x1,y1)= (0,0)
        (x2,y2)= (1,1)

    #(larghezza, altezza)
    new_img= image.EmptyImage(x2-x1, y2-y1)

    for i in range(y1, y2):
        for j in range(x1, x2):
            p= img.getPixel(j,i)
            gscale= (p.getRed() + p.getGreen() + p.getBlue()) //3
            newPixel= image.Pixel(gscale, gscale, gscale)
            new_img.setPixel(j-x1, i-y1, newPixel)
            
    return new_img


def main():
    #Carichiamo e mostriamo l'immagine
    img= image.Image("FOTO1.gif")
    win= image.ImageWin("img", img.getWidth(), img.getHeight())
    #image.ImageWin: crea una cornice, finestra, per visualizzare una o più immagini.
    img.draw(win)
    
    img2= trasforma_immagine(img, win)
    win._close()  #chiude la finestra contenente la foto originale
    win= image.ImageWin("img2", img2.getWidth(), img2.getHeight())
    img2.draw(win)
    
main()
