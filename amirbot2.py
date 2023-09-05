import requests

while True:
    text = input("لطفا ایدی موردنظر را وارد کنید (برای خروج از برنامه عبارتی مانند 'exit' را وارد کنید): ")
    if text.lower() == "exit":
        break

    url = f"https://api2.haji-api.ir/instainfo/?text={text}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data["ok"]:
        result = data["result"][0]
        print(f"نام کاربری: {result['full_name']}")
        print(f"بیوگرافی: {result['biography']}")
        print(f"لینک اکسترنال: {result['external_url']}")
        print(f"لینک اکسترنال لینکس: {result['external_lynx_url']}")
        print("--------------------------------------")
    else:
        print("خطایی در دریافت اطلاعات رخ داد.")
