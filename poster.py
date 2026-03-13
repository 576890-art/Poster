import os
import random
from pyfiglet import Figlet
from termcolor import colored
from PIL import Image, ImageDraw, ImageFont
import qrcode

# ===== Clear terminal =====
os.system("clear")

# ===== Big Name Banner =====
try:
    banner = Figlet(font="slant")
    print(colored(banner.renderText("ARAFAT"), "green"))
except:
    print(colored("ARAFAT", "green"))

# ===== Personal Info =====
personal_info = {
    "Developer": "Arafat",
    "GitHub": "https://github.com/576890-art",
    "Facebook": "https://www.facebook.com/arafat576890",
    "WhatsApp": "01989333156",
    "Telegram": "https://t.me/arafat_tech",
    "Email": "arafat342422@gmail.com"
}

for key, value in personal_info.items():
    print(colored(f"{key:<10}: {value}", "cyan"))

print(colored("="*50, "green"))

# ===== Tool Menu =====
def create_poster():
    text_main = input(colored("Enter Main Title / Logo Text: ", "yellow"))
    text_sub = input(colored("Enter Subtitle / Your Name: ", "yellow"))
    filename = input(colored("Enter filename to save (example: poster.png): ", "yellow"))

    width, height = 800, 600
    bg_color = tuple(random.randint(0, 50) for _ in range(3))
    img = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    try:
        title_font = ImageFont.truetype("arial.ttf", 50)
        sub_font = ImageFont.truetype("arial.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        sub_font = ImageFont.load_default()

    draw.text((50, 50), text_main, fill=(255, 255, 0), font=title_font)
    draw.text((50, 150), text_sub, fill=(0, 255, 255), font=sub_font)

    emojis = ["😀", "🔥", "🚀", "💻", "🎨"]
    draw.text((50, 250), "".join(random.choices(emojis, k=5)), fill=(255, 100, 100), font=sub_font)

    # QR Code
    qr = qrcode.QRCode(version=1, box_size=4, border=2)
    qr.add_data(personal_info["GitHub"])
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="white", back_color="black").convert("RGB")
    img.paste(qr_img, (600, 400))

    img.save(filename)
    print(colored(f"Poster/Logo saved as {filename}", "green"))

while True:
    print(colored("""
1  Create Poster / Logo
2  Exit
""", "yellow"))

    option = input(colored("Select Option: ", "magenta"))

    if option == "1":
        create_poster()
    elif option == "2":
        print(colored("Goodbye Arafat!", "red"))
        break
    else:
        print(colored("Invalid Option", "red"))
