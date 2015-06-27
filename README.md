# pybrl ⠏⠽⠃⠗⠇

Braille (6-dot cell patterns) for Python

## Grade 1

	import pybrl

	print pybrl.braille("braille for python is cool!") -> "⠃⠗⠁⠊⠇⠇⠑⠀⠋⠕⠗⠀⠏⠽⠞⠓⠕⠝⠀⠊⠎⠀⠉⠕⠕⠇⠮"

	print pybrl.ascii("⠃⠗⠁⠊⠇⠇⠑⠀⠋⠕⠗⠀⠏⠽⠞⠓⠕⠝⠀⠊⠎⠀⠉⠕⠕⠇⠮") -> "braille for python is cool!"

## Conversions

- braille to ascii
- braille to hex
- braille to dot
- braille to matrix
- ascii to braille
- hex to braille
- dot to braille
- matrix to braille

## Contradictions (Grade 2)

TODO!

## Symbols mappings

CSV file, that hold basic mapping between Braille symbols, ascii, hex, unicode, dot, matrix, words, meanings and decodings data.

https://github.com/markomanninen/pybrl/blob/master/braille_mappings.csv

## IPython notebook demo

https://github.com/markomanninen/pybrl/blob/master/Braille%20for%20Python%20(pybrl).ipynb

Sources:

https://en.wikipedia.org/wiki/Braille
https://en.wikipedia.org/wiki/Braille_ASCII
https://en.wikipedia.org/wiki/Braille_Patterns

http://www.brailleauthority.org/literary/ebae2002.pdf
http://www.brailleauthority.org/ueb/symbols_list.pdf
http://www.htctu.fhda.edu/trainings/manuals/alt/grade_two_day_2.pdf 

## The MIT License (MIT)

Copyright (c) 2015 Marko Manninen