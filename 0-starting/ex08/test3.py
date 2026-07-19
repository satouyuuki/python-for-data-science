# import time


# class ProgressBar:
#     def __init__(self, ends = "|", body = "=",
# pointer = ">", intervals = 20):
#         self.ends = ends
#         self.body = body
#         self.pointer = pointer
#         # //でfloatではなくてintになる
#         self.bucket = 100//intervals
#         self.progress = 0
#         self.intervals = intervals


#     def update(self, completion):
#         bodies = int(completion // self.bucket)
#         print(bodies)
#         string = self.ends
#         string += self.body * bodies
#         string += self.pointer
#         string += " " * (self.intervals - bodies + 1)
#         string += self.ends
#         return string


# bar = ProgressBar()
# #print(bar.update(45))
# maxIters = 100
# for iters in range(maxIters):
#     progress = (iters + 1) * 100 / maxIters
#     print(f"Custom tqdm: {iters+1} / {maxIters}
# {bar.update(progress)} {progress:.2f}% Done", end="\r")
#     #print(f"{iters+1} / {maxIters}", end="\r")
#     time.sleep(1)
