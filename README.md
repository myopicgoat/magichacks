# magichacks

## Idea

* Write your ipython notebook with a few extra commands indicating what you want to output to students.
* Have the content of the cells you want to show in the asciidoc by synchronized directly
* Generate a boilerplate notebook for the students

all of this using only one notebook and a few scripts.

## Notebook>Asciidoc

### Usage

At the beginning of your notebook (both Py2 and Py3)

```python
with open("cca_editing_library.py") as f:
    exec(f.read())
_sw = "DEV+CONTENT"
```

the switch variable can be named whatever you want which will not be overwritten (here `_sw`), for the mode choice see below.

* `"CONTENT"` : only writes the content of the cell apart from the `#<cca>` and `#</cca>` tags
* `"STUDENT"` : only writes the content of the cell that is outside of the `#<cca>` and `#</cca>` tags
* add `"DEV+"` before either and the cell is also executed (e.g., `"DEV+CONTENT"`)
* (anything else): executes the cell normally

A cell of interest would then be written

```python
%%write2file scripts/example0.py _sw

# How would you compute the first five powers of
a = 5

# Your solution here ...

#<cca>
f = lambda v: [v**i for i in range(0,5)]
print(f(a))
#</cca>

print("well done")
```

this will create (or overwrite) the file `example0.py`:

```python

# How would you compute the first five powers of
a = 5

# Your solution here ...

f = lambda v: [v**i for i in range(0,5)]
print(f(a))

print("well done")
```

had the switch been to `"STUDENT"`

```python

# How would you compute the first five powers of
a = 5

# Your solution here ...


print("well done")
```

*Notes*:

* *absence of quotes* around the path, relative paths are fine.
* whitespaces between the magic line and the start of the code will not be included in asciidoc so don't worry about it.


### Within asciidoc

```asciidoc
[source,python]
----
include::../scripts/example0.py[]
----
```

and you don't have to worry anymore about changing the cell content.

## Notebook>Notebook

(this hasn't been tested extensively and it's not a clean way of doing it)

This converts your notebook to a secondary notebook discarding everything that is between the `#<cca>` and `#</cca>` tags.

For example:

```bash
python cca_convert.py mainNotebook.ipynb
```

(try it and then open the corresponding `mainNotebook_template.ipynb`)

## Remarks and warnings

This is a basic hack, if you want to improve it, feel free. Do not expect it to be robust or whatever if you don't use it within the constrained guidelines above.

If you want entire cells to be escaped with `#<cca>` `#</cca>` they are currently written as blank cells in the converted notebook so at the moment these have to be removed manually (in the future I will hack some more to remove those with some dirty regex)
