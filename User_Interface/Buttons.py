import cv2

def checkButtons(printer, sliders):
	command = cv2.waitKey(10) & 0xFF
	if command == ord('q'):
		printer.settings.saveSettings()
		sliders.maskSettings.saveSettings()
		printer.home()
		return True
	elif command == ord('d'):
		enableDots = not enableDots
	elif command == ord('c'):
		printer.settings.xOffset -= 1
	elif command == ord('v'):
		printer.settings.xOffset += 1
	elif command == ord('u'):
		printer.settings.yOffset -= 1
	elif command == ord('i'):
		printer.settings.yOffset += 1
	elif command == ord('s'):
		printer.sendMovement = not printer.sendMovement
	elif command == ord('f'):
		printer.sendSpike = not printer.sendSpike
		print(printer.sendSpike)
	elif command == ord('h'):
		printer.home()
	elif command == ord('g'):
		printer.callibrate()
	elif command == ord('z'):
		printer.raiseZ()
	return False