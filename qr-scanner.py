import cv2

qr = cv2.QRCodeDetector()

# From Saved Image

# img = cv2.imread("left.jpg")
# val, x, y = qr.detectAndDecode(img)
# print(val)

# directions = ["left", "right", "forward", "backward"]
# for i in range(len(directions)):
# 	img = cv2.imread("qr-" + str(directions[i]) + ".jpg")
# 	val, x, y = qr.detectAndDecode(img)
# 	print("Value Decoded from qr: " + val)




# From Live Video

def scan():
	val = ""
	vid = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Windows only 2nd argument
	print("Opening Camera")
	print("Show the QR Code")
	while(True):
		ret, frame = vid.read()
		# Display the resulting frame
		# cv2.imshow('Live QR Scanner', frame)
		try:
			val, x, y = qr.detectAndDecode(frame)
		except:
			val = "No QR Code"

		if (val != ""):
		    break
		print("Waiting")
		
	vid.release()
	cv2.destroyAllWindows()

	return val


qr_value = scan()
print(qr_value)



