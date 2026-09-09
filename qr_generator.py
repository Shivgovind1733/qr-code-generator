import qrcode

data = input("Enter a text or URL to generate QR Code: ").strip()
filename = input("Enter the filename: ").strip()
# Strip gets rid of any white spaces typed by the user.

qr = qrcode.QRCode(box_size=15, border=6)
qr.add_data(data)

image = qr.make_image(fill_color = 'black', back_color = 'white')
image.save(filename)


print(f"QR Code saved as {filename}")