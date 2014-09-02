import click
import binascii

OPS = ['ROR', 'ROL', 'XOR', '^', '+', '-', 'ADD', 'SUB', '>>', '<<', 'SHL', 'SHR']
SIZE = 8

def unint(a, b):
    if b == 16:
        return hex(a)
    elif b == 2:
        return bin(a)
    else:
        return a

def intify(item, b):
    ret = 0

    if len(item) > 1 and item[1] in ['x', 'b']:
            ret = int(item[2:], b)
    else:
        ret = int(item, b)

    return ret

def shr(a, b):
    return a >> b

def shl(a, b):
    return a << b

def rol(a, b, w):
    res = (a << count | a >> (8 - b)) & 0xFF
    return res

def ror(a, b, w):
    res = (a >> count | a << (8 - b)) & 0xFF
    return res

def xor(a, b):
    return a ^ b

def add(a, b):
    res = a + b
    if res >= ((2 ** SIZE) - 1):
        res = res - ((2 ** SIZE) - 1)

    return res

def sub(a, b):
    res = a - b
    if res < 0:
        res = res + (2 ** SIZE) - 1

    return res

def calc(a, op, b):
    return {
        'ROR': ror,
        'ROL': rol,
        'XOR': xor,
        '^': xor,
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
    
    for item in txt.split(' '):
        if item.upper() in OPS:
            stack.append(item)
        else:
            stack.append(intify(item, base))

        if (len(stack) == 3):
            b = stack.pop()
            op = stack.pop()
            a = stack.pop()
            res = calc(a, op, b)
            stack.append(res)

    return unint(stack.pop(), base)

@click.command()
@click.option('--wordsize', default=8, help='Size of data being calculated (default: 8)')
@click.option('--base', default=16, help='Format of data being calculated (default: 16 (hex))')
@click.argument('calculation')

def calculator(wordsize, base, calculation):
    SIZE = wordsize
    click.echo(parse(calculation, base))

if __name__ == '__main__':
    calculator()