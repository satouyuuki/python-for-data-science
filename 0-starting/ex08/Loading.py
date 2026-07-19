import os
def update(completion):
    starts = "|["
    ends = "]|"
    body = "="
    pointer = ">"
    intervals = os.get_terminal_size().columns - 44
    bucket = 100 / intervals
    bodies = int(completion / bucket)
    string = starts
    string += body * bodies
    string += pointer
    string += " " * (intervals - bodies)
    string += ends
    return string

def ft_tqdm(lst: range) -> None:
    maxIters = len(lst)
    for iters in lst:
        progress = (iters + 1) * 100 / maxIters
        print(f"{progress:.0f}%{update(progress)} {iters+1}/{maxIters}", end="\r")
        yield
    return
