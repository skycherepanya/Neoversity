import sys
import os
from colorama import Fore, Style

if len(sys.argv) < 2:
    print(f"{Fore.RED}Будь ласка, вкажіть шлях до папки.{Style.RESET_ALL}")
    print(f"Приклад: python {sys.argv[0]} .")
    sys.exit(1)

path_from_user = sys.argv[1]
start_path = os.path.normpath(path_from_user)

root_name = os.path.basename(start_path)

if not root_name:
    root_name = start_path

print(f"{Fore.CYAN}{root_name}/{Style.RESET_ALL}")

base_level = start_path.count(os.sep)

for current_folder_path, subfolders, filenames in os.walk(start_path, topdown=True):

    subfolders.sort()
    filenames.sort()
    current_level = current_folder_path.count(os.sep)
    level = current_level - base_level

    if level > 0:

        folder_indent = "    " * level
        folder_name = os.path.basename(current_folder_path)
        print(f"{folder_indent}{Fore.CYAN}{folder_name}/{Style.RESET_ALL}")

    file_indent = "    " * (level + 1)

    for name in filenames:
        print(f"{file_indent}{Fore.GREEN}{name}{Style.RESET_ALL}")