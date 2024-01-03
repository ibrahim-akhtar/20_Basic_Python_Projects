# Project 07
# QR Code Generator

# install libraries "qrcode" and "Image"
# run this command on terminal > pip install qrcode Image (for windows) (for mac change pip to pip3)

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border = 5,
    )

    qr.add_data(text)
    qr.make(fit= True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_image.png")

url = input("Enter your url: ")
generate_qrcode(url)