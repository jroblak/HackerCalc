import click
import binascii

OPS = ['ROR', 'ROL', 'XOR', '+', '-', 'ADD', 'SUB', '>>', '<<', 'SHL', 'SHR']
SIZE = 8

def unint(a, b):
    if b == 16:
        return hex(a)
    elif b == 2:
        return bin(a)
    else:
        return a

#todo: make this more robust
def intify(item, b):
    return int(item, b)

def shr(a, b):
    return a >> b

def shl(a, b):
    return a << b

def rol(a, b):
    res = (a << b % SIZE) & (2 ** SIZE - 1) | ((a & (2 ** SIZE - 1)) >> (SIZE - (b % SIZE)))
    return res

def ror(a, b):
    res = ((a & (2 ** SIZE - 1)) >> (b % SIZE)) | (a << (SIZE - (b % SIZE)) & (2 ** SIZE - 1))
    return res

def xor(a, b):
    return a ^ b

def add(a, b):
    res = a + b

    if res >= (2 ** SIZE - 1):
        res = res - (2 ** SIZE)

    return res

def sub(a, b):
    res = a - b
    if res < 0:
        res = res + (2 ** SIZE)

    return res

def calc(a, op, b):
    return {
        'ROR': ror,
        'ROL': rol,
        'XOR': xor,
        '+': add,
        'ADD': add,
        '-': sub,
        'SUB': sub,
        'SHR': shr,
        '>>': shr,
        'SHL': shl,
        '<<': shl
    }[op](a, b)

def parse(txt, base):
    stack = []

    for item in txt:
        if item.upper() in OPS:
            stack.append(item)
        else:
            stack.append(intify(item, base))

        if (len(stack) == 3):
            b = stack.pop()
            op = stack.pop().upper()
            a = stack.pop()
            res = calc(a, op, b)
            stack.append(res)

    return unint(stack.pop(), base)

@click.command()
@click.option('--wordsize', default=8, help='Size of data being calculated (default: 8)')
@click.option('--base', default=16, help='Format of data being calculated (default: 16 (hex))')
@click.option('--ascii/--no-ascii', default=False, help='Print result as ASCII (default: False)')
@click.argument('calculation', nargs=-1)

def calculator(wordsize, base, calculation, ascii):
    SIZE = wordsize
    res = parse(calculation, base)
    
    if ascii:
        res = str(chr(int(res, base)))
        
    try:
        click.echo('result: ' + res)
    except:
        click.echo('Result doesn\'t decode to ASCII!')

if __name__ == '__main__':
    calculator()