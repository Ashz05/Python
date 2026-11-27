
## Python Numbers

There are three numeric types in Python:

* `int`
* `float`
* `complex`

Variables of numeric types are created when you assign a value to them:

```Python
x = 1 # int
y = 2.8  # float
z = 1j   # complex
```

## Random Number

Python does not have a `random()` function to
make a random number, but Python has a built-in module called
`random` that can be used to make random numbers:

### Example

Import the random module, and display a random number from 1 to 9:

```Python
import random
print(random.randrange(1, 10))
```
