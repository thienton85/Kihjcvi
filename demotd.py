try:
    import requests
    import time
    import os
    from art import *
    from colorama import Fore, Style
    import json
    import random
    from tabulate import tabulate
    import re
    from time import sleep
    import sys
    from random_user_agent.user_agent import UserAgent
    from random_user_agent.params import SoftwareName, OperatingSystem
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
    os.system('pip install random_user_agent')

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

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
    print(f"{Fore.CYAN}║       TOOL Golike Threads V1       ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║   Created by: NGUYÊN VĂN ĐẠT           ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}📌 TikTok: {Fore.GREEN}demov1{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}📌 Telegram: {Fore.GREEN}demov1{Style.RESET_ALL}")
    print()

# Hàm xử lý Threads
def THREADS():
    checkaccount = requests.get('https://gateway.golike.net/api/threads-account', headers=headers).json()
    user_THREADS = []
    account_id1 = []
    i = 1
    tong = 0
    dem = 0

    banner()
    print(f"{Fore.YELLOW}📋 DANH SÁCH TÀI KHOẢN THREADS{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
    for data in checkaccount['data']:
        usernametk = data['name']
        user_THREADS.append(usernametk)
        account_id1.append(data['id'])
        print(f"{Fore.GREEN}[{i}] {Fore.WHITE}Tài khoản: {Fore.YELLOW}{usernametk} {Fore.GREEN}- Trạng thái: {Fore.GREEN}Hoạt động{Style.RESET_ALL}")
        i += 1
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")

    choose = int(input(f"{Fore.YELLOW}➤ Nhập số thứ tự tài khoản (1-{len(user_THREADS)}): {Style.RESET_ALL}"))
    os.system('cls' if os.name == 'nt' else 'clear')
    if 1 <= choose <= len(user_THREADS):
        user_tiktok = user_THREADS[choose - 1]
        account_id = account_id1[choose - 1]

        # Kiểm tra và nhập cookie
        checkfile2 = os.path.isfile(f'COOKIETHR{account_id}.txt')
        if not checkfile2:
            banner()
            cookieTHR = input(f"{Fore.GREEN}🔑 Nhập Cookie Threads cho {user_tiktok}: {Style.RESET_ALL}")
            with open(f'COOKIETHR{account_id}.txt', 'w') as f:
                f.write(cookieTHR)
        else:
            with open(f'COOKIETHR{account_id}.txt', 'r') as f:
                cookieTHR = f.read()

        banner()
        print(f"{Fore.YELLOW}🔧 QUẢN LÝ COOKIE{Style.RESET_ALL}")
        print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[1] Sử dụng cookie hiện tại{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[2] Xóa cookie và nhập lại{Style.RESET_ALL}")
        print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
        URchoose = int(input(f"{Fore.YELLOW}➤ Chọn (1-2): {Style.RESET_ALL}"))
        if URchoose == 2:
            os.remove(f'COOKIETHR{account_id}.txt')
            return 0

        # Nhập số lượng job và delay
        banner()
        print(f"{Fore.YELLOW}🔧 CÀI ĐẶT CÔNG VIỆC{Style.RESET_ALL}")
        choose = int(input(f"{Fore.GREEN}📌 Số lượng job cần thực hiện: {Style.RESET_ALL}"))
        DELAY = int(input(f"{Fore.GREEN}⏱ Thời gian delay (giây): {Style.RESET_ALL}"))

        # Thực hiện công việc
        print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🚀 BẮT ĐẦU THỰC HIỆN CÔNG VIỆC{Style.RESET_ALL}")
        for i in range(choose):
            try:
                headersTHR = {
                    'accept': '*/*',
                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': cookieTHR,
                    'origin': 'https://www.threads.net',
                    'priority': 'u=1, i',
                    'referer': 'https://www.threads.net/@dreyt041',
                    'sec-ch-prefers-color-scheme': 'dark',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-model': '"Pixel 5"',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"13"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': user_agent_rotator.get_random_user_agent(),
                    'x-asbd-id': '129477',
                    'x-csrftoken': cookieTHR.split('csrftoken=')[1].split(';')[0],
                    'x-fb-friendly-name': 'useBarcelonaFollowMutationFollowMutation',
                    'x-fb-lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
                    'x-ig-app-id': '238260118697367',
                }
                job = f'https://gateway.golike.net/api/advertising/publishers/threads/jobs?account_id={account_id}'
                nos = ses.get(job, headers=headers).json()
                if nos['status'] == 200:
                    ads_id = nos['data']['id']
                    object_id = nos['data']['object_id']
                    type = nos['data']['type']
                    link = nos['data']['link']
                    if type == 'follow':
                        try:
                            check = requests.get(link, headers=headersTHR).text
                            fb_dtsg = check.split('"f":"')[1].split('",')[0]
                            user_id = check.split('"props":{"user_id":"')[1].split('",')[0]
                            data = {
                                'av': '17841461328267610',
                                '__user': '0',
                                '__a': '1',
                                '__req': 'c',
                                '__hs': '19925.HYP:barcelona_web_pkg.2.1..0.1',
                                'dpr': '1',
                                '__ccg': 'UNKNOWN',
                                '__rev': '1015041514',
                                '__s': '4oqz5z:tfv4jd:iv92im',
                                '__hsi': '7394241910778378470',
                                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lx-0iS2S3qazo7u0zE2ZwrUdUbGw4mwr86C2q1iwiQ1mwLwHxW17y9UjgdE-19w',
                                '__csr': 'gV2QPfHkGNcIQZFAjlqvap8lbc9qyBByp99O96y9o01J73a4A5hlwQSaxshDk9a4Ujgakph3DS7o6K0_A0hvc2p1afwk41jx7OhM1SmEiglwqcM4d01vhx22t0FhYg0QFA',
                                '__comet_req': '29',
                                'fb_dtsg': fb_dtsg,
                                'jazoest': '26086',
                                'lsd': '6Z5u6bYBj-kOXPD0nbgSGu',
                                '__spin_r': '1015041514',
                                '__spin_b': 'trunk',
                                '__spin_t': '1721606103',
                                'fb_api_caller_class': 'RelayModern',
                                'fb_api_req_friendly_name': 'useBarcelonaFollowMutationFollowMutation',
                                'variables': f'{{"target_user_id":{user_id},"media_id_attribution":null,"container_module":"ig_text_feed_profile"}}',
                                'server_timestamps': 'true',
                                'doc_id': '7812622502155806',
                            }
                            response = requests.post('https://www.threads.net/api/graphql', headers=headersTHR, data=data).text
                            countdown(DELAY)
                            if '"following":true' in response:
                                json_data = {'account_id': account_id, 'ads_id': ads_id}
                                response = requests.post('https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs', headers=headers, json=json_data).json()
                                if response['success']:
                                    dem += 1
                                    prices = response['data']['prices']
                                    tong += prices
                                    local_time = time.localtime()
                                    timestamp = f"{local_time.tm_hour:02d}:{local_time.tm_min:02d}:{local_time.tm_sec:02d}"
                                    print(f"{Fore.GREEN}[{dem}] {Fore.YELLOW}{timestamp} {Fore.GREEN}✔ Thành công | {Fore.CYAN}Follow | {Fore.WHITE}Ẩn ID | {Fore.GREEN}+{prices} | Tổng: {Fore.YELLOW}{tong} VNĐ{Style.RESET_ALL}")
                                else:
                                    skip_job(ads_id, account_id, object_id, type)
                        except IndexError:
                            print(f"{Fore.RED}✖ Cookie hết hạn - Vui lòng thay cookie mới{Style.RESET_ALL}")
                            os.remove(f'COOKIETHR{account_id}.txt')
                            return 0
                    elif type == 'like':
                        try:
                            check = requests.get(link, headers=headersTHR).text
                            fb_dtsg = check.split('"f":"')[1].split('",')[0]
                            post_id = check.split('"props":{"post_id":"')[1].split('",')[0]
                            data = {
                                'av': '17841465195438651',
                                '__user': '0',
                                '__a': '1',
                                '__req': '13',
                                '__hs': '19926.HYP:barcelona_web_pkg.2.1..0.1',
                                'dpr': '1',
                                '__ccg': 'UNKNOWN',
                                '__rev': '1015041902',
                                '__s': 'gmmbni:g1innv:0tm2do',
                                '__hsi': '7394261959223963838',
                                '__dyn': '7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W0om782Cw8G11wBz81s8hwGwQw9m1YwBgao6C0Mo2swlo5qfK0EUjwGzE2ZwNwmE2eUlwhE2Lx-0iS2S3qazo7u0zE2ZwrUdUbGw4mwr86C2q6oe84J0lEbUaUuwhUyu4Q3qfwio',
                                '__csr': 'gV2QP9mJiHkTYQZFAjlqvap8lbc9qKpqG9AAD8Cm8Bw06QscEigl5m3joG5N6tgAEjxd0FhB4evotwqU3-g15YM9A4E-1gg5e4v9706Gy89mEiglwqcM4d01vhx22t0FhYg0QFA58',
                                '__comet_req': '29',
                                'fb_dtsg': fb_dtsg,
                                'jazoest': '26398',
                                'lsd': 'cQ5UmUjtTg4rd7wo5B_3qv',
                                '__spin_r': '1015041902',
                                '__spin_b': 'trunk',
                                '__spin_t': '1721610771',
                                'fb_api_caller_class': 'RelayModern',
                                'fb_api_req_friendly_name': 'useBarcelonaLikeMutationLikeMutation',
                                'variables': f'{{"mediaID":{post_id}}}',
                                'server_timestamps': 'true',
                                'doc_id': '24068295876148027',
                            }
                            response = requests.post('https://www.threads.net/api/graphql', headers=headersTHR, data=data).text
                            countdown(DELAY)
                            if '"is_final":true' in response:
                                json_data = {'account_id': account_id, 'ads_id': ads_id}
                                response = requests.post('https://gateway.golike.net/api/advertising/publishers/threads/complete-jobs', headers=headers, json=json_data).json()
                                if response['success']:
                                    dem += 1
                                    prices = response['data']['prices']
                                    tong += prices
                                    local_time = time.localtime()
                                    timestamp = f"{local_time.tm_hour:02d}:{local_time.tm_min:02d}:{local_time.tm_sec:02d}"
                                    print(f"{Fore.GREEN}[{dem}] {Fore.YELLOW}{timestamp} {Fore.GREEN}✔ Thành công | {Fore.CYAN}Like | {Fore.WHITE}Ẩn ID | {Fore.GREEN}+{prices} | Tổng: {Fore.YELLOW}{tong} VNĐ{Style.RESET_ALL}")
                                else:
                                    skip_job(ads_id, account_id, object_id, type)
                        except IndexError:
                            skip_job(ads_id, account_id, object_id, type)
                else:
                    print(f"{Fore.RED}✖ {nos['message']}{Style.RESET_ALL}")
                    countdown(15)
            except TypeError:
                skip_job(ads_id, account_id, object_id, type)

        print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}🏁 HOÀN THÀNH: {dem} job thành công | Tổng tiền: {tong} VNĐ{Style.RESET_ALL}")

# Hàm bỏ qua job
def skip_job(ads_id, account_id, object_id, type):
    skipjob = 'https://gateway.golike.net/api/advertising/publishers/threads/skip-jobs'
    PARAMS = {
        'ads_id': ads_id,
        'account_id': account_id,
        'object_id': object_id,
        'async': 'true',
        'data': 'null',
        'type': type,
    }
    checkskipjob = ses.post(skipjob, params=PARAMS).json()
    if checkskipjob['status'] == 200:
        print(f"{Fore.RED}✖ {checkskipjob['message']}{Style.RESET_ALL}")

# Hàm hiển thị menu chính
def LIST():
    print(f"{Fore.YELLOW}📋 MENU CHÍNH{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] Chạy tool Threads{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[2] Xóa Authorization hiện tại{Style.RESET_ALL}")
    print(f"{Fore.CYAN}═══════════════════════════════════════{Style.RESET_ALL}")

# Cấu hình ban đầu
ses = requests.Session()
User_Agent = user_agent_rotator.get_random_user_agent()
if not os.path.isfile('user.txt'):
    banner()
    AUTHUR = input(f"{Fore.GREEN}🔑 Nhập Authorization Golike: {Style.RESET_ALL}")
    with open('user.txt', 'w') as f:
        f.write(AUTHUR)
with open('user.txt', 'r') as f:
    file = f.read().strip()

headers = {
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://app.golike.net/',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'T': 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
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
        ip = requests.get('https://api.ipify.org?format=json').json()
        banner()
        print(f"{Fore.GREEN}🌐 IP hiện tại: {Fore.YELLOW}{ip['ip']}{Style.RESET_ALL}")
        THREADS()
    elif choose == 2:
        os.remove('user.txt')
        print(f"{Fore.GREEN}✔ Đã xóa Authorization{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}❌ ĐĂNG NHẬP THẤT BẠI{Style.RESET_ALL}")
    os.remove('user.txt')