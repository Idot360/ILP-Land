# ILP-Land-Usage

Optimization target: Happiness (H)

Additional minimization target: Cost (C)

---

function(F)

measured(M)

---

Parameters:

Affordability (F) - Income & Cost of living (M)

Population (M)

Land Size (M)

Average work hours (M)

Government style (M)

Government corruption (M)

Environment (F)

Number of buildings (F, target) - total & recreational & Office & Residential & Necessities (M)

---

General Idea:

Regression fitting the parameters to a function (record variance)

Use basic optimization algorithms to find optimal buildings 

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
```
fmin is for finding minima. We can use it to find maxima though, but finding the minima of −f(x)
```

account for variance by using a random matrix with set mean and s.d. (basically a simulation)
```
Use numpy.random.normal to general coefficients for the parameters; then multiply each of the coefficients before optimizing
```
