from colorama import init, Fore, Style
import time

# Khởi tạo colorama để hỗ trợ màu sắc trên terminal
init()

def display_message():
    # Xóa màn hình (làm việc trên Windows/Linux/Mac)
    print("\033c", end="")
    
    # Thiết kế thông báo với màu sắc
    print(f"{Fore.CYAN}{Style.BRIGHT}╔════════════════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║                                    ║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}║  Tool đã có phiên bản mới!         ║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}║  Liên hệ admin để lấy.             ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}║                                    ║{Style.RESET_ALL}")
    print(f"{Fore.CYAN}╚════════════════════════════════════╝{Style.RESET_ALL}")
    
    # Đợi 5 giây trước khi thoát
    print(f"\n{Fore.GREEN}Chương trình sẽ tự động thoát sau 5 giây...{Style.RESET_ALL}")
    time.sleep(5)

if __name__ == "__main__":
    display_message()
