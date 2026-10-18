import urllib.request
import urllib.parse
import json

signup_url = "https://api.data.gov/signup/"
# api.data.gov usually accepts user signup JSON
payload = json.dumps({
    "user": {
        "first_name": "Alexia",
        "last_name": "Kamal",
        "email": "alexiachoi22@gmail.com",
        "terms_and_conditions": True
    }
}).encode("utf-8")

req = urllib.request.Request(
    signup_url,
    data=payload,
    headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
)
try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Status:", resp.status)
        data = json.loads(resp.read().decode())
        api_key = data.get("api_key")
        print("Received API Key:", bool(api_key))
        if api_key:
            with open("scripts/usda_key.txt", "w") as f:
                f.write(api_key)
except Exception as e:
    print("Signup error:", e)
