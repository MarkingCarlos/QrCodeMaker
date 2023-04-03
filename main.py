import qrcode

# texto a ser codificado em QR Code
text = "https://www.linkedin.com/in/carlos-alberto-de-souza-junior-12232223b/"

# gerar QR Code
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)
qr.add_data(text)
qr.make(fit=True)

# criar imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# salvar imagem como arquivo PNG
img.save("C:/Users/carlo/Documents/Codigos/QrCodeReader/Imgs/qrcodeLinkedin.png")
