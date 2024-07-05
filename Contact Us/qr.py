import qrcode

# Replace this with the URL of your hosted HTML file
url = "https://yourusername.github.io/yourrepositoryname"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("qr_code.png")
