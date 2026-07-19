from give_bmi import give_bmi, apply_limit

# height = None
# height = [2.71, 1.15, 1.71, 3]
# height = [2.71, 1.15, "hello"]
height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
# bmi = None
# limit = "hoge"
limit = 26
# limit = None
print(apply_limit(bmi, limit))
