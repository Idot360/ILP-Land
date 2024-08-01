# ILP-Land-Usage

Optimization target: Happiness (H)

---

Parameters:

Population

Income & Cost of living

Population

Land Size 

Environment

Average work hours

Number of buildings (target) - Recreational & Office & Residential & Necessities 

---

Population and Land Size to be rescaled, and Income and Cost of Living to be combined to reduce the number of parameters

---

General Idea:

Regression fitting the parameters to a function (polynomial regression)

Use basic optimization algorithms to find optimal buildings 

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
```
fmin is for finding minima. To find maxima, find minima of −f(x)
```
