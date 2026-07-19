def update(completion):
    ends = "|"
    body = "="
    pointer = ">"
    intervals = 20
    bucket = 100//intervals
    intervals = intervals
    bodies = int(completion // bucket)
    string = ends
    string += body * bodies
    string += pointer
    string += " " * (intervals - bodies + 1)
    string += ends
    return string

def ft_tqdm(lst: range) -> None:
    maxIters = len(lst)
    for iters in lst:
        progress = (iters + 1) * 100 / maxIters
        print(f"{progress:.0f}%{update(progress)} {iters+1}/{maxIters}", end="\r")
        yield
    return
