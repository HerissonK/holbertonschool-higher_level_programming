🐍 Understanding Mutability, Memory, and Object Identity in Python

In this blog post, I explore one of the core concepts of Python: how objects are stored in memory, how their mutability affects their behavior, and how Python handles object identity, types, references, and function arguments. These ideas are essential for writing predictable, bug-free Python code and understanding the behavior “under the hood.”

1. Introduction

Python treats values differently depending on whether they are mutable or immutable, and these differences impact memory allocation, how variables refer to objects, how functions receive arguments, and how Python optimizes performance. In this article, I explain all foundational concepts: id, type, mutability, assignment, references, aliasing, memory diagrams, integer preallocation (including NSMALLPOSINTS and NSMALLNEGINTS), and special immutable containers that may contain mutable objects.

2. What Are id and type?

Every Python object has two fundamental properties:

✔ type(obj)

This tells us what kind of object we are dealing with (integer, string, list, etc.).

✔ id(obj)

This returns the memory identity of the object — its address (or a unique identifier representing it).

Example:

x = 10
print(type(x))  # <class 'int'>
print(id(x))    # 140221233514912 (example)


The id shows that x refers to a specific object in memory.

3. Mutable Objects

A mutable object can be changed in place without creating a new object.

Python’s mutable built-ins:

list

dict

set

bytearray

Example:

L = [1, 2]
print(id(L))
L.append(3)
print(L)
print(id(L))  # same id → mutated, not replaced


Memory diagram:

L ──► [1, 2]
        ↑
      same object after modification

4. Immutable Objects

An immutable object cannot be changed after it is created.

Python’s immutable built-ins:

numbers (int, float, complex)

string (str)

tuple

frozenset

bytes

Example:

a = 5
print(id(a))
a = a + 1
print(id(a))  # different id → a new object was created


Memory diagram:

a ──► 5
a ──► 6 (new object)

5. Why It Matters: Assignment vs Referencing

When you write:

x = [1, 2]
y = x


Python does not make a copy.
It creates two names referencing the same object.
This is called aliasing.

x ──► [1, 2] ◄── y


Modifying one modifies both:

y.append(3)
print(x)  # [1, 2, 3]


This behavior applies only to mutable objects.

6. How Immutable Objects Are Stored

Immutable objects must never be changed in place.
Thus, any operation that “modifies” them creates a new memory object.

Example with strings:

s = "hi"
print(id(s))
s += "!"
print(id(s))  # different id


Memory diagram:

s ──► "hi"
s ──► "hi!"

7. Memory Schemas (at least 2 examples)
Example 1: mutable list
names ──► ["Ana", "Bob"]
               ↑
           same list when mutated

Example 2: immutable int
n ──► 10
n ──► 11 (new object)

8. Passing Arguments to Functions (Call-by-Assignment)

Python uses call-by-assignment:

The function receives a reference to the object.

If the object is mutable, the function can change it.

If the object is immutable, the function cannot change the original object.

Mutable example:

def add(L):
    L.append(99)

lst = [1, 2]
add(lst)
print(lst)  # [1, 2, 99]


Immutable example:

def inc(x):
    x += 1

n = 10
inc(n)
print(n)  # still 10

9. Integer Preallocation in CPython

CPython preallocates the first 262 integers at startup.

This means integers from -5 to +256 always exist in memory:

NSMALLNEGINTS = 5   → integers -1 to -5
NSMALLPOSINTS = 257 → integers 0 to 256


These integers are reused because they are extremely common in programs.

Example:

a = 10
b = 10
print(id(a) == id(b))  # True for small integers


This is not true for larger integers:

x = 1000
y = 1000
print(id(x) == id(y))  # Often False

10. Why NSMALLPOSINTS and NSMALLNEGINTS Have These Values

Python designers analyzed usage patterns:
Integers between -5 and 256 appear extremely frequently in loops, indexing, flags, and counters.
Preallocating them:

saves memory

boosts performance

reduces allocation overhead

Thus, these values represent the most commonly used range of integers.

11. Aliases Explained

An alias occurs when multiple variable names refer to the same object.

Example:

A = [1, 2]
B = A


Memory diagram:

A ──► [1, 2] ◄── B


Modifying a mutable object through any alias affects all aliases.

12. Special Case: Tuple and Frozen Set

Even though tuple and frozenset are immutable,
they can contain mutable objects.

Example:

t = ([1, 2], 3)
t[0].append(99)
print(t)  # ([1, 2, 99], 3)


The tuple cannot change its structure (length, order),
but the mutable element inside it can change.

Same for frozenset elements.

13. Conclusion

Understanding mutability, identity, and memory mechanisms in Python is essential for writing efficient and predictable code. Concepts like aliasing, integer caching, assignment vs referencing, and function argument behavior help developers avoid subtle bugs and make better design decisions.