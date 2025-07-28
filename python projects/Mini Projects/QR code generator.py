import qrcode
from PIL import Image  # Ensure Pillow is installed for .show()

upi_id = input("Enter your UPI ID =")

# upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

# Defining the payment url based on the upi id and the payment app

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

# creating QR codes

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# display the qr codes

Image.open("phonepe_qr.png").show()
Image.open("paytm_qr.png").show()
Image.open("google_pay_qr.png").show()
