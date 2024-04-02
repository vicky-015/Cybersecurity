!pip install pillow
import base64
from PIL import Image, ImageFont, ImageDraw

# Load the GIF image
img = Image.open('reallyreadme.gif')

# Define the message and its position
message = "Hello, World!"
x, y = 10, 10

# Define the font and text color
font = ImageFont.load_default()
color = (0, 0, 0)

# Check if the message is encoded or not
if message.isascii():
    # Get the encoded message
    message_bytes = message.encode()
    encoded_message = base64.b64encode(message_bytes)
    message = encoded_message.decode()
    # Draw the encoded message on the image
    encoded_message_x, encoded_message_y = x, y + 30
    d = ImageDraw.Draw(img)
    d.text((encoded_message_x, encoded_message_y), message, font=font, fill=color)
    # Save the encoded image
    img.save('encoded_image.png')

else:
    # Decode the encoded message
    encoded_message = img.crop((x, y + 30, x + 100, y + 50))
    message_bytes = base64.b64decode(encoded_message.tobytes().decode())
    message = message_bytes.decode()
    # Draw the decoded message on the image
    x, y = 10, 10
    d = ImageDraw.Draw(img)
    d.text((x, y), message, font=font, fill=color)
    # Save the decoded image
    img.save('decoded_image.png')
