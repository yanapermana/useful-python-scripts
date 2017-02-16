# -*- coding: utf-8 -*-
"""
Python’s tuples are a simple data structure 
for grouping arbitrary objects. Tuples are 
also immutable—they cannot be modified once 
they’ve been created.
"""

tup = ('hello', object(), 42)
print tup
print tup[2]

# tup[2] = 23
# Assignment have error,
# (TypeError: 'tuple' object does not support item assignment)

"""
A downside of plain tuples is that the 
data you store in them can only be pulled 
out by accessing it through integer indexes. 

You can’t give names to individual properties 
stored in a tuple. This can impact code 
readability.

Also, a tuple is always an ad-hoc structure. 
It’s hard to ensure that two tuples have the 
same number of fields and the same properties 
stored on them. This makes it easy to 
introduce “slip-of-the-mind” bugs by mixing   <= Here we go {:
up the field order.
"""

"""
# Namedtuples to the Rescue
Namedtuples aim to solve these two problems.

First of all, namedtuples are immutable just 
like regular tuples. Once you store something 
in them you can’t modify it.

Besides that, namedtuples are, well ... 
named tuples. Each object stored in them can 
be accessed through a unique (human-readable) 
identifier. This frees you from having to 
remember integer indexes, or resorting to 
workarounds like defining integer constants 
as mnemonics for your indexes.

Here’s what a namedtuple looks like:
"""

from collections import namedtuple
Car = namedtuple('Car','color mileage')

"""
To use namedtuples you need to import the 
collections module. They were added to the 
standard library in Python 2.6. In the 
above example we defined a simple “Car” 
data type with two fields: “color” and 
“mileage”.

You might find the syntax a little weird 
here—Why are we passing the fields as a 
string encoding them "color mileage"?

The answer is that namedtuple’s factory 
function calls split() on the field names 
string, so this is really just a shorthand 
to say the following:
"""

print 'color mileage'.split()
Car = namedtuple('Car',['color','mileage'])

"""
Of course you can also pass a list with 
string field names directly if you prefer how 
that looks. The advantage of using a proper 
list is that it’s easier to reformat this 
code if you need to split it across multiple 
lines:
"""

Car = namedtuple('Car',[
	'color',
	'mileage'
	])

"""
However you decide, you can now create new “car”
objects with the Car factory function. It behaves
as if you had defined a Car class manually and 
given it a constructor accepting a “color” and a 
“mileage” value:
"""

my_car = Car('red',3812.4)
print my_car.color
print my_car.mileage

"""
Tuple unpacking and the *-operator for function 
argument unpacking also work as expected:
"""

color, mileage = my_car
print(color, mileage)
print(*my_car)

# To be continued

# https://dbader.org/blog/writing-clean-python-with-namedtuples#.
