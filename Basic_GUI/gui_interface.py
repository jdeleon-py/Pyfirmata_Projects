from tkinter import *
import controller_functions as c

class App:

	def __init__(self, master):
		self.controller = c.Controller()
		
		self.frame = Frame(master)
		self.frame.pack()

		on_button = Button(self.frame, text = "ON", command = self.controller.output_high)
		off_button = Button(self.frame, text = "OFF", command = self.controller.output_low)

		on_button.grid(row = 1, columnspan = 2)
		off_button.grid(row = 2, columnspan = 2)
