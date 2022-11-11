from simplex import SimplexSolver

min_or_max = input("Choose min or max: ")
while min_or_max not in ("min", "max"):
    min_or_max = input("Choose min or max: ")

if min_or_max == "max":
    constrains = [[2, 1, 5, 0, 3], [0, 2, 0, 0, 0], [0, 0, 2, 1, 0], [7, 0, 0, 2, 1], [0, 2, 10, 0, 1]]
    b = [100, 80, 85, 200, 100]
    expression = [32, 30, 35, 30, 20]
    SimplexSolver().run_simplex(constrains, b, expression, prob=min_or_max, enable_msg=False, latex=True)

else:
    constrains = [[18, 0, 23, 83.5, 1], [37, 52, 0, 0, 0], [21, 52, 23, 41.75, 1], [75, 0, 0, 0, 1],
                  [0, 0, 23, 41.75, 0]]
    b = [500, 360, 400, 300, 300]
    expression = [150, 104, 69, 167, 1]
    SimplexSolver().run_simplex(constrains, b, expression, prob=min_or_max, enable_msg=False, latex=True)
