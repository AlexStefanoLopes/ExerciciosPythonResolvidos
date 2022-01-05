>>> biomoleculas = ('proteína', 'ácidos', 'carboidrato', 'lipidio', 'proteína', 'ácidos')
>>> print(biomoleculas)
('proteína', 'ácidos', 'carboidrato', 'lipidio', 'proteína', 'ácidos')
>>> print(set(biomoleculas))
{'ácidos', 'lipidio', 'carboidrato', 'proteína'}
>>> c1 = {1,2,3,4,5}
>>> c2 = {3,4,5,6,7}
>>> c3 = c1.intersection{c2}
SyntaxError: invalid syntax
>>> print(c3)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(c3)
NameError: name 'c3' is not defined
>>> c3 = c1.intersection(c2)
>>> print(c3)
{3, 4, 5}
>>> c1.difference(c2)
{1, 2}
>>> c2.difference(c1)
{6, 7}
>>>