import requests
import time
import os
from colorama import init, Fore, Style
from tqdm import tqdm
import logging
import random

# Khởi tạo colorama và logging
init()
logging.basicConfig(filename='script_runner.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Danh sách các mục với URL
SCRIPTS = {
    "1": {"name": "Reg mail.tm", "url": "https://raw.githubusercontent.com/thienton85/Kihjcvi/refs/heads/main/regtm.py"},
    "2": {"name": "Đào proxy + check live", "url": "https://raw.githubusercontent.com/thienton85/Kihjcvi/refs/heads/main/proxy.py"},
    "3": {"name": "Auto golike Snapchat adb + thủ công", "url": "https://raw.githubusercontent.com/thienton85/Kihjcvi/refs/heads/main/encode-adblsn.py"},
    "4": {"name": "Auto Golike Tiktok adb + thủ công", "url": "https://raw.githubusercontent.com/thienton85/Kihjcvi/refs/heads/main/encode-adbltt.py"},
    "5": {"name": "Reg Facebook Vip", "url": "https://raw.githubusercontent.com/thienton85/Kihjcvi/refs/heads/main/regfbvipmh.py"},
    "6": {"name": "Auto golike Snapchat trực tiếp nhận tiền", "url": "https://raw.githubusercontent.com/thienton85/Kihjcvi/refs/heads/main/snglkh.py"},
    "7": {"name": "chưa thêm", "url": "https://raw.githubusercontent.com/Khanh23047/Golike-likedin/refs/heads/main/p.py"},
    "8": {"name": "chưa thêm", "url": "https://raw.githubusercontent.com/Khanh23047/Golike-likedin/refs/heads/main/p.py"},
    "9": {"name": "chưa thêm", "url": "https://raw.githubusercontent.com/Khanh23047/Golike-likedin/refs/heads/main/p.py"}
}

def clear_screen():
    """Xóa màn hình console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, color=Fore.WHITE, delay=0.01):
    """Hiệu ứng đánh máy VIP"""
    for char in text:
        print(f"{color}{Style.BRIGHT}{char}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(delay)
    print()

def fade_in_line(text, color=Fore.WHITE, steps=10):
    """Hiệu ứng fade-in mượt mà hơn"""
    for i in range(steps):
        partial = text[:int(len(text) * (i+1) / steps)]
        print(f"{color}{Style.DIM}{partial}{Style.RESET_ALL}", end='\r', flush=True)
        time.sleep(0.025)
    print(f"{color}{Style.BRIGHT}{text}{Style.RESET_ALL}")

def wave_effect(text, color=Fore.WHITE, cycles=4):
    """Hiệu ứng sóng VIP với ánh sáng"""
    for i in range(cycles):
        padding_left = " " * (i % 4)
        padding_right = " " * ((3 - i) % 4)
        wave_text = f"{padding_left}✦ {text} ✦{padding_right}".center(60)
        print(f"{color}{Style.BRIGHT}{wave_text}{Style.RESET_ALL}", end='\r', flush=True)
        time.sleep(0.12)
    print(f"{color}{Style.BRIGHT}{f'✦ {text} ✦'.center(60)}{Style.RESET_ALL}")

def gradient_sweep(text, colors, cycles=3):
    """Hiệu ứng gradient chuyển màu"""
    for _ in range(cycles):
        for color in colors:
            print(f"{color}{Style.BRIGHT}{text}{Style.RESET_ALL}", end='\r', flush=True)
            time.sleep(0.1)
    print(f"{colors[-1]}{Style.BRIGHT}{text}{Style.RESET_ALL}")

def show_loading():
    """Hiển thị màn hình khởi động"""
    clear_screen()
    loading_symbols = ["◉", "◎", "◍", "◌", "◐", "◑"]
    title = "SCODE - KHỞI ĐỘNG"
    
    for i in range(5):
        clear_screen()
        print(f"{Fore.YELLOW}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}", end='')
        padding = " " * (i % 3)
        centered_text = f"{padding}{title}{padding}".center(42)
        print(f"{Fore.WHITE}{centered_text}{Style.RESET_ALL}", end='')
        print(f"{Fore.YELLOW}║{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{loading_symbols[i % len(loading_symbols)]} Đang kết nối hệ thống...{Style.RESET_ALL}")
        time.sleep(0.2)
    
    print(f"{Fore.CYAN}Quá trình khởi động:{Style.RESET_ALL}")
    with tqdm(total=100, desc="", bar_format="{l_bar}{bar}{r_bar}", colour='green') as pbar:
        for i in range(100):
            pbar.set_description(f"{Fore.GREEN}▷ Tải [{i+1}%]{Style.RESET_ALL}")
            pbar.update(1)
            time.sleep(0.025)
    
    clear_screen()
    wave_effect("╔════ HỆ THỐNG SẴN SÀNG ════╗", Fore.GREEN)
    wave_effect("║ SCODE HOẠT ĐỘNG            ║", Fore.GREEN)
    wave_effect("╚════════════════════════════╝", Fore.GREEN)
    time.sleep(0.5)
    clear_screen()

def run_script_from_url(url, script_name):
    """Chạy script với giao diện và hiệu ứng"""
    clear_screen()
    print(f"{Fore.BLUE}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
    typing_effect(f"  ĐANG CHẠY: {script_name}".center(44), Fore.CYAN, 0.015)
    print(f"{Fore.BLUE}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    try:
        with tqdm(total=100, desc="", bar_format="{l_bar}{bar}{r_bar}", colour='blue') as pbar:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            script_content = response.text
            for i in range(100):
                pbar.set_description(f"{Fore.CYAN}⟳ Đang tải [{i+1}%]{Style.RESET_ALL}")
                pbar.update(1)
                time.sleep(0.01)
        
        print(f"\n{Fore.GREEN}▷ Thực thi {script_name}...{Style.RESET_ALL}")
        exec(script_content, globals())
        logging.info(f"Hoàn thành: {script_name}")
        fade_in_line(f"✔ Thành công: {script_name}", Fore.GREEN)
    except requests.exceptions.RequestException as e:
        logging.error(f"Lỗi kết nối {script_name}: {e}")
        fade_in_line(f"✘ Lỗi mạng: {e}", Fore.RED)
    except Exception as e:
        logging.error(f"Lỗi thực thi {script_name}: {e}")
        fade_in_line(f"✘ Thực thi thất bại: {e}", Fore.RED)

def transition_to_tool(script_name):
    """Hiệu ứng chuyển tiếp vào tool"""
    clear_screen()
    print(f"{Fore.MAGENTA}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
    typing_effect(f"  KHỞI CHẠY: {script_name}".center(44), Fore.WHITE, 0.015)
    print(f"{Fore.MAGENTA}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    spinner = ["◴", "◷", "◶", "◵"]
    print(f"{Fore.CYAN}Đang khởi tạo", end='', flush=True)
    for i in range(6):
        time.sleep(0.2)
        print(f"{Fore.CYAN} {spinner[i % len(spinner)]}{Style.RESET_ALL}", end='\r', flush=True)
    print(f"\n{Fore.GREEN}✔ Khởi tạo hoàn tất{Style.RESET_ALL}")
    time.sleep(0.3)
    
    clear_screen()
    print(f"{Fore.YELLOW}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
    typing_effect(f"  KIỂM TRA: {script_name}".center(44), Fore.WHITE, 0.015)
    print(f"{Fore.YELLOW}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    stages = ["Kiểm tra kết nối...", "Xác nhận quyền truy cập...", "Tải cấu hình..."]
    for stage in stages:
        print(f"{Fore.CYAN}⮞ {stage}", end='', flush=True)
        for _ in range(3):
            time.sleep(0.25)
            print(f"{Fore.CYAN}.{Style.RESET_ALL}", end='', flush=True)
        print(f"{Fore.GREEN} [Hoàn tất]{Style.RESET_ALL}")
    time.sleep(0.5)
    
    clear_screen()
    print(f"{Fore.GREEN}╔════════════════════════════════════════════╗{Style.RESET_ALL}")
    typing_effect(f"  CHUẨN BỊ: {script_name}".center(44), Fore.WHITE, 0.015)
    print(f"{Fore.GREEN}╚════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    with tqdm(total=50, desc=f"{Fore.CYAN}Chuẩn bị chạy{Style.RESET_ALL}", bar_format="{l_bar}{bar}{r_bar}", colour='green') as pbar:
        for i in range(50):
            pbar.update(1)
            time.sleep(0.03)
    fade_in_line(f"✔ Sẵn sàng: {script_name}", Fore.GREEN)
    time.sleep(0.5)

def display_menu():
    """Hiển thị giao diện chính VIP với hiệu ứng SCODE đẹp hơn"""
    clear_screen()
    
    # Giai đoạn 1: Hiệu ứng SCODE lớn với gradient và sóng
    colors = [Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.YELLOW]
    scode_text = "SCODE"  # Tách các chữ cái để tạo hiệu ứng
    version_text = "Phiên bản: V1"
    
    for i in range(6):
        clear_screen()
        border = f"{colors[i % len(colors)]}╔═{'═' * 60}═╗{Style.RESET_ALL}"
        print(border)
        
        # Hiệu ứng sóng cho SCODE
        padding = " " * (i % 4)
        scode_line = ""
        for char in scode_text:
            scode_line += f"{colors[i % len(colors)]}{Style.BRIGHT}{char}{Style.RESET_ALL} "
        scode_display = f"{padding}{scode_line.strip()}{padding}".center(62)
        print(f"{colors[i % len(colors)]}║{Style.RESET_ALL}{scode_display}{Style.RESET_ALL}║")
        
        # Dòng phiên bản nhỏ hơn bên dưới
        version_display = version_text.center(62)
        print(f"{colors[i % len(colors)]}║{Style.RESET_ALL}{Fore.WHITE}{Style.DIM}{version_display}{Style.RESET_ALL}║")
        print(f"{colors[i % len(colors)]}╚═{'═' * 60}═╝{Style.RESET_ALL}")
        time.sleep(0.12)
    
    # Giai đoạn 2: Fade-in tiêu đề hoàn chỉnh
    clear_screen()
    print(f"{Fore.BLUE}╔═{'═' * 60}═╗{Style.RESET_ALL}")
    fade_in_line(f"║ {Style.BRIGHT}{scode_text.center(60)}{Style.RESET_ALL} ║", Fore.CYAN, steps=15)
    fade_in_line(f"║ {Style.DIM}{version_text.center(60)}{Style.RESET_ALL} ║", Fore.WHITE, steps=10)
    print(f"{Fore.BLUE}╚═{'═' * 60}═╝{Style.RESET_ALL}")
    
    # Giai đoạn 3: Thông tin hệ thống
    time.sleep(0.2)
    print(f"{Fore.GREEN}╔═{'═' * 60}═╗{Style.RESET_ALL}")
    fade_in_line(f"║ {Style.BRIGHT}THÔNG TIN HỆ THỐNG{' ' * 41}{Style.NORMAL}║", Fore.GREEN)
    fade_in_line(f"║   ▣ {Style.NORMAL}Admin:{Style.BRIGHT} Nguyễn Văn Đạt{' ' * 34}║", Fore.GREEN)
    fade_in_line(f"║   ▣ {Style.NORMAL}YouTube:{Style.BRIGHT} SIÊU CODE{' ' * 30}║", Fore.GREEN)
    fade_in_line(f"║   ▣ {Style.NORMAL}Zalo:{Style.BRIGHT} 0982....{' ' * 30}║", Fore.GREEN)
    fade_in_line(f"║   ▣ {Style.NORMAL}Thời gian:{Style.BRIGHT} {time.strftime('%H:%M:%S')}{' ' * 30}║", Fore.GREEN)
    print(f"{Fore.GREEN}╚═{'═' * 60}═╝{Style.RESET_ALL}")
    
    # Giai đoạn 4: Tiêu đề bảng điều khiển
    time.sleep(0.3)
    wave_effect("BẢNG ĐIỀU KHIỂN VIP", Fore.YELLOW)
    fade_in_line(f"  ▣ {Style.NORMAL}Trạng thái:{Style.BRIGHT} Trực tuyến{Style.NORMAL} | {Style.NORMAL}Công cụ:{Style.BRIGHT} {len(SCRIPTS)}", Fore.YELLOW)
    
    # Giai đoạn 5: Danh sách script
    time.sleep(0.2)
    print(f"{Fore.CYAN}╔═{'═' * 60}═╗{Style.RESET_ALL}")
    fade_in_line(f"║ {Style.BRIGHT}CÔNG CỤ HOẠT ĐỘNG{' ' * 42}{Style.NORMAL}║", Fore.CYAN)
    for key, value in SCRIPTS.items():
        status_color = Fore.GREEN if key != "0" else Fore.RED
        fade_in_line(f"║   ▣ {Style.NORMAL}[{key}] {Style.BRIGHT}{value['name']:<38}{Style.NORMAL} [{('BẬT' if key != '0' else 'TẮT')}]", status_color)
    fade_in_line(f"║   ▣ {Style.NORMAL}[0] {Style.BRIGHT}{'Tắt hệ thống':<38}{Style.NORMAL} [TẮT]", Fore.RED)
    print(f"{Fore.CYAN}╚═{'═' * 60}═╝{Style.RESET_ALL}")
    
    # Footer đã sửa: Chỉ hiển thị 1 lần với hiệu ứng đơn giản
    time.sleep(0.2)
    symbols = ["✪", "✬", "✯", "✰"]
    footer_text = f"SCODE v1.0 | BY NVĐ {random.choice(symbols)}"
    footer_line = f"╚════{footer_text.center(56)}════╝"
    fade_in_line(footer_line, Fore.CYAN)  # Sử dụng fade_in_line để hiển thị 1 lần duy nhất

def main():
    # Hiển thị loading khi khởi động
    show_loading()
    logging.info("Hệ thống khởi động")
    
    while True:
        display_menu()
        choice = input(f"\n{Fore.CYAN}  ▸ {Style.NORMAL}Nhập lựa chọn (0-9):{Style.RESET_ALL} ")

        if choice == "0":
            clear_screen()
            wave_effect("╔════ TẮT HỆ THỐNG ════╗", Fore.RED)
            wave_effect(f"║ Ngoại tuyến: {time.strftime('%Y-%m-%d %H:%M:%S')} ║", Fore.RED)
            wave_effect("╚═══════════════════════╝", Fore.RED)
            logging.info("Hệ thống tắt")
            break
        elif choice in SCRIPTS:
            script_info = SCRIPTS[choice]
            transition_to_tool(script_info['name'])
            run_script_from_url(script_info['url'], script_info['name'])
            input(f"\n{Fore.YELLOW}Nhấn Enter để quay lại...{Style.RESET_ALL}")
        else:
            fade_in_line("✘ Lệnh không hợp lệ!", Fore.RED)
            input(f"\n{Fore.YELLOW}Nhấn Enter để tiếp tục...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
