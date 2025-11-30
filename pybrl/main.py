#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# file: main.py
import argparse
import sys

# u2800 - u283F
unibase = ['280', '281', '282', '283']
uniend = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
# Python 3 uses chr() instead of unichr()
ordered_unicodes = [chr(int(''.join(['0x', j, i]),0)) for j in unibase for i in uniend]

# 64 symbols
brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
            '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
            '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

# corresponding unicodes for Braille symbols
unicodes = ['\u2800','\u282e','\u2810','\u283c','\u282b','\u2829','\u282f','\u2804',
            '\u2837','\u283e','\u2821','\u282c','\u2820','\u2824','\u2828','\u280c',
            '\u2834','\u2802','\u2806','\u2812','\u2832','\u2822','\u2816','\u2836',
            '\u2826','\u2814','\u2831','\u2830','\u2823','\u283f','\u281c','\u2839',
            '\u2808','\u2801','\u2803','\u2809','\u2819','\u2811','\u280b','\u281b',
            '\u2813','\u280a','\u281a','\u2805','\u2807','\u280d','\u281d','\u2815',
            '\u280f','\u281f','\u2817','\u280e','\u281e','\u2825','\u2827','\u283a',
            '\u282d','\u283d','\u2835','\u282a','\u2833','\u283b','\u2818','\u2838']


# corresponding bitwise matrix for Braille symbols
matrixcodes = [
    [[0, 0], [0, 0], [0, 0]],[[0, 1], [1, 0], [1, 1]],[[0, 0], [0, 1], [0, 0]],[[0, 1], [0, 1], [1, 1]],
    [[1, 1], [1, 0], [0, 1]],[[1, 1], [0, 0], [0, 1]],[[1, 1], [1, 0], [1, 1]],[[0, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 1], [1, 1]],[[0, 1], [1, 1], [1, 1]],[[1, 0], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 1]],
    [[0, 0], [0, 0], [0, 1]],[[0, 0], [0, 0], [1, 1]],[[0, 1], [0, 0], [0, 1]],[[0, 1], [0, 0], [1, 0]],
    [[0, 0], [0, 1], [1, 1]],[[0, 0], [1, 0], [0, 0]],[[0, 0], [1, 0], [1, 0]],[[0, 0], [1, 1], [0, 0]],
    [[0, 0], [1, 1], [0, 1]],[[0, 0], [1, 0], [0, 1]],[[0, 0], [1, 1], [1, 0]],[[0, 0], [1, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],[[0, 0], [0, 1], [1, 0]],[[1, 0], [0, 1], [0, 1]],[[0, 0], [0, 1], [0, 1]],
    [[1, 0], [1, 0], [0, 1]],[[1, 1], [1, 1], [1, 1]],[[0, 1], [0, 1], [1, 0]],[[1, 1], [0, 1], [0, 1]],
    [[0, 1], [0, 0], [0, 0]],[[1, 0], [0, 0], [0, 0]],[[1, 0], [1, 0], [0, 0]],[[1, 1], [0, 0], [0, 0]],
    [[1, 1], [0, 1], [0, 0]],[[1, 0], [0, 1], [0, 0]],[[1, 1], [1, 0], [0, 0]],[[1, 1], [1, 1], [0, 0]],
    [[1, 0], [1, 1], [0, 0]],[[0, 1], [1, 0], [0, 0]],[[0, 1], [1, 1], [0, 0]],[[1, 0], [0, 0], [1, 0]],
    [[1, 0], [1, 0], [1, 0]],[[1, 1], [0, 0], [1, 0]],[[1, 1], [0, 1], [1, 0]],[[1, 0], [0, 1], [1, 0]],
    [[1, 1], [1, 0], [1, 0]],[[1, 1], [1, 1], [1, 0]],[[1, 0], [1, 1], [1, 0]],[[0, 1], [1, 0], [1, 0]],
    [[0, 1], [1, 1], [1, 0]],[[1, 0], [0, 0], [1, 1]],[[1, 0], [1, 0], [1, 1]],[[0, 1], [1, 1], [0, 1]],
    [[1, 1], [0, 0], [1, 1]],[[1, 1], [0, 1], [1, 1]],[[1, 0], [0, 1], [1, 1]],[[0, 1], [1, 0], [0, 1]],
    [[1, 0], [1, 1], [0, 1]],[[1, 1], [1, 1], [0, 1]],[[0, 1], [0, 1], [0, 0]],[[0, 1], [0, 1], [0, 1]]
]

# corresponding hexcodes for Braille symbols
hexbase  = ['2', '3', '4', '5']
hexend   = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
hexcodes = [''.join([j, i]) for j in hexbase for i in hexend]

# corresponding ascii codes for Braille symbols
asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
              '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
              'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
              'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

# corresponding dotcodes for Braille symbols
dotcodes = ['','2-3-4-6','5','3-4-5-6','1-2-4-6','1-4-6','1-2-3-4-6','3','1-2-3-5-6','2-3-4-5-6','1-6','3-4-6','6','3-6','4-6',
            '3-4','3-5-6','2','2-3','2-5','2-5-6','2-6','2-3-5','2-3-5-6','2-3-6','3-5','1-5-6','5-6','1-2-6','1-2-3-4-5-6',
            '3-4-5','1-4-5-6','4','1','1-2','1-4','1-4-5','1-5','1-2-4','1-2-4-5','1-2-5','2-4','2-4-5','1-3','1-2-3','1-3-4',
            '1-3-4-5','1-3-5','1-2-3-4','1-2-3-4-5','1-2-3-5','2-3-4','2-3-4-5','1-3-6','1-2-3-6','2-4-5-6','1-3-4-6','1-3-4-5-6',
            '1-3-5-6','2-4-6','1-2-5-6','1-2-4-5-6','4-5','4-5-6']

# corresponding letter/word combinations for Braille symbols
meanings = ['(space)','the','(contraction)','(number prefix)','ed','sh','and','(undefined)','of','with','ch','ing','(uppercase prefix)','-',
            '(italic prefix)','st','”',',',';',':','.','en','!','( or )','“ or ?','in','wh','(letter prefix)','gh','for','ar','th',
            '(accent prefix)','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'ow','ou','er','(currency prefix)','(contraction)']

# corresponding word combinations for Braille symbols
words = ['','THE','','','','SHALL','AND','','OF','WITH','CHILD','ING','','','','STILL','WAS','','BE','','','ENOUGH','TO','WERE','HIS',
         'IN','WHICH','','','FOR','','THIS','','','BUT','CAN','DO','EVERY','FROM','GO','HAVE','','JUST','KNOWLEDGE','LIKE','MORE','NOT',
         '','PEOPLE','QUITE','RATHER','SO','THAT','US','VERY','WILL','IT','YOU','AS','','OUT','','','']

# todo: decoded strings of possible translations of Braille symbols
# this can be improved for more robust and clever way to translating 
# grade 2 Braille input to human eye readable sentences
decodings = ['SPACE/empty','THE/5-there/4-5-these/4-5-6-their','5-','ble/#','ed','sh/SHALL','AND','3-','OF','WITH','ch/CHILD/5-character',
             'ing','6-','com/-','4-6-','st/STILL','was/BY/”','ea/,','be/bb/;','con/cc/:','dis/dd/.','en/ENOUGH','to/ff/!','were/gg/()',
             'his/?/“','in','wh/WHICH/5-where/4-5-whose','5-6-','gh/RELEASE CAPS/<','FOR/full','ar','th/THIS/5-through/4-5-those','´/@',
             'a/1','b/BUT/2','c/CAN/4-5-6-cannot/3','d/DO/5-day/4-6-ound/4','e/EVERY/5-ever/4-6-ance/5-6-ence/5','f/FROM/5-father/6',
             'g/GO/5-6-ong/7','h/HAVE/5-here/4-5-6-had/8','i/9','j/JUST/0','k/KNOWLEDGE/5-know','l/LIKE/5-lord/5-6-ful/RELEASE',
             'm/MORE/5-mother/4-5-6-many','n/NOT/5-name/4-6-sion/5-6-tion/6-ation','o/5-one','p/PEOPLE/5-part','q/QUITE/5-question',
             'r/RATHER/5-right','s/SO/5-some/4-5-6-spirit/4-6-less/5-6-ness','t/THAT/5-time/4-6-ount/5-6-ment','u/US/5-under/4-5-upon',
             'v/VERY','w/WILL/5-work/4-5-word/4-5-6-world','x/IT','y/YOU/5-young/5-6-ity/6-ally/','z/AS','ow','ou/OUT/5-ought','er',
             '4-5- ','4-5-6-']

# Create dictionaries for O(1) lookups
def _create_mapping(keys, values):
    return {k: v for k, v in zip(keys, values)}

ascii_to_braille_map = _create_mapping(asciicodes, brailles)
braille_to_ascii_map = _create_mapping(brailles, asciicodes)
braille_to_matrix_map = _create_mapping(brailles, matrixcodes)
matrix_to_braille_map = {tuple(tuple(r) for r in m): b for m, b in zip(matrixcodes, brailles)}
braille_to_hex_map = _create_mapping(brailles, hexcodes)
hex_to_braille_map = _create_mapping(hexcodes, brailles)
braille_to_dot_map = _create_mapping(brailles, dotcodes)
dot_to_braille_map = _create_mapping(dotcodes, brailles)

def convert(string, toNotation, fromNotation):
    # This remains for backward compatibility or generic use, but optimized where possible
    # if both are hashable, we could build a map on the fly or use existing ones
    # But for now, let's keep the logic but remove decode('utf-8')
    # And improve efficiency by building a temp map if len(string) is large?
    # For now, just fixing the decode issue.
    # The original implementation was:
    # return [toNotation[fromNotation.index(d)] for c in string.decode('utf-8') for d in fromNotation if c == d.decode('utf-8')]

    # New implementation:
    # This logic was essentially: find c in fromNotation, map to toNotation.
    # It assumes 1-to-1 mapping.

    res = []
    # Create a lookup map for faster access
    # Note: toNotation and fromNotation must be aligned
    lookup = dict(zip(fromNotation, toNotation))

    for c in string:
        if c in lookup:
            res.append(lookup[c])
        # Original code didn't append anything if not found.
    return res

# ascii to braille. currently supporting grade 1 conversion only
def braille(string):
    # Optimized using dictionary
    return ''.join([ascii_to_braille_map.get(c, '') for c in string])

def braille2(string):
    return "Grade 2 conversion not supported yet. you should use convert function to find out translation possibilities for Grade 2."

# braille to ascii
def ascii(string):
    return ''.join([braille_to_ascii_map.get(c, '') for c in string])

# braille to matrix
def matrix(string):
    return [braille_to_matrix_map.get(c, None) for c in string if c in braille_to_matrix_map]

# braille to hex
def hex(string):
    return [braille_to_hex_map.get(c, '') for c in string if c in braille_to_hex_map]

# braille to dot
def dot(string):
    return [braille_to_dot_map.get(c, '') for c in string if c in braille_to_dot_map]

# helper function for n2braille
def convert_list(arr, toNotation, fromNotation):
    lookup = dict(zip(fromNotation, toNotation))
    return [lookup.get(c) for c in arr if c in lookup]

# matrix to braille
def matrix2braille(arr):
    # arr is a list of matrices (lists of lists)
    # Lists are not hashable, so we need to convert to tuple of tuples for lookup
    result = []
    for m in arr:
        # Check if m is a list of lists and convert to tuple of tuples
        if isinstance(m, list):
            key = tuple(tuple(r) for r in m)
        else:
            key = m
        if key in matrix_to_braille_map:
            result.append(matrix_to_braille_map[key])
    return ''.join(result)

# hex to braille
def hex2braille(arr):
    return ''.join([hex_to_braille_map.get(c, '') for c in arr])

# dot to braille
def dot2braille(arr):
    return ''.join([dot_to_braille_map.get(c, '') for c in arr])


def cli():
    parser = argparse.ArgumentParser(description="Braille for Python (pybrl) - Conversion Tool")
    parser.add_argument("input", help="Input string or data to convert")
    parser.add_argument("--to", dest="to_type", choices=['braille', 'ascii', 'hex', 'dot', 'matrix'], default='braille', help="Target format")
    parser.add_argument("--from", dest="from_type", choices=['ascii', 'braille', 'hex', 'dot', 'matrix'], default='ascii', help="Source format")

    args = parser.parse_args()

    input_data = args.input

    # Handle input data parsing for list-based inputs (hex, dot, matrix)
    # This is a simple CLI, handling complex structures like matrix via CLI arg is hard.
    # We will assume comma separated values for hex and dot if source is not ascii/braille?
    # Or just keep it simple for now.

    if args.from_type == 'ascii' and args.to_type == 'braille':
        print(braille(input_data))
    elif args.from_type == 'braille' and args.to_type == 'ascii':
        print(ascii(input_data))
    elif args.from_type == 'braille' and args.to_type == 'hex':
        print(hex(input_data))
    elif args.from_type == 'braille' and args.to_type == 'dot':
        print(dot(input_data))
    elif args.from_type == 'braille' and args.to_type == 'matrix':
        print(matrix(input_data))
    elif args.from_type == 'hex' and args.to_type == 'braille':
         # Assume input is comma separated hex codes
         arr = input_data.split(',')
         print(hex2braille(arr))
    elif args.from_type == 'dot' and args.to_type == 'braille':
         arr = input_data.split(',')
         print(dot2braille(arr))
    # Matrix input via CLI is tricky, skipping for now or user can pass JSON string?
    # sticking to basic requirements.
    else:
        print(f"Conversion from {args.from_type} to {args.to_type} not directly supported in CLI yet.")

if __name__ == "__main__":
    cli()
