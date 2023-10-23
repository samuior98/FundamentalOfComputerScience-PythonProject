# Portion of an image in black and white

---IT---

FONDAMENTI DI INFORMATICA E LABORATORIO - MODULO 1

TRACCIA 1: 
"Convertire in toni di grigio una porzione dell’immagine originale, facendo scegliere all’utente la porzione mediante due click del mouse (corrispondenti ai pixel in alto a sinistra e in basso a destra)."
L’homework è basato sull’utilizzo del modulo “cImage” per applicare trasformazioni ad immagini.

La funzione "trasforma_immagine(img,win)" riceve un'immagine e una finestra.
Per prima cosa ho usato la funzione "win.captureClicks(n)": tale funzione, applicata ad una finestra (cImage.ImageWin), cattura n click del mouse su un’immagine e restituisce la lista delle coordinate dei pixel su cui sono stati effettuati i click.
Il primo elemento della lista mi rappresenta le coordinate del primo click, il secondo elemento le coordinate del secondo click.

Successivamente ho fatto dei controlli per assicurarmi che il primo punto si trovasse in una posizione particolare, diversa dal secondo punto, come da traccia.
Ho creato la nuova immagine, per ogni pixel mi sono preso le componenti RGB e le ho sommate assieme per ottenere l'intensità del pixel.
Ora poichè ogni pixel viene visto come componenti RGB, l'intensità dei pixel la dobbiamo dimezzare per tre e impostare i valori rgb su quel numero.
Non è cambiata l'intensità dei pixel ma il rapporto tra tutti e tre, ora sono tutti uguali e appaiono in scala di grigi.

Dopo aver scelto i due punti, come da traccia, aspettare qualche secondo per avere la foto in toni di grigio.

* Le funzioni getWidth() e getHeight() applicate ad un'immagine (cImage.Image) ne restituiscono larghezza e altezza, rispettivamente.
* La funzione setPixel(j,i,p) applicata ad un'immagine imposta il pixel p sulla riga i e colonna j.
* La funzione getRed() applicata ad un pixel restituisce il valore della componente rosso. I valori sono compresi tra 0 e 255.
* La funzione getGreen() applicata ad un pixel restituisce il valore della componente verde. I valori sono compresi tra 0 e 255.
* La funzione getBlue() applicata ad un pixel restituisce il valore della componente blu. I valori sono compresi tra 0 e 255. 



---ENG---

COMPUTER SCIENCE FUNDAMENTALS AND LABORATORY - MODULE 1

TRACK 1: 
"Convert a portion of the original image to gray tones by having the user choose the portion by two mouse clicks (corresponding to the upper left and lower right pixels)."
The homework is based on using the "cImage" module to apply transformations to images.

The function "transform_image(img,win)" receives an image and a window.
First I used the function "win.captureClicks(n)": this function, applied to a window (cImage.ImageWin), captures n mouse clicks on an image and returns the list of coordinates of the pixels on which the clicks were made.
The first item in the list represents to me the coordinates of the first click, the second item the coordinates of the second click.

Next I did some checking to make sure that the first point was at a particular location, different from the second point, as per the trace.
I created the new image, for each pixel I took the RGB components and added them together to get the intensity of the pixel.
Now since each pixel is seen as RGB components, the pixel intensity we have to halve it by three and set the rgb values to that number.
Not the intensity of the pixels has changed but the ratio of all three, now they are all the same and appear in grayscale.

After choosing the two points, as per the trace, wait a few seconds to get the photo in grayscale.
* The getWidth() and getHeight() functions applied to an image (cImage.Image) return its width and height, respectively.
* The setPixel(j,i,p) function applied to an image sets the pixel p on row i and column j.
* The getRed() function applied to a pixel returns the value of the red component. Values range from 0 to 255.
* The getGreen() function applied to a pixel returns the value of the green component. Values are between 0 and 255.
* The getBlue() function applied to a pixel returns the value of the blue component. Values are between 0 and 255. 



Samuele Iorio - 189706 Computer Engineering
COMPUTER SCIENCE FUNDAMENTALS AND LABORATORY
