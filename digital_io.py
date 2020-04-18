import pyfirmata2 as py 

class DigitalIO:

	def __init__(self):
		self.port = py.Arduino.AUTODETECT #initialize the port connecting to the board
		self.board = py.Arduino(self.port) #initialize the board with corresponding port

		self.board.samplingOn() #be able to sample analog data (default is 19 ms)

		self.dig_in = self.board.get_pin('d:2:i') #initialize digital pin 2 as an input pin
		self.dig_in.enable_reporting() #allow for values (voltages) to be processed from the input pin
		self.dig_out = self.board.get_pin('d:3:o') #initialize digital pin 3 as an output pin

		self.HIGH = 1
		self.LOW = 0

	def push_interval(self):
		counter = 0 #initialize a counter
		while counter < 100: #counter will loop over 100 times
			if self.dig_in.read() == self.HIGH: #synonymous to digitalRead() in Arduino IDE
				print('Button Pressed!')
				self.dig_out.write(self.HIGH) #synonymous to digitalWrite() in Arduino IDE
			elif self.dig_in.read() == self.LOW:
				print("Button Not Pressed!")
				self.dig_out.write(self.LOW)
			else:
				print("Button has never been pressed!") #present an initial condition

			self.board.pass_time(0.10) #synonymous to delay() in Arduino IDE where (0.10 = 1/10 seconds) 
			counter += 1

		self.dig_out.write(self.LOW)
		return self.board.exit() #once the program is completed, close out the board

test1 = DigitalIO()
test1.push_interval()

