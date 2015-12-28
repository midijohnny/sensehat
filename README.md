# sensehat
Raspberry Python SenseHat code
Just some simple programs to play around with Raspberry Pi SenseHat Board.

'kaleidoscope.py'
================

Just draws pretty symmetrical patterns.

'smallhex.py'
=============

Defines small (3x5) pixel characters to display two digit number on the
SenseHat LEDs; to avoid scrolling text.

Hex + Decimal digits defined.


'sensor_client.py'
==================

Publishes SenseHat data (temperature, humidity, pressure) to an 'mqtt' broker.
Allows other clients (by sending a '?' (question-mark) to the appropriate topic)
to recieve the information from the SenseHat.

Other devices can then be used to request and display the information from the SenseHat.

See: https://pypi.python.org/pypi/paho-mqtt for required library.

Needs an 'mqtt' broker: you can install 'mosquitto' on the Pi with:

	sudo apt-get install mosquitto

Note: the broker and the client can be run on different machines or the same machine - it doesn't matter.






