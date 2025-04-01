import requests
import time
import os
from art import text2art
from colorama import Fore, Style, init
import json
import random
import sys
import asyncio
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36"
]

DEFAULT_HEADERS = {
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
    'Referer': 'https://app.golike.net/',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': "Windows",
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'T': 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
    'Content-Type': 'application/json;charset=utf-8'
}

class ToolUI:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_banner():
        ToolUI.clear_screen()
        banner = text2art("Golike X", font="small")
        print(f"{Fore.CYAN}{Style.BRIGHT}{banner}")
        print(f"{Fore.YELLOW}╔════════════════════════════════════════════════════╗")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}Tool By: NGUYỄN VĂN ĐẠT         Version: 1.0         {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}Zalo: https://zalo.me/g/nexigi855        {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}║ {Fore.GREEN}Youtube: @scode           {Fore.YELLOW}║")
        print(f"{Fore.YELLOW}╚════════════════════════════════════════════════════╝")
        print()

    @staticmethod
    def loading_animation(message, duration=2):
        symbols = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧']
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            sys.stdout.write(f'\r{Fore.CYAN}{Style.BRIGHT}{symbols[i % len(symbols)]} {message}')
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1
        print(f'\r{Fore.GREEN}{Style.BRIGHT}✔ {message}{" " * 20}')

    @staticmethod
    def display_account_info(user_data):
        ToolUI.print_banner()
        print(f"{Fore.CYAN}{Style.BRIGHT}🎉 THÔNG TIN TÀI KHOẢN GOLIKE")
        print(f"{Fore.MAGENTA}╭{'─' * 50}╮")
        print(f"{Fore.MAGENTA}│ {Fore.GREEN}👤 Tên tài khoản : {Fore.WHITE}{user_data['username']:<36} {Fore.MAGENTA}│")
        print(f"{Fore.MAGENTA}│ {Fore.GREEN}💰 Số dư hiện tại: {Fore.YELLOW}{user_data['coin']:,} VNĐ{Fore.RESET}{' ' * (35-len(str(f'{user_data['coin']:,}')))} {Fore.MAGENTA}│")
        print(f"{Fore.MAGENTA}│ {Fore.GREEN}🆔 ID người dùng : {Fore.WHITE}{user_data['id']:<36} {Fore.MAGENTA}│")
        print(f"{Fore.MAGENTA}╰{'─' * 50}╯")
        print()

    @staticmethod
    def display_twitter_accounts(accounts, user_data):
        ToolUI.print_banner()
        print(f"{Fore.CYAN}{Style.BRIGHT}📊 DANH SÁCH TÀI KHOẢN TWITTER (X) - CHỦ: {Fore.YELLOW}{user_data['username']}")
        print(f"{Fore.GREEN}╭{'─' * 40}╮")
        print(f"{Fore.GREEN}│ {Fore.WHITE}Tổng số dư    : {Fore.YELLOW}{user_data['coin']:,} VNĐ{' ' * (23-len(str(f'{user_data['coin']:,}')))} {Fore.GREEN}│")
        print(f"{Fore.GREEN}│ {Fore.WHITE}ID người dùng : {Fore.YELLOW}{user_data['id']}{' ' * (25-len(str(user_data['id'])))} {Fore.GREEN}│")
        print(f"{Fore.GREEN}╰{'─' * 40}╯")
        print()

        print(f"{Fore.BLUE}╔════╦{'═' * 22}╦{'═' * 15}╦{'═' * 12}╗")
        print(f"{Fore.BLUE}║ {Fore.YELLOW}STT{Fore.BLUE} ║ {Fore.YELLOW}TÀI KHOẢN TWITTER      {Fore.BLUE}║ {Fore.YELLOW}ID TÀI KHOẢN {Fore.BLUE}║ {Fore.YELLOW}TRẠNG THÁI {Fore.BLUE}║")
        print(f"{Fore.BLUE}╠════╬{'═' * 22}╬{'═' * 15}╬{'═' * 12}╣")

        for i, acc in enumerate(accounts['data'], 1):
            screen_name = acc['screen_name']
            account_id = acc.get('id', 'N/A')
            display_name = (screen_name[:18] + '...') if len(screen_name) > 18 else screen_name.ljust(18)
            display_id = (str(account_id)[:12] + '...') if len(str(account_id)) > 12 else str(account_id).ljust(12)
            status = "Hoạt động"
            
            print(f"{Fore.BLUE}║ {Fore.GREEN}{str(i).rjust(2)}{' ' * 2} {Fore.BLUE}║ "
                  f"{Fore.WHITE}@{display_name:<19} {Fore.BLUE}║ "
                  f"{Fore.WHITE}{display_id:<13} {Fore.BLUE}║ "
                  f"{Fore.GREEN}{status.center(10)}{Fore.BLUE} ║")
            
            if i < len(accounts['data']):
                print(f"{Fore.BLUE}├────┼{'─' * 22}┼{'─' * 15}┼{'─' * 12}┤")

        print(f"{Fore.BLUE}╚════╩{'═' * 22}╩{'═' * 15}╩{'═' * 12}╝")
        print(f"{Fore.YELLOW}➤ Tổng cộng: {Fore.WHITE}{len(accounts['data'])} tài khoản Twitter (X)")
        print()

    @staticmethod
    def input_prompt(prompt, options=None, clear_after=True):
        print(f"{Fore.GREEN}{Style.BRIGHT}✦ {prompt.upper()} ✦")
        print(f"{Fore.GREEN}╭{'─' * 40}╮")
        if options:
            for i, opt in enumerate(options, 1):
                print(f"{Fore.GREEN}│ {Fore.YELLOW}{i}. {Fore.WHITE}{opt:<36} {Fore.GREEN}│")
        else:
            print(f"{Fore.GREEN}│ {prompt:<38} {Fore.GREEN}│")
        print(f"{Fore.GREEN}╰{'─' * 40}╯")
        value = input(f"{Fore.WHITE}➤ ")
        if clear_after:
            ToolUI.clear_screen()
            ToolUI.print_banner()
        return value

    @staticmethod
    def display_task_runner(delay, account_name):
        ToolUI.clear_screen()
        print(f"{Fore.CYAN}{Style.BRIGHT}🚀 TRÌNH XỬ LÝ NHIỆM VỤ - TK: {Fore.YELLOW}{account_name}")
        print(f"{Fore.GREEN}╭{'─' * 50}╮")
        print(f"{Fore.GREEN}│ {Fore.YELLOW}Chế độ       : {Fore.WHITE}Chạy liên tục{' ' * 28} {Fore.GREEN}│")
        print(f"{Fore.GREEN}│ {Fore.YELLOW}Thời gian chờ: {Fore.WHITE}{delay} giây{' ' * (34-len(str(delay)))} {Fore.GREEN}│")
        print(f"{Fore.GREEN}╰{'─' * 50}╯")
        print(f"{Fore.MAGENTA}{Style.BRIGHT}✦ TRẠNG THÁI NHIỆM VỤ ✦")
        print(f"{Fore.MAGENTA}{'═' * 50}")

    @staticmethod
    def display_earning(count, timestamp, job_type, amount, total):
        print(f"{Fore.GREEN}╔{'─' * 44}╗")
        print(f"{Fore.GREEN}║ {Fore.WHITE}[{count:03d}] {Fore.CYAN}{timestamp} {Fore.GREEN}✔ {Fore.YELLOW}{job_type:<10} {Fore.GREEN}+{Fore.YELLOW}{amount:,} VNĐ{Fore.GREEN}{' ' * (6-len(str(amount)))}║")
        print(f"{Fore.GREEN}║ {Fore.WHITE}Tổng thu nhập: {Fore.YELLOW}{total:,} VNĐ{' ' * (28-len(str(f'{total:,}')))} {Fore.GREEN}║")
        print(f"{Fore.GREEN}╚{'─' * 44}╝")

    @staticmethod
    def display_multi_account_status(accounts_status):
        ToolUI.clear_screen()
        print(f"{Fore.CYAN}{Style.BRIGHT}🌐 TRÌNH XỬ LÝ ĐA TÀI KHOẢN TWITTER (X)")
        print(f"{Fore.BLUE}╔════╦{'═' * 22}╦{'═' * 12}╦{'═' * 12}╦{'═' * 15}╗")
        print(f"{Fore.BLUE}║ {Fore.YELLOW}STT{Fore.BLUE} ║ {Fore.YELLOW}TÀI KHOẢN TWITTER      {Fore.BLUE}║ {Fore.YELLOW}NHIỆM VỤ {Fore.BLUE}║ {Fore.YELLOW}THU NHẬP {Fore.BLUE}║ {Fore.YELLOW}TRẠNG THÁI   {Fore.BLUE}║")
        print(f"{Fore.BLUE}╠════╬{'═' * 22}╬{'═' * 12}╬{'═' * 12}╬{'═' * 15}╣")
        
        for i, status in enumerate(accounts_status, 1):
            display_name = (status['name'][:18] + '...') if len(status['name']) > 18 else status['name'].ljust(18)
            job_count = str(status['jobs']).rjust(5)
            earnings = f"{status['earnings']:,} VNĐ".ljust(10)
            state = status['status'].center(13)
            color = Fore.GREEN if status['status'] == 'Running' else Fore.RED
            
            print(f"{Fore.BLUE}║ {Fore.GREEN}{str(i).rjust(2)}{' ' * 2} {Fore.BLUE}║ "
                  f"{Fore.WHITE}@{display_name:<19} {Fore.BLUE}║ "
                  f"{Fore.WHITE}{job_count:<10} {Fore.BLUE}║ "
                  f"{Fore.YELLOW}{earnings:<11} {Fore.BLUE}║ "
                  f"{color}{state:<13}{Fore.BLUE} ║")
            
            if i < len(accounts_status):
                print(f"{Fore.BLUE}├────┼{'─' * 22}┼{'─' * 12}┼{'─' * 12}┼{'─' * 15}┤")
        
        print(f"{Fore.BLUE}╚════╩{'═' * 22}╩{'═' * 12}╩{'═' * 12}╩{'═' * 15}╝")
        print(f"{Fore.YELLOW}➤ Tổng tài khoản hoạt động: {Fore.WHITE}{len([s for s in accounts_status if s['status'] == 'Running'])}")

class TwitterBot:
    def __init__(self):
        self.session = requests.Session()
        self.auth_file = 'user.txt'
        self.user_agent = random.choice(USER_AGENTS)
        self.headers = DEFAULT_HEADERS.copy()
        self.headers['User-Agent'] = self.user_agent
        self.accounts_status = []
        self.retry_count = 0
        self.max_retries = 5

    def load_or_create_auth(self):
        ToolUI.clear_screen()
        ToolUI.print_banner()
        print(f"{Fore.CYAN}{Style.BRIGHT}🔑 QUẢN LÝ AUTHORIZATION")
        print(f"{Fore.YELLOW}╭{'─' * 50}╮")
        if os.path.isfile(self.auth_file):
            with open(self.auth_file, 'r') as f:
                old_auth = f.read().strip()
            temp_headers = self.headers.copy()
            temp_headers['Authorization'] = old_auth
            username = "Không xác định (auth lỗi)"
            try:
                response = self.session.get('https://gateway.golike.net/api/users/me', headers=temp_headers, timeout=10)
                response.raise_for_status()
                data = response.json()
                if data.get('status') == 200:
                    username = data['data']['username']
            except requests.RequestException:
                pass
            
            print(f"{Fore.YELLOW}│ {Fore.GREEN}Đã tìm thấy Authorization cũ{' ' * 21} {Fore.YELLOW}│")
            print(f"{Fore.YELLOW}├{'─' * 50}┤")
            print(f"{Fore.YELLOW}│ {Fore.GREEN}Tài khoản Golike: {Fore.WHITE}{username:<28} {Fore.YELLOW}│")
            print(f"{Fore.YELLOW}╰{'─' * 50}╯")
            print()  # Thêm dòng trống để tách biệt
            choice = ToolUI.input_prompt("Sử dụng auth này? (y/n)", None, True)
            if choice.lower() == 'y':
                self.headers['Authorization'] = old_auth
                return
        print(f"{Fore.YELLOW}│ {Fore.GREEN}Vui lòng nhập Authorization mới{' ' * 19} {Fore.YELLOW}│")
        print(f"{Fore.YELLOW}╰{'─' * 50}╯")
        print()
        auth = ToolUI.input_prompt("Nhập Authorization Golike", None, True)
        with open(self.auth_file, 'w') as f:
            f.write(auth)
        self.headers['Authorization'] = auth

    async def check_login(self):
        try:
            response = self.session.get('https://gateway.golike.net/api/users/me', 
                                     headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get('status') == 200:
                return data['data']
            else:
                print(f"{Fore.RED}die")
                return None
        except requests.RequestException:
            print(f"{Fore.RED}die")
            return None

    async def get_twitter_accounts(self):
        try:
            response = self.session.get('https://gateway.golike.net/api/twitter-account',
                                      headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            print(f"{Fore.RED}die")
            return None

    async def process_jobs(self, account_id, delay, account_name, multi_mode=False, status=None):
        job_url = f'https://gateway.golike.net/api/advertising/publishers/twitter/jobs?account_id={account_id}'
        
        total_earned = 0
        success_count = 0
        
        if not multi_mode:
            ToolUI.display_task_runner(delay, account_name)
        
        while True if not multi_mode else status['status'] == 'Running':
            try:
                print(f"{Fore.YELLOW}➤ Đang lấy nhiệm vụ..." if not multi_mode else "")
                job_response = await asyncio.to_thread(self.session.get, job_url, headers=self.headers)
                job_response.raise_for_status()
                job_data = job_response.json()
                
                if job_data['status'] != 200:
                    print(f"{Fore.RED}die" if not multi_mode else "")
                    if job_data['status'] == 400:
                        if self.retry_count < self.max_retries:
                            self.retry_count += 1
                            print(f"{Fore.YELLOW}➤ Thử lại lần {self.retry_count}/{self.max_retries}..." if not multi_mode else "")
                            await asyncio.sleep(5 * self.retry_count)
                            continue
                        else:
                            print(f"{Fore.RED}die" if not multi_mode else "")
                            if multi_mode:
                                status['status'] = 'Error: Max retries exceeded'
                            break
                    await asyncio.sleep(15)
                    continue

                self.retry_count = 0
                job_type = job_data['data']['type']
                ads_id = job_data['data']['id']
                object_id = job_data['data']['object_id']

                await asyncio.sleep(delay)
                complete_response = await self.complete_job(ads_id, account_id, job_type)
                
                if complete_response and complete_response.get('success'):
                    prices = complete_response['data']['prices']
                    total_earned += prices
                    success_count += 1
                    if multi_mode:
                        status['earnings'] += prices
                        status['jobs'] += 1
                    else:
                        timestamp = time.strftime("%H:%M:%S")
                        ToolUI.display_earning(success_count, timestamp, job_type.upper(), prices, total_earned)
                else:
                    await self.skip_job(ads_id, account_id, object_id, job_type)
                
                await asyncio.sleep(delay)
                
            except requests.RequestException:
                print(f"{Fore.RED}die" if not multi_mode else "")
                if multi_mode:
                    status['status'] = 'Error: Request failed'
                break
            except Exception:
                print(f"{Fore.RED}die" if not multi_mode else "")
                if multi_mode:
                    status['status'] = 'Error: Unexpected'
                break

    async def complete_job(self, ads_id, account_id, job_type):
        url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
        payload = {
            'ads_id': str(ads_id),
            'account_id': str(account_id),
            'async': 'true',
            'type': job_type
        }
        try:
            response = self.session.post(url, headers=self.headers, json=payload, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            print(f"{Fore.RED}die")
            return None

    async def skip_job(self, ads_id, account_id, object_id, job_type):
        url = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
        params = {
            'ads_id': ads_id,
            'account_id': account_id,
            'object_id': object_id,
            'async': 'true',
            'type': job_type
        }
        try:
            response = self.session.post(url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            if data.get('status') == 200:
                print(f"{Fore.YELLOW}↷ Đã bỏ qua job: {data.get('message')}")
        except requests.RequestException:
            print(f"{Fore.RED}die")

    async def process_account(self, account, delay, semaphore):
        async with semaphore:
            account_id = account['id']
            account_name = account['screen_name']
            status = {
                'name': account_name,
                'jobs': 0,
                'earnings': 0,
                'status': 'Running'
            }
            self.accounts_status.append(status)
            
            try:
                await self.process_jobs(account_id, delay, account_name, multi_mode=True, status=status)
            except Exception:
                status['status'] = 'Error: Unexpected'

    async def run_multi_accounts(self, accounts, delay, max_concurrent=5):
        semaphore = asyncio.Semaphore(max_concurrent)
        tasks = [self.process_account(account, delay, semaphore) for account in accounts['data']]
        
        async def status_updater():
            while True:
                ToolUI.display_multi_account_status(self.accounts_status)
                await asyncio.sleep(2)

        await asyncio.gather(*tasks, status_updater())

async def main():
    bot = TwitterBot()
    
    bot.load_or_create_auth()
    ToolUI.loading_animation("Đang kiểm tra đăng nhập...", 2)
    user_data = await bot.check_login()
    
    if user_data:
        ToolUI.display_account_info(user_data)
        accounts = await bot.get_twitter_accounts()
        if accounts and 'data' in accounts:
            ToolUI.display_twitter_accounts(accounts, user_data)
            
            mode = ToolUI.input_prompt("Chọn chế độ", ["Single", "Multi"])
            delay = int(ToolUI.input_prompt("Nhập thời gian delay (giây)"))
            
            if mode == '1':
                acc_choice = int(ToolUI.input_prompt(f"Chọn tài khoản (1-{len(accounts['data'])})"))
                account_name = accounts['data'][acc_choice-1]['screen_name']
                await bot.process_jobs(accounts['data'][acc_choice-1]['id'], delay, account_name)
            elif mode == '2':
                max_concurrent = int(ToolUI.input_prompt(f"Số tài khoản chạy cùng lúc (max {len(accounts['data'])})"))
                max_concurrent = min(max_concurrent, len(accounts['data']))
                await bot.run_multi_accounts(accounts, delay, max_concurrent)
            else:
                print(f"{Fore.RED}✗ Chế độ không hợp lệ!")
        else:
            print(f"{Fore.RED}✗ Không lấy được danh sách tài khoản Twitter")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}✗ ĐĂNG NHẬP THẤT BẠI")
        if os.path.exists(bot.auth_file):
            os.remove(bot.auth_file)

if __name__ == "__main__":
    asyncio.run(main())