from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

key = b'12345678'  # 8-byte key

with open("images/secret.png", "rb") as file:
    data = file.read()

cipher = DES.new(key, DES.MODE_ECB)
encrypted_data = cipher.encrypt(pad(data, DES.block_size))

with open("images/encrypted_image.des", "wb") as file:
    file.write(encrypted_data)

return render_template(
    "index.html",
    result=encrypted,
    success="Message hidden successfully and image encrypted successfully!"
)