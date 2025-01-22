# Lesson 0 - Basic Concepts

In order to prevent confusion later in the course, we have to start with some fundamentals but we keep this lesson as short as possible. 

# Data and data types

In order to do anything useful in a programming language, we need to process data. When I tell my I am 20. You understand that I am talking about my age (I'm unfortunatly not 20 anymore). Computers however are not smart enough to understand what a piece of data (Like 20 in that sentence) refers to so we have to make sure the program understands what kind of data it's dealing with so for any piece of data, there is an associated type attached to it.

## The Text (String)

one of the most useful types in programming is `String`. It a piece of text and we always have to put it in quotes (single or double) other wise Python gets really confused. for example you can write this:

```python
print("Hello there")
```

Lets break it down.

`print` tells python to display some thing on the screen. then comes `()` to make python understand what needs to be printed. Inside the parentheses we put what ever we want displayed. in this case `"Hello there"` is what we want to print. The presence of `""` tells python where the string starts and when it ends. In you skip the quotes Python gets confused and gives you an error so always make sure to include the quotes for strings.


There are other ways to write string, but we discover that as we go further. For the moment all you need to know is that strings need quotes around them.


## Numbers

Number come in two flavors in Python. `int` or integers are numbers without fractional parts like `5`. `float`s or floating point numbers are numbers with fractions like `5.2` or `3.1415`. we write numbers without any special characters around them in code. so to print `42` and `3.1415` we write.

```python
print(42)
print(3.1415)
```

note that we dont have anything beside the number in side parentheses.

## Lists

Sometime we need to bunch a few things together. Think a few lines of text or a few numbers to add up. For that we use a list. it's pretty easy to define a list.

```python
["Alice", "Bob", "Mark]
[1, 3, 5, 7]
```

the `[]` tells python we want a list. The items inside the list should be separated by `,`. Notice again that all strings are in quotes. We can print the list like:

```python






