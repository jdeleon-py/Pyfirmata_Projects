import pyfirmata2 as py

class Controller:

	def __init__(self):
		self.port = py.Arduino.AUTODETECT
		self.board = py.Arduino(self.port)

		self.dig_out = self.board.get_pin('d:2:o')

		self.HIGH = 1
		self.LOW = 0

	def output_high(self):
		return self.dig_out.write(self.HIGH)

	def output_low(self):
		return self.dig_out.write(self.LOW)
