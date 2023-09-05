import requests

while True:
    text = input("متنتون رو وارد کتید:")
    if text.lower() == "finished":
        break
    
    url = f"https://haji-api.ir/Free-GPT3/?text={text}"
    response = requests.get(url)
    data = response.json()
    
    if data["ok"]:
        answer = data["result"]["answer"]
        print(f"Answer: {answer}")
    else:
        print("An error occurred.")
