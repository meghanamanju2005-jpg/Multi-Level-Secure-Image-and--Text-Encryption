from PIL import Image

def hide_message(image_path, message, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '11111110'

    data_index = 0

    for y in range(img.height):
        for x in range(img.width):
            if data_index >= len(binary_message):
                break

            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary_message[data_index])
            pixels[x, y] = (r, g, b)
            data_index += 1

        if data_index >= len(binary_message):
            break

    img.save(output_path)


def extract_message(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ""

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            binary_message += str(r & 1)

    message = ""

    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]

        if byte == "11111110":
            break

        if len(byte) < 8:
            break

        message += chr(int(byte, 2))

    return message