try:
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore, Style
    import json
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")

# Hàm đếm ngược với giao diện đẹp hơn
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
            f"{Fore.CYAN}OFFTO {Fore.YELLOW}OL 🍉 {Fore.GREEN}VIP Tool{Style.RESET_ALL}",
            f"{Fore.MAGENTA}OFFTO {Fore.CYAN}OL 🍉 {Fore.GREEN}VIP Tool{Style.RESET_ALL}",
            f"{Fore.YELLOW}OFFTO {Fore.BLUE}OL 🍉 {Fore.GREEN}VIP Tool{Style.RESET_ALL}",
        ]
        for color in colors:
            print(f"\r{color} | Đếm ngược: {Fore.YELLOW}{remaining_time}s{Style.RESET_ALL}", end="")
            time.sleep(0.12)
    print(f"\r{Fore.GREEN}Đang xử lý công việc...{Style.RESET_ALL}", end="\r")
    time.sleep(1)
    print("\r" + " " * 50 + "\r", end="")  # Xóa dòng cũ

# Hàm hiển thị banner chuyên nghiệp
def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║       SCODE Golike Linkedin v1.0       ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Created by: NGUYỄN VĂN ĐẠT         ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚════════════════════════════════════╝{Style.RESET_ALL}")
    print()

# Hàm hiển thị danh sách tài khoản LinkedIn
def LINKEDIN():
    checkaccount = requests.get('https://gateway.golike.net/api/linkedin-account', headers=headers).json()
    user_linkedin1 = []
    account_id1 = []
    i = 1

    banner()
    print(f"{Fore.YELLOW}📋 DANH SÁCH TÀI KHOẢN LINKEDIN{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
    for data in checkaccount['data']:
        usernametk = data['name']
        user_linkedin1.append(usernametk)
        account_id1.append(data['id'])
        print(f"{Fore.GREEN}[{i}] {Fore.WHITE}Tài khoản: {Fore.YELLOW}{usernametk} {Fore.GREEN}- Trạng thái: {Fore.GREEN}Hoạt động{Style.RESET_ALL}")
        i += 1
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")

    # Chọn tài khoản
    choose = int(input(f"{Fore.YELLOW}➤ Nhập số thứ tự tài khoản (1-{len(user_linkedin1)}): {Style.RESET_ALL}"))
    os.system('cls' if os.name == 'nt' else 'clear')
    if 1 <= choose <= len(user_linkedin1):
        user_tiktok = user_linkedin1[choose - 1]
        account_id = account_id1[choose - 1]
        
        # Kiểm tra và nhập cookie
        checkfile = os.path.isfile(f'COOKIELINKEDIN{account_id}.txt')
        if not checkfile:
            banner()
            COOKIELINK = input(f"{Fore.GREEN}🔑 Nhập Cookie LinkedIn cho {user_tiktok}: {Style.RESET_ALL}")
            with open(f'COOKIELINKEDIN{account_id}.txt', 'w') as f:
                f.write(COOKIELINK)
        else:
            with open(f'COOKIELINKEDIN{account_id}.txt', 'r') as f:
                COOKIELINK = f.read()

        # Nhập số lượng job và delay
        banner()
        print(f"{Fore.YELLOW}🔧 CÀI ĐẶT CÔNG VIỆC{Style.RESET_ALL}")
        choose = int(input(f"{Fore.GREEN}📌 Số lượng job cần thực hiện: {Style.RESET_ALL}"))
        DELAY = int(input(f"{Fore.GREEN}⏱ Thời gian delay (giây): {Style.RESET_ALL}"))
        
        # Thực hiện công việc
        print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🚀 BẮT ĐẦU THỰC HIỆN CÔNG VIỆC{Style.RESET_ALL}")
        dem = 0
        tong = 0
        for i in range(choose):
            url2 = f'https://gateway.golike.net/api/advertising/publishers/linkedin/jobs?account_id={account_id}&data=null'
            checkurl2 = ses.get(url2, headers=headers).json()
            if checkurl2['status'] == 200:
                ads_id = checkurl2['data']['id']
                object_id = checkurl2['data']['object_id']
                type = checkurl2['data']['type']
                countdown(DELAY)
                
                if type == 'follow':
                    headers_follow = {
                        'accept': 'application/vnd.linkedin.normalized+json+2.1',
                        'cookie': COOKIELINK,
                        'csrf-token': COOKIELINK.split('JSESSIONID="')[1].split('"')[0],
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                    }
                    response = requests.get(checkurl2['data']['link'], headers=headers_follow).text
                    json_data2 = {'account_id': account_id, 'ads_id': ads_id}
                    url_complete = 'https://gateway.golike.net/api/advertising/publishers/linkedin/complete-jobs'
                    check = requests.post(url_complete, headers=headers, json=json_data2).json()

                    if check['success']:
                        dem += 1
                        prices = check['data']['prices']
                        tong += prices
                        local_time = time.localtime()
                        timestamp = f"{local_time.tm_hour:02d}:{local_time.tm_min:02d}:{local_time.tm_sec:02d}"
                        print(f"{Fore.GREEN}[{dem}] {Fore.YELLOW}{timestamp} {Fore.GREEN}✔ Thành công | {Fore.CYAN}Follow | {Fore.WHITE}Ẩn ID | {Fore.GREEN}+{prices} | Tổng: {Fore.YELLOW}{tong} VNĐ{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}✖ Thất bại - Bỏ qua job{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🏁 HOÀN THÀNH: {dem} job thành công | Tổng tiền: {tong} VNĐ{Style.RESET_ALL}")

# Hàm hiển thị menu chính
def LIST():
    print(f"{Fore.YELLOW}📋 MENU CHÍNH{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] Chạy tool LinkedIn{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[2] Xóa Authorization hiện tại{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")

# Cấu hình headers (giữ nguyên)
ses = requests.Session()
User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
with open('user.txt', 'r') as f:
    file = f.read().strip()
headers = {
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://app.golike.net/',
    'User-Agent': User_Agent,
    "Authorization": file,
    'Content-Type': 'application/json;charset=utf-8'
}

# Kiểm tra đăng nhập
url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1, headers=headers).json()
if checkurl1['status'] == 200:
    banner()
    print(f"{Fore.GREEN}✅ ĐĂNG NHẬP THÀNH CÔNG{Style.RESET_ALL}")
    time.sleep(2)
    username = checkurl1['data']['username']
    coin = checkurl1['data']['coin']
    banner()
    print(f"{Fore.YELLOW}👤 THÔNG TIN TÀI KHOẢN{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Tên tài khoản: {Fore.YELLOW}{username}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Số dư: {Fore.YELLOW}{coin} VNĐ{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
    
    LIST()
    choose = int(input(f"{Fore.YELLOW}➤ Chọn chức năng (1-2): {Style.RESET_ALL}"))
    if choose == 1:
        LINKEDIN()
    elif choose == 2:
        os.remove('user.txt')
        print(f"{Fore.GREEN}✔ Đã xóa Authorization{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}❌ ĐĂNG NHẬP THẤT BẠI{Style.RESET_ALL}")
    os.remove('user.txt')