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

note that we don't have anything beside the number in side parentheses.

## Lists

Sometime we need to bunch a few things together. Think a few lines of text or a few numbers to add up. For that we use a list. it's pretty easy to define a list.

```python
["Alice", "Bob", "Mark"]
[1, 3, 5, 7]
```

the `[]` tells python we want a list. The items inside the list should be separated by `,`. Notice again that all strings are in quotes. We can print the list like:

```python
print(["Alice", "Bob", "Mark"])
print([1, 3, 5, 7])
```

You can put as much whitespace as you like between items in the list. Python does not case about whitespace.


There is a type in Python that confuses the beginners because it looks kinda like a list. it's called a `tuple` and is written with `()` instead of `[]` like so:

```python
(1,2,3)
```

It's like a list in that it can contain a few things. It differs with a list in that a list is a dynamic type meaning that it's like a box where we can put thing in and pull them out when we want. A tuple is like gluing things together. Once you create one you can't change it anymore.

## Maps or Dictionaries

On last type we will discuss right now is a map. Also known as a dictionary. This one is like a list with one different. Each Item in the list can have a name that we pick (Like a dictionary where each word is *mapped* to a definition.)

Later we would see why this type is very useful but for the moment just see how we create a map.

```python
{
    "Alice" : "1 212 55 691",
    "Bob"   : "1 212 99 951",
    "Mike"  : "1 212 12 341",
}
```

This is a simple phone book. the `{}` tells Python we want to define a map. then comes the *key* or the name we want to give an item. After that you have the `:` that tells python the next thing is the value assigned to that *key*. We have to separate `key : value` pairs with `,` like we did for the list. Both key and value in this example are Strings that represent names and phone numbers. 

We could have used the number type for phone number like `121255691` but we can not put any whitespace in the middle of a number (That would confuse Python) so we used text (or `String`) instead.

# Objects

You or any other programmer can create almost any type you like using these few fundamental types. For Example if you want to define a shape for your game, you could write something like this


```python
class MyCuteShape:
    def __init__(self):
        self.geometry = "circle"
        self.border_color = "red"
        self.fill_color = "blue"
```

We don't care about all the details right now but let's figure out the interesting parts.

the first line 

```python
class MyCuteShape:
```

tells python we want to make our own type. python knows it's a type because it starts with the word `class`. then `MyCuteShape` is a name I have chosen for my type. You can name your types almost anything you like (there are a few rules like it should not start with a number). The `:` tells python that the class has a *body*. the *body* is a bunch of code that goes inside the class. We say that the rest of the code for our type is nested. It should always start with a tab like so.


```python
class MyRocket:
<TAB>WHAT EVER SHOULD GO INSIDE 
```

if you don't put the tab. Python gets really mad at you. we figure that out in details later.
we don't care about `def __init__(self):` right now. just know that it's a bunch of code that has it's own body so whatever goes inside it now needs two tabs. then comes.


```
<TAB><TAB>self.geometry = "circle"
<TAB><TAB>self.border_color = "red"
<TAB><TAB>self.fill_color = "blue"
```

`<TAB><TAB>` is added for emphasis. the next lines tell Python that your type has `geometry` and `border_color` and `fill_color` with some values which themselves are strings. 

When you hear about objects. We are talking about this custom types we (or some other programmer) has created. We define them using the keyword `class` but we call them `object`s.


That's it.You are ready to jump head first into this adventure.













