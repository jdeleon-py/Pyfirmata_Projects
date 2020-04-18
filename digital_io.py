import pyfirmata2 as py

class DigitalIO:

	def __init__(self):
	  self.port = py.Arduino.AUTODETECT
		self.board = py.Arduino(self.port)

		self.board.samplingOn()

		self.dig_in = self.board.get_pin('d:2:i')
		self.dig_in.enable_reporting()
		self.dig_out = self.board.get_pin('d:3:o')

		self.HIGH = 1
		self.LOW = 0

	def push_interval(self):
		counter = 0
		while counter < 100:
			if self.dig_in.read() == self.HIGH:
				print('Button Pressed!')
				self.dig_out.write(self.HIGH)
			elif self.dig_in.read() == self.LOW:
				print("Button Not Pressed!")
				self.dig_out.write(self.LOW)
			else:
				print("Button has never been pressed!")

			self.board.pass_time(0.10)
			counter += 1

		self.dig_out.write(self.LOW)
		return self.board.exit()

test1 = DigitalIO()
test1.push_interval()

