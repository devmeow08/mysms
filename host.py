import updater
import json
import os

# ------------------- SETTINGS -------------------
# 📂 BABASAHIN NA LANG NATIN ANG FILE NASA LOOB NG FOLDER
CONFIG_FILE = "config.json"
# ------------------------------------------------

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

print("🔍 Checking config...")
try:
    # 📖 BASAHIN ANG FILE NASA LOOB NG CELLPHONE/PC MO
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    print("✅ Config loaded from LOCAL FILE!")

    if config.get("maintenance"):
        print("⚠️ SYSTEM OFFLINE:", config.get("message"))
        exit()

except Exception as e:
    print("❌ DI MAKABASA NG LOCAL CONFIG:", str(e))
    exit()

# INPUT KEY
key = input("\n🔑 Enter your key: ").strip()

# CHECK KUNG TAMA
valid = config.get("valid_keys", {})

if key in valid:
    print("\n✅ HAHAHSHSPOTA")
    print("🚀 Pumasok ka na sa system!")
    print("\n📋 MENU:")
    print("[1] Start Bomb")
    print("[2] Settings")
    print("[3] Exit")

else:
    print("\n❌ MALI O WALA SA LISTAHAN ANG KEY MO!")
