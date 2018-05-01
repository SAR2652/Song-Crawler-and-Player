from tkinter import *
import webcrawler

root = Tk()
root.geometry('896x504')
searchVar = StringVar(root)
searchsong = ""
songfileText = Text()
def openfile():
	f = open(webcrawler.getSongName(searchsong, False)+'.txt')
	global songfileText
	songfileText.insert('1.0', f)

def leftArrowPress(event = None):
	searchEntry.focus_set()

def rightArrowPress(event = None):
	searchButton.focus_set()

def getSong():
	searchVar = searchEntry.get()
	global searchsong
	searchsong = str(searchVar)
	webcrawler.getSongName(searchsong,True)

searchLabel = Label(root, text = "Name of the song :")
searchEntry = Entry(root, width = 75)
searchIcon = PhotoImage(file = "searchicon.png")
searchButton = Button(root, image = searchIcon, command = getSong)
openButton = Button(text="View Links", command = openfile)
searchEntry.focus_set()
root.bind('<Left>', leftArrowPress)
root.bind('<Right>', rightArrowPress)


searchLabel.grid(row = 0, column = 0, sticky = W)
searchEntry.grid(row = 1, column = 0)
searchButton.grid(row = 1, column = 1)
openButton.grid(row=2,column=0)
songfileText.grid(row=3, column = 0)
root.mainloop()
