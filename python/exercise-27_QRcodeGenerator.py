import qrcode

qr = qrcode.QRCode(
    version =1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)
print("-----------------QR CODE GENERATOR-----------------")
print()
data = input("Enter the data to code: ")
print("---------------------------------------------------")
filename = input("Enter the filename to save the QR code: ")
print("---------------------------------------------------")

qr.add_data(data)
img = qr.make_image()
img.save(filename)

