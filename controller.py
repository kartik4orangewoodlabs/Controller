# Python Code to test the Game Controller
# Before running this code , make sure you have connected the USB of controller & switched ON the controller 
 
import evdev 
from evdev import InputDevice, categorize, ecodes

devices_list = evdev.list_devices() # This would give us the list of devices 
index = 0

"""
InputDevice gives the device type which has following properties :
1.name
2.capbilities
3.phys


Event has following properties mainly : 
1.Code
2.type 
3.Value



"""



for device in devices_list:
	if evdev.InputDevice(device).name == "Microsoft X-Box 360 pad":
		print("Index where the Controller is found is : " + str(index))
		break
	else:
		index = index + 1

controller =evdev.InputDevice(devices_list[index])
#print(controller.name)

for event in controller.read_loop():
	if event.code != 0:
		#print(categorize(event))
		#print(event)
		
		if event.code == 304:
			if event.value == 1:
				print("A button pressed")
			elif event.value == 0:
				print("A button released")
		if event.code == 305:
			if event.value == 1:
				print("B button pressed")
			elif event.value == 0:
				print("B button released")
		if event.code == 307:
			if event.value == 1:
				print("X button pressed")
			elif event.value == 0:
				print("X button released")
		if event.code == 308:
			if event.value == 1:
				print("Y button pressed")
			elif event.value == 0:
				print("Y button released")

		
