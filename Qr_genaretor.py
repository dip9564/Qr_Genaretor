import qrcode as qr

url = input("Enter URL (or any text): ").strip()

img=qr.make(url)

# choose output file name
file_name = input("Enter file name to save (default: myp.png): ").strip()
if type(file_name)==str:
    file_name += ".png"
else:
    file_name = "my_qr.png"

img.save(file_name)
print("✅ Your QR code Successfully saved as ",file_name)
