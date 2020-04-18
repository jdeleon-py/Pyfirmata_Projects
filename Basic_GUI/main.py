from tkinter import *
import gui_interface

if __name__ == "__main__":

	root = Tk()
	root.geometry("300x200")
	root.wm_title('Arduino GUI')
	app = gui_interface.App(root)

	
	root.mainloop()
