# magichacks

## Usage

At the beginning of your notebook

```python
execfile("cca_editing_library.py")
_sw = "DEV+CONTENT" 
```

the switch variable can be named whatever you want which will not be overwritten (here `_sw`), for the mode choice see below.

* `"CONTENT"` : only writes the content of the cell apart from the `#<cca>` and `#</cca>` tags
* `"STUDENT"` : only writes the content of the cell that is between the `#<cca>` and `#</cca>` tags
* `"DEV+CONTENT"` : same as `"CONTENT"` but also executes the cell in current notebook
* (anything else): executes the cell normally

A cell of interest would then be written

```python
%%write2file scripts/blah.py _sw

#<cca>
# How would you compute the first five powers of
a = 5
#</cca>

f = lambda v: [v**i for i in range(0,5)]
print(f(a))
```

this will create (or overwrite) the file `blah.py`:

```python

# How would you compute the first five powers of
a = 5

f = lambda v: [v**i for i in range(0,5)]
print(f(a))
```

had the switch been to `"STUDENT"`

```python
# How would you compute the first five powers of
a = 5
```

*Notes*:

* *absence of quotes* around the path, relative paths are fine.
* whitespaces between the magic line and the start of the code will not be included in asciidoc so don't worry about it.


## Within asciidoc

```asciidoc
[source,python]
----
include::../scripts/blah.py[]
----
```

and you don't have to worry anymore about changing the cell content.

## Remarks and warnings

This is a basic hack, if you want to improve it, feel free. Do not expect it to be robust or whatever if you don't use it within the constrained guidelines above.



