import requests, time

PHP_URL = "https://yourdomain.com/secret/mybot.php?key=supersecure123"

def fetch_bot_code():
    print("🔄 Fetching latest bot code...")
    r = requests.get(PHP_URL)
    if r.status_code == 200:
        print("✅ Code loaded.")
        return r.text
    else:
        print(f"❌ Fetch error: {r.status_code}")
        return None

def run_bot_forever(refresh_interval=900):  # 15 mins
    while True:
        code = fetch_bot_code()
        if code:
            try:
                exec(code, globals())
            except Exception as e:
                print("❌ Bot crashed:", e)
        else:
            print("⚠️ Skipping run due to fetch error.")
        print(f"⏱ Waiting {refresh_interval} seconds to refresh...")
        time.sleep(refresh_interval)

if __name__ == "__main__":
    run_bot_forever()
