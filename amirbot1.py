import requests
import os

text = input("متن مورد نظر را وارد کنید: ")

while text != "exit":
    url = "https://haji-api.ir/prompts/?text=" + text
    response = requests.get(url)

    image_path = "/storage/emulated/0/Download/image.jpg"  # مسیر فایل برای ذخیره کردن تصویر
    
    with open(image_path, "wb") as f:
        f.write(response.content)

    print("فایل دانلود شد و در گالری شما ذخیره شد")
    text = input("Enter the text: ")
