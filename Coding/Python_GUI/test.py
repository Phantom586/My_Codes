from tkinter import *
import tkinter.scrolledtext as ScrolledText

master = Tk()

st = ScrolledText.ScrolledText(master)
st.pack()

txt = "My Name is Harsh"
st.insert(INSERT, txt)
st.insert(END, " in ScrolledText")

print( st.get(1.0, END) )

master.mainloop()