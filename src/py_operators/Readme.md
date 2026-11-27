# Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name           | Example         |
| -------- | -------------- | --------------- |
| /        | Division       | x / y           |
| %        | Modulus        | x % y           |
| **       | Exponentiation | x ** y          |
| //       | Floor division | x // y          |
| *        | Mutliplication | x * y           |
| +        | Addition       | x + y           |
| -        | Subtraction    | x - y Examples |

Here is an example using different arithmetic operators:

#### Example

```Python
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
```

### Python has two division operators:

    / - Division (returns a float)
    // - Floor division (returns an integer)

#### Example

Division always returns a float:

```Python
x = 12
y = 5
print(x / y)
```

#### Example

Floor division always returns an integer.

It rounds DOWN to the nearest integer:

```Python

x = 12
y = 5
print(x // y)
```

## Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example       | Same As             |
| -------- | ------------- | ------------------- |
| =        | x = 5         | x = 5               |
| +=       | x += 3        | x = x + 3           |
| -=       | x -= 3        | x = x - 3           |
| *=       | x *= 3        | x = x * 3           |
| /=       | x /= 3        | x = x / 3           |
| %=       | x %= 3        | x = x % 3           |
| //=      | x //= 3       | x = x // 3          |
| **=      | x **= 3       | x = x ** 3          |
| &=       | x &= 3        | x = x & 3           |
| ^=       | x ^= 3        | x = x ^ 3           |
| >>=      | x >>= 3       | x = x >> 3          |
| <<=      | x <<= 3       | x = x << 3          |
| :=       | print(x := 3) | x = 3<br />print(x) |

## Comparison Operators

Comparison operators are used to compare two values:

| Operator | Name                     | Example |
| -------- | ------------------------ | ------- |
| ==       | Equal                    | x == y  |
| !=       | Not equal                | x != y  |
| >        | Greater than             | x > y   |
| <        | Less than                | x < y   |
| >=       | Greater than or equal to | x >= y  |
| <=       | Less than or equal to    | x <= y  |

## Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description                                             | Example               |
| -------- | ------------------------------------------------------- | --------------------- |
| and      | Returns True if both statements are true                | x < 5 and  x < 10     |
| or       | Returns True if one of the statements is true           | x < 5 or x < 4        |
| not      | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

## Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

| Operator              | Name                 | Description                                                                                             | Example                |
| --------------------- | -------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------- |
| &                     | AND                  | Sets each bit to 1 if both bits are 1                                                                   | x & y                  |
| press:shift ( \\ ) | OR                   | Sets each bit to 1 if one of two bits is 1                                                              | x press:shift( \\ ) y |
| ^                     | XOR                  | Sets each bit to 1 if only one of two bits is 1                                                         | x ^ y                  |
| ~                     | NOT                  | Inverts all the bits                                                                                    | ~x                     |
| <<                    | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off                        | x << 2                 |
| >>                    | Signed right shift   | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2                 |


## Precedence Order

The precedence order is described in the table below, starting with the highest precedence at the top:

| Operator                          | Description                                          |
| --------------------------------- | ---------------------------------------------------- |
| ()                                | Parenthese                                           |
| **                                | Exponentiation                                       |
| +x -x ~x                          | unary plus, unary minus, adn bitwise NOT             |
| * / // %                          | Multiplication, division, floor division and modulus |
| + -                               | Addition and suctraction                             |
| <<    >>                        | Bitwise left and right shifts                        |
| &                                 | Bitwise and                                          |
| ^                                 | Bitwise XOR                                          |
| press:shift(\)                    | Bitwise OR                                           |
| == != >= < <= is is not in not in | comparisons, identity, and membership operators      |
| not                               | Logical NOT                                         |
| and                               | AND                                                  |
| or                                | OR                                                   |
