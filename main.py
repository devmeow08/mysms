import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

class Style:
    BRIGHT = '\033[1m'
    SKULL = '\033[0m'

W = '\033[1;37m'  # White
B = '\033[1;30m'  # Black
R = '\033[1;31m'  # Red
GR = '\033[1;32m' # Green
CY = '\033[1;36m' # Cyan

class NGL_BOMBER:
    def __init__(self):
        self.total_requests = 0
        self.success = 0
        self.failed = 0

    def clear(self):
        import os
        os.system('clear' if os.name == 'posix' else 'cls')

    def random_string(self, length: int) -> str:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
        return ''.join(random.choice(chars) for _ in range(length))

    # ✅ NGL API FUNCTION
    def send_ngl_request(self, username: str, message: str):
        try:
            url = "https://ngl.link/api/submit"
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
                "Accept": "*/*",
                "Origin": "https://ngl.link",
                "Referer": f"https://ngl.link/{username}",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest"
            }

            payload = {
                "username": username,
                "question": message,
                "deviceId": self.random_string(32),
                "gameSlug": "",
                "referrer": ""
            }

            response = requests.post(url, data=payload, headers=headers, timeout=15)
            
            if response.status_code == 200:
                return True, response.status_code
            else:
                return False, response.status_code

        except Exception as e:
            return False, None

    def start_bombing(self):
        self.clear()
        banner = [
            f"{CY}",
            "╔╗╔╗ ╔═╗╦ ╦",
            "║║║║ ║ ║║ ║",
            "║║║║ ║ ║║ ║",
            "║║║║ ║ ║║ ║",
            "║╚╝╚╗╚═╝╚═╝",
            "╚═══╝      ",
            f"{GR}       NGL BOMBER TOOL",
            f"{R}   MADE BY: JOHN MICHAEL"
        ]
        for line in banner:
            print(line)

        # ✅ INPUTS BASE SA HININGI MO
        print(f"\n{W}[{CY}+{W}] {GR}SETTINGS{W}")
        target_user = input(f"{W}└─➤ {CY}Enter Username : {GR}")
        target_msg = input(f"{W}└─➤ {CY}Enter Message  : {GR}")
        try:
            bomb_count = int(input(f"{W}└─➤ {CY}Count Bomb     : {GR}"))
        except:
            bomb_count = 50
            print(f"{R}⚠ Invalid input, set to 50 default{W}")

        if not target_user or not target_msg:
            print(f"{R}❌ Username or Message cannot be empty!{W}")
            return

        print(f"\n{CY}========================================={W}")
        print(f"{GR}TARGET  : {W}@{target_user}")
        print(f"{GR}MESSAGE : {W}{target_msg}")
        print(f"{GR}COUNT   : {W}{bomb_count}")
        print(f"{CY}========================================={W}")
        print(f"{R}⚠ STARTING BOMB... PLEASE WAIT...{W}\n")

        self.total_requests = 0
        self.success = 0
        self.failed = 0

        # Gamit ang Threads para mabilis
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.send_ngl_request, target_user, target_msg) for _ in range(bomb_count)]
            
            for future in as_completed(futures):
                self.total_requests += 1
                res, code = future.result()
                
                if res:
                    self.success += 1
                    status = f"{GR}SUCCESS{W}"
                else:
                    self.failed += 1
                    status = f"{R}FAILED{W}"

                print(f"[{self.total_requests:03d}/{bomb_count}] STATUS: {status} | CODE: {code if code else 'ERROR'}")

        # RESULT SUMMARY
        print(f"\n{CY}========================================={W}")
        print(f"{GR}✅ COMPLETED!")
        print(f"{W}TOTAL   : {self.total_requests}")
        print(f"{GR}SUCCESS : {self.success}")
        print(f"{R}FAILED  : {self.failed}")
        print(f"{CY}========================================={W}")

        input(f"\n{W}Press Enter to exit...")

if __name__ == "__main__":
    app = NGL_BOMBER()
    app.start_bombing()
