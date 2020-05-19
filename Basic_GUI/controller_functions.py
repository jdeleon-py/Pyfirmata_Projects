import pyfirmata2 as py

class Controller:

	def __init__(self):
		self.port = py.Arduino.AUTODETECT
		self.board = py.Arduino(self.port)

		self.digital_out = self.board.get_pin('d:2:o')
		self.analog_out = self.board.get_pin('d:3:p')

		self.HIGH = 1
		self.LOW = 0


class DigitalIO(Controller):

	def __init__(self):
		self.controller = Controller()

	def output_high(self):
		return self.controller.digital_out.write(self.controller.HIGH)

	def output_low(self):
		return self.controller.digital_out.write(self.controller.LOW)


class AnalogIO(Controller):

	def __init__(self):
		self.controller = Controller()
		self.controller.board.samplingOn()

	def output_data(self, data):
		return self.controller.analog_out.write(data / 1000)

# GUI is analog input (scrollbar will control the output of an LED)
# Do I have to convert between ADC and a voltage?

# Scrollbar input will have values from 0-1023.
# output PWM operates from 0-255 (input / 4)
