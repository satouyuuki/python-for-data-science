import os

padding = " "
term_size = os.get_terminal_size().columns
print(term_size)
padding += padding * (term_size - 42)
print(f"100%|{padding}| 333/333")
