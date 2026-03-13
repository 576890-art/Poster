from PIL import Image, ImageDraw, ImageFont
import qrcode
from termcolor import colored
import random
import os

# ================= Clear screen =================
os.system("clear")

# ================= Banner & Personal Info =================
print(colored("========== ARAFAT DESIGN TOOL ==========", "green"))
print("Developer : Arafat")
print("GitHub    : https://github.com/576890-art")
print("Facebook  : https://www.facebook.com/arafat576890")
print("WhatsApp  : 01989333156")
print("Telegram  : https://t.me/arafat_tech")
print("Email     : arafat342422@gmail.com")
print("========================================\n")

# ================= Menu =================
while True:
    print("""
1  Create Poster / Logo
2  Exit
""")
    choice = input("Select option: ")

    if choice == "1":
        # ================= Input =================
        text1 = input("Enter main title/logo text: ")
        text2 = input("Enter subtitle / your name: ")
        filename = input("Enter filename to save (example: poster.png): ")

        # ================= Image =================
        width = 800
        height = 600
        # Random background color
        bg_color = tuple(random.randint(0,50) for _ in range(3))
        img = Image.new('RGB', (width, height), color=bg_color)
        draw = ImageDraw.Draw(img)

        # ================= Fonts =================
        try:
            title_font = ImageFont.truetype("arial.ttf", 50)
            subtitle_font = ImageFont.truetype("arial.ttf", 30)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

        # ================= Add Text =================
        draw.text((50, 50), text1, fill=(255,255,0), font=title_font)
        draw.text((50, 150), text2, fill=(0,255,255), font=subtitle_font)

        # ================= Emoji =================
        emojis = ["😀","🔥","🚀","💻","🎨"]
        draw.text((50, 250), random.choice(emojis)*5, fill=(255,100,100), font=subtitle_font)

        # ================= QR Code =================
        qr = qrcode.QRCode(version=1, box_size=4, border=2)
        qr.add_data('https://github.com/576890-art')
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color='white', back_color='black')
        img.paste(qr_img, (600, 400))

        # ================= Save =================
        img.save(filename)
        print(colored(f"Poster / Logo saved as {filename}", "green"))

    elif choice == "2":
        print(colored("Goodbye Arafat!", "red"))
        break
    else:
        print(colored("Invalid option", "red"))
