# Gencode

A library for defining classes based on their pseudo-genetic structure, rather than their evolutionary hierarchy. 

---

### What have you done, and why?

I noticed that there are a lot of similarities between evolution and software systems architecture. Particularly, we model the hierarchy of a system like we do the tree of life! Classes extend other classes, make little changes, and gradually evolve. 

However, the actual components of some classes might be the same. Infact, you might find yourself with classes and methods that are entirely interchanges as the sofware system becomes larger and larger; then, similar code must be rewritten many times, often to the same effect. This means we're more likely to make mistakes, because we can't write good code every time, and we're likely to end up with a much larger codebase than is necessary. 

---

### How does gencode fix this, then?

A gene defines a small part of molecular "functionality": it's an expression of instructions for how a cell or organism should *do* something. 

This is also true of functions in software systems! They're literally just a set of instructions that tell us how to do something. That concept seems a little functional in nature -- borrowing the notion that a function does a specific, well-defined job and is stateless -- but Gencode does this with classes, and adds the states inherant in object oriented systems. 

Particularly, gencode will take a list of methods as the 'genes' of the class. That way, we can save collections of genes and create new or different classes based on the 'genetic' encoding of the class. 

---

### That's madness. How do you use it, anyway?!

Pretty easy. The provided module, `gencode`, contains a function, also called `gencode`. Give it the namespace you want the class to reside within (usually just `globals()` for the main namespace), the name of the class as a string, and as many function objects as you want to be methods of the generated class. 

Note that those methods WILL be class methods, so they'll want to start with `self` in their argument list!

Here's a minimum working example: 

```python 
  >>> import gencode 
  >>> def m(self, n):
  ...   print n
  ...
  >>> gencode.gencode(globals(), 'C', m)
  >>> test_var = C()
  >>> test_var.m(5)
  5
```
