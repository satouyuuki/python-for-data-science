import time

maxIters = 100
for iters in range(maxIters):
    print(f"{iters+1} / {maxIters}", end="\r")
    time.sleep(1)
