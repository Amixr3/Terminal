import requests

while True:
    number = input("لطفاً عدد NUMBER بین ۱ تا ۱۲۰ باشه. را وارد کنید: ")
    name = input("لطفاً مقدار NAME را وارد کنید: ")

    url = f"http://haji-api.ir/ephoto360?type=text&id={number}&text={name}"
    response = requests.get(url)

    if response.status_code == 200:
        file_path = "/storage/emulated/0/Download/logo.png"
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"لوگو با موفقیت در مسیر {file_path} ذخیره شد.")
    else:
        print("دریافت لوگو با خطا مواجه شد.")

    # بررسی آیا کاربر می‌خواهد ادامه دهد یا خیر
    choice = input("آیا می خواهید ادامه دهید؟ (بله/خیر): ")
    if choice.lower() != "بله":
        break
