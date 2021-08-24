import qrcode

directions = ["left", "right", "forward", "backward"]

for i in range(len(directions)):
	print("Generating qr code for: " + directions[i])
	img = qrcode.make(directions[i])
	img.save("qr-" + str(directions[i]) + ".jpg")



