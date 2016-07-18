# a\_bad\_idea

\#langs for Python.

## Installation

No.

## Usage

You want to add a custom parser to Python?
Sure you can.

```python
from a_bad_idea import add_implementation

add_implementation("mylanguage", my_language_fun)
```

The loaded module will then have a `value` property that
you can read out. Because that is not hacky at all.

For an example, look at [the JSON example](https://github.com/hellerve/a_bad_idea/blob/master/examples/json_lang.py).

<hr/>

Have fun!
