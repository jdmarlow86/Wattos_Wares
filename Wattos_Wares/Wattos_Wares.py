from tkinter import *
from tkinter import ttk
#from PIL import ImageTk,Image
import sqlconnect

    
root = Tk()
root.title("Watto's Wares")

#canvas = Canvas(root, width = 30, height = 30)  
#canvas.pack()  
#img = ImageTk.PhotoImage(Image.open("Watto.jpg"))  
#canvas.create_image(20, 20, anchor=NW, image=img)

mainframe = ttk.Frame(root, padding="50 50 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
#feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable='See stuff').grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="View Inventory", command=sqlconnect.main).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="View Planets", command=sqlconnect.AllPlanets).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="View Clients", command=sqlconnect.AllClients).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="Exit").grid(column=3, row=6, sticky=W)


ttk.Label(mainframe, text="Query text").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="More query text").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="blah blah").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.bind('<Return>', sqlconnect.main)

root.mainloop()