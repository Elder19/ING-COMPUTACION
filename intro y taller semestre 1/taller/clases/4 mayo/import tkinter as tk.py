import tkinter as tk

# --- functions ---

def on_click(widget):
   
    input("X")
    input("ingresey")
    Y=Y
    X=X
    print('clicked')
    if widget['image'] == str(img2):
        widget['image'] = img3
    else:
        widget['image'] = img2
    w = widget
    print(w)
    
# --- main ---

root = tk.Tk()

img1 = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAACMAAAAjAQMAAAAkFyEaAAAABlBMVEX///8AAABVwtN+AAAAJ0lEQVQI12P4DwQPGCDkAQYGhgRSSDv+BjwkqabZ/2/AQ+LVi+QLAGveQwjt4H11AAAAAElFTkSuQmCC")
img2 = tk.PhotoImage(data="iVBORw0KGgoAAAANSUhEUgAAACMAAAAjAQMAAAAkFyEaAAAABlBMVEUAAADw0gCjrW2CAAAAI0lEQVQI12NgQAL2////byCFPPihHg9JqmkHGOrxkHj1IgEAZH9nDhQLxPMAAAAASUVORK5CYII=")
img3=tk.PhotoImage(file="smile-3.png")
for y in range(Y):
    for x in range(X):
        button = tk.Button(root, image=img1)

        button['command'] = lambda arg=button:on_click(arg)
        
        button.grid(row=y, column=x)
       



root.mainlo
