# Pyfirmata_Projects
This repository will catalog my creations with the Pyfirmata2 library in conjunction with an Arduino microcontroller.

As of Apr.17, 2020, the most recent version of Pyfirmata is version 2.0.1.
This library and version of Pyfirmata can be installed with the command 

pip install pyfirmata2==2.0.1

In order to upload sketches into the Arduino microcontroller, the StandardFirmata sketch must be uploaded to the Arduino microcontroller using the Arduino IDE.

File -> Examples -> Firmata -> StandardFirmata -> Upload
(choose the correct board and port when uploading the StandardFirmata sketch)

Once the StandardFirmata sketch has been uploaded to the microcontroller, python scripts using the imported 'pyfirmata2' library can be written and uploaded without anymore need of the Arduino IDE, since the StandardFirmata sketch is already preloaded on the controller.

In my case, I am writing Python scripts in Sublime Text and running them via the command line of a Mac terminal.
