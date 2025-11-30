# pybrl ⠏⠽⠃⠗⠇

Braille (6-dot cell patterns) for Python

## Usage

### Library

```python
import pybrl

print(pybrl.braille("braille for python is cool!"))
# Output: "⠃⠗⠁⠊⠇⠇⠑⠀⠋⠕⠗⠀⠏⠽⠞⠓⠕⠝⠀⠊⠎⠀⠉⠕⠕⠇⠮"

print(pybrl.braille_to_ascii("⠃⠗⠁⠊⠇⠇⠑⠀⠋⠕⠗⠀⠏⠽⠞⠓⠕⠝⠀⠊⠎⠀⠉⠕⠕⠇⠮"))
# Output: "braille for python is cool!"
```

### CLI

Pybrl now includes a command-line interface.

```bash
# Convert ASCII to Braille
pybrl "Hello World"
# Output: ⠓⠑⠇⠇⠕⠀⠺⠕⠗⠇⠙

# Convert Braille to ASCII
pybrl "⠓⠑⠇⠇⠕⠀⠺⠕⠗⠇⠙" --from braille --to ascii
# Output: hello world

# Convert Braille to Hex codes
pybrl "⠁⠃" --from braille --to hex
# Output: ['41', '42']
```

## Conversions

- braille to ascii (function `braille_to_ascii`, alias `ascii`)
- braille to hex (function `braille_to_hex`, alias `hex`)
- braille to dot
- braille to matrix
- ascii to braille
- hex to braille
- dot to braille
- matrix to braille

## Contractions (Grade 2)

Partial support for Grade 2 Braille (contracted braille) has been implemented.
Use the `braille2(string)` function to convert text to Grade 2 Braille.

Currently supported features:
- **Alphabetic Wordsigns**: Single letters representing whole words (e.g., 'b' -> 'but', 'c' -> 'can').
- **Strong Wordsigns**: Common words like 'and', 'the', 'with'.
- **Strong Groupsigns**: Letter groups like 'ch', 'sh', 'ing', 'ed'.
- **Lower Wordsigns**: Words like 'his', 'was', 'were'.
- **Initial-Letter Contractions**: Words/parts like 'day', 'know', 'cannot'.
- **Final-Letter Groupsigns**: Endings like 'tion', 'ness', 'ment'.
- **Shortforms**: Abbreviated words like 'about', 'good', 'braille'.

Example:
```python
print(pybrl.braille2("you and the child"))
# Output: "⠽⠀⠯⠀⠮⠀⠡"

print(pybrl.braille2("braille is good"))
# Output: "⠃⠗⠇⠀⠊⠎⠀⠛⠙"
```

## Symbols mappings

CSV file, that hold basic mapping between Braille symbols, ascii, hex, unicode, dot, matrix, words, meanings and decodings data.

https://github.com/markomanninen/pybrl/blob/master/braille_mappings.csv

## Sources:

https://en.wikipedia.org/wiki/Braille
https://en.wikipedia.org/wiki/Braille_ASCII
https://en.wikipedia.org/wiki/Braille_Patterns

http://www.brailleauthority.org/literary/ebae2002.pdf
http://www.brailleauthority.org/ueb/symbols_list.pdf
http://www.htctu.fhda.edu/trainings/manuals/alt/grade_two_day_2.pdf 

## The MIT License (MIT)

Copyright (c) 2015 Marko Manninen
