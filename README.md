# Simplex Solver

Example code for solving linear equations using simplex.

- Provides step-by-step instrucitons for solving LPs using simplex algorithm (tableau method).
- Outputs raw LaTeX file.

LaTeX files can be compiled [here].

Note: Currently, only LPs in standard form are supported.

### Examples

###### 1. Standard Form Maximization LP

Consider the following objective function and constraints:
F = 32x1 + 30x2 + 35x3 +30x4 +20x5

2x1 + x2 + 5x3 + 3x5 <= 100
2x2 <= 80
2x3 + x4 <= 85
7x1 + 2x4 + x5 <= 200
2x2 + 10x3 + x5 <= 100

This problem can be solved by running the script with the following parameters:

```sh
$ python run.py
```

###### 2. Standard Form Minimization LP

Consider the following objective function and constraints:
F = 150x1 + 104x2 + 69x3 +167x4 + 1x5

18x1 + 23x3 + 83.5x3 + x5 >= 500
37x1 + 52x2 >= 360
27x1 + 52x2 +23x3 + 41.75x4 + x5 >= 400
75x1 + x5 >= 300
23x3 + 41.75x4 >= 300

This problem can be solved by running the script with the following parameters:

```sh
$ python run.py
```


[here]: <https://latexbase.com/>

