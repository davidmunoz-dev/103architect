import sys
import math

def matmult(a, b):
    zip_b = zip(*b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
             for col_b in zip_b] for row_a in a]

def t(x, y, a, b):
    x += a
    y += b
    print ('Translation by the vector (' + "%.0f" % a + ',' + "%.0f" % b + ')')
    print ('1 0 ' + "%.0f" % a)
    print ('0 1 ' + "%.0f" % b)
    print ('0 0 1')
    return x, y

def s(x, y, a):
    xs = x
    ys = y
    if a % 90 != 0:
        x = (math.cos(2 * a) * xs) + (math.sin(2 * a) * ys)
        y = (math.sin(2 * a) * xs) - (math.cos(2 * a) * ys)
        x1 = math.cos(2 * a)
        x2 = math.sin(2 * a)
        y1 = math.sin(2 * a)
        y2 = -math.cos(2 * a)
    elif a % 180 == 0:
        y *= -1
        x1 = 1
        x2 = 0
        y1 = 0
        y2 = -1
    elif a % 180 == 90:
        x *= -1
        x1 = -1
        x2 = 0
        y1 = 0
        y2 = 1
    print ('Symmetry about an axis inclined with an angle at a ' +      \
           str(a) + ' degree')
    print ("%.0f" % x1 + ' ' + "%.0f" % x2 + ' 0')
    print ("%.0f" % y1 + ' ' + "%.0f" % y2 + ' 0')
    print ('0 0 1')
    return x, y

def h(x, y, a, b):
    x *= a
    y *= b
    x1 = a
    x2 = 0
    y1 = 0
    y2 = b
    print ('Homothety by the ratios ' + "%.0f" % a + ' and ' + "%.0f" % b)
    print ("%.0f" % x1 + ' ' + "%.0f" % x2 + ' 0')
    print ("%.0f" % y1 + ' ' + "%.0f" % y2 + ' 0')
    print ('0 0 1')
    return x, y

def r(x, y, a):
    xs = x
    ys = y
    x1 = math.cos(a)
    x2 = -math.sin(a)
    y1 = math.sin(a)
    y2 = math.cos(a)
    x = (math.cos(a) * xs) - (math.sin(a) * ys)
    y = (math.sin(a) * xs) + (math.cos(a) * ys)
    print ('Rotation at a ' + str(a) + ' degree angle')
    print ("%.0f" % x1 + ' ' + "%.0f" % x2 + ' 0')
    print ("%.0f" % y1 + ' ' + "%.0f" % y2 + ' 0')
    print ('0 0 1')
    return x, y

def get_int_arg(argv, i, ch):
    try:
        argv[i]
    except IndexError:
        print(ch + ' not defined !')
        sys.exit(84)
    try:
        (float)(sys.argv[i])
    except ValueError:
        print(ch + ' not a number !')
        sys.exit(84)
    return (float)(sys.argv[i])

def main():
    x = get_int_arg(sys.argv, 1, 'x')
    y = get_int_arg(sys.argv, 2, 'y')
    xs = x
    ys = y
    i = 3
    try:
        len(sys.argv[3])
    except IndexError:
        print ('Need a least one transformation !')
        sys.exit(84)
    while i < len(sys.argv):
        if sys.argv[i] == '-t':
            a = get_int_arg(sys.argv, i + 1, '-t i')
            b = get_int_arg(sys.argv, i + 2, '-t j')
            x, y = t(x, y, a, b)
            i += 2
        elif sys.argv[i] == '-h':
            a = get_int_arg(sys.argv, i + 1, '-h : m')
            b = get_int_arg(sys.argv, i + 2, '-h : n')
            x, y = h(x, y, a, b)
            i += 2
        elif sys.argv[i] == '-r':
            a = get_int_arg(sys.argv, i + 1, 'r : alpha')
            x, y = r(x, y, a)
            i += 1
        elif sys.argv[i] == '-s':
            a = get_int_arg(sys.argv, i + 1, 'r : alpha')
            x, y = s(x, y, a)
            i += 1
        else:
            print('Unknow option : ' + sys.argv[i])
            sys.exit(84)
        i += 1
        x = round(x, 0)
        y = round(y, 0)
    print('(' + "%.0f" % xs + ',' + "%.0f" %ys + ') => (' +    \
          "%.2f" % x + ',' + "%.2f" % y + ')')

main()
