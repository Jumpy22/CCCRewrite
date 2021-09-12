import colorama
import random
import sys

def bannerTop():
    banner = '''
  ____ ____ ____ ____                    _ _
 / ___/ ___/ ___|  _ \ _____      ___ __(_| |_ ___
| |  | |  | |   | |_) / _ \ \ /\ / | '__| | __/ _ \\
| |__| |__| |___|  _ |  __/\ V  V /| |  | | ||  __/_
 \____\____\____|_| \_\___| \_/\_/ |_|  |_|\__\___(_)
                Rewritten by Jumpy22
'''

    bad_colors = ['BLACK', 'MAGENTA', 'LIGHTBLACK_EX', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'BLACK', 'RESET', 'LIGHTBLUE_EX', 'LIGHTCYAN_EX', 'LIGHTGREEN_EX', 'LIGHTMAGENTA_EX', 'LIGHTRED_EX', 'LIGHTYELLOW_EX']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)