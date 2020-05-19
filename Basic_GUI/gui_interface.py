from tkinter import *
import controller_functions as c

class App:

	def __init__(self, master):
		self.dig_controller = c.DigitalIO()
		self.a_controller = c.AnalogIO()
		
		self.frame = Frame(master)
		self.frame.pack()

		self.var = DoubleVar()

		on_button = Button(self.frame, text = "ON", command = self.dig_controller.output_high)
		off_button = Button(self.frame, text = "OFF", command = self.dig_controller.output_low)
		analog_scale = Scale(self.frame, variable = self.var, from_ = 0, to = 100, length = 600, 
								tickinterval = 10, orient=HORIZONTAL, command = self.scale_output)

		on_button.grid(row = 1, columnspan = 2)
		off_button.grid(row = 2, columnspan = 2)
		analog_scale.grid(row = 3, columnspan = 2)

	def scale_output(self, value = None):
		raw = float(self.var.get())
		return self.a_controller.output_data(raw)
