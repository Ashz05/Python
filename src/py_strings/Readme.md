# String

Strings in python are surrounded by either single quotation marks, or double quotation marks.

**'hello'** is the same as **"hello"**.

You can display a string literal with the `print()` function:

### Example

```Python

print("Hello")
print('Hello')
```

## Multiline Strings

You can assign a multiline string to a variable by using three quotes:

### Example

You can use three double quotes:

```Python

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)
```

## Strings are Arrays

Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

### Example

Get the character at position 1 (remember that the first character has the
position 0):

```Python
a = "Hello, World!"
print(a[1])
```

## Slicing

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

### Example

Get the characters from position 2 to position 5 (not included):

```Python

b = "Hello, World!"
print(b[2:5])**
```

## Negative Indexing

Use negative indexes to start the slice from the end of the string:

### Example

Get the characters:

  From: "o" in "World!" (position -5)

  To, but not included: "d" in "World!" (position -2):

```Python

b = "Hello, World!"
print(b[-5:-2])
```

## Escape Characters

Other escape characters used in Python:

| Code | Result          |
| ---- | --------------- |
| \'   | Single Quote    |
| \\   | Backslash       |
| \n   | New Line        |
| \r   | Carriage Return |
| \t   | Tab             |
| \b   | Backspace       |
| \f   | Form Feed       |
| \ooo | Octal value     |
| \xhh | Hex value       |

---

## String Methods:

| Method         | Description                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- |
| capitalize()   | Converts the first character to upper case                                                    |
| casefold()     | Converts string into lower case                                                               |
| center()       | Returns a centered string                                                                      |
| count()        | Returns the number of times a specified value occurs in a string                              |
| encode()       | Returns an encoded version of the string                                                      |
| endswith()     | Returns true if the string ends with the specified value                                      |
| expandtabs()   | Sets the tab size of the string                                                                |
| find()         | Searches the string for a specified value and returns the position of where it was found      |
| format()       | Formats specified values in a string                                                          |
| format_map()   | Formats specified values in a string                                                           |
| index()        | Searches the string for a specified value and returns the position of where it was found      |
| isalnum()      | Returns True if all characters in the string are alphanumeric                                 |
| isalpha()      | Returns True if all characters in the string are in the alphabet                              |
| isascii()      | Returns True if all characters in the string are ascii characters                             |
| isdecimal()    | Returns True if all characters in the string are decimals                                      |
| isdigit()      | Returns True if all haracters in the string are decimals                                      |
| isidentifier() | Returns True if the string is an identifierthe string is an identifier                         |
| islower()      | Returns True if all characters in the string are lower case                                   |
| isnumeric()    | Returns True if all characters in the string are numeric                                      |
| isprintable()  | Returns True if all characters in the string are printable                                    |
| isspace()      | Returns True if all characters in the string are whitespaces                                  |
| istitle()      | Returns True if the string follows the rules of a title                                       |
| isupper()      | Returns True if all characters in the string are upper case                                   |
| join()         | Joins the elements of an iterable to the end of the string                                     |
| ljust()        | Returns a left justified an iterable to the end of the string                                 |
| lower()        | Converts a string into lower case                                                             |
| lstrip()       | Returns a left trim version of the string                                                     |
| maketrans()    | Returns a translation table to be used in translations                                        |
| partition()    | Returns a tuple where the string is parted into three parts                                   |
| replace()      | Returns a string where a specified value is replaced with a specified value                   |
| rfind()        | Searches the string for a specified value and returns the last position of where it was found |
| rindex()       | Searches the string for a specified value and returns the last position of where it was found |
| rjust()        | Returns a right justified version of the string                                               |
| rpartition()   | Returns a tuple where the string is parted into three parts                                   |
| rsplit()       | Splits the string at the specified separator, and returns a list                              |
| rstrip()       | Returns a right trimversion of the string                                                      |
| split()        | Splits the string at the specified separator, and returns a list                              |
| splitlines()   | Splits the stringat line breaks and returns a list                                             |
| startswith()   | Returns true if the string starts with the specified value                                    |
| str[i]()p()     | Returns a trimmed version of the string                                                        |
| swapcase()     | Swaps cases, lower case becomes upper case and vice versa                                     |
| title()        | Converts the first character of each word to upper case                                       |
| translate()    | Returns a translated string                                                                   |
| upper()        | Converts a string version of the string                                                       |
| zfill()        | Fills the string with version of the string                                                   |
