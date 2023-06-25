import requests
#create your account on cuttly and genrate your api_key
api_key = "Your Key"
url = input()
api_url = f"https://cutt.ly/api/api.php?key={api_key}&short={url}"
data = requests.get(api_url).json()["url"]
if data["status"] == 7:
    shortened_url = data["shortLink"]
    print("Shortened URL:", shortened_url)
else:
    print("[!] Error Shortening URL:", data)