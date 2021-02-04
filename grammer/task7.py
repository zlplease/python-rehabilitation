#1. 编写一个函数calu(a, b, op)。要求：
# op表示加减乘除某一运算，函数要求返回a与b的运算结果
# 当运算出现错误时，捕获该错误并在控制台输出相关错误信息，输出格式要求如下
# Caught an Exception:
# Exception Type: {错误类型}
# Exception Info: {错误提示信息}
def calu(a, b, op):
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        try:
            x = a / b
            return x
        except Exception as e:
            print('Caught an Exception:')
            info = repr(e)
            re = info[0:info.rfind('(',1)]
            print('Exception Type: '+re)
            print('Exception Info:',e)

# 2. 编写一个函数devide(a, b)，要求：
# 以a为被除数，b为除数，返回a除b的结果
# 当b为0时，手动抛出异常
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('0')
    else:
        x = a / b
        return x

# 3. 写一个单元测试来测试你第二题编写的devide函数。测试内容：
# 测试devide(5, 1)与devide(6, 4)的返回值是否正确
# 测试devide(5, 0)是否会抛出异常
# 运行单元测试

import unittest

class task(unittest.TestCase):

    def test_divide1(self):
        x = divide(5, 1)
        self.assertEqual(x, 5.0)

    def test_divide2(self):
        x = divide(6, 4)
        self.assertEqual(x, 1.5)

    def test_divide3(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
            self.assertEqual(ZeroDivisionError,divide(5, 0))


# if __name__ == '__main__':
#     unittest.main()
# 4. 为第一题的calu函数编写一个文档测试，测试内容：
# >>> calu(1, 2, "+")
# 3
# >>> calu(1, 2, "-")
# -1
# >>> calu(1, 2, "*")
# 2
# >>> calu(1, 2, "/")
# 0.5
# >>> calu(1, 0, "+")
# Caught an Exception:
# Exception Type: ZreoDivisionError
# Exception Info: division by zero

import doctest

def calu(a, b, op):
    """
        >>> calu(1, 2, "+")
        3
        >>> calu(1, 2, "-")
        -1
        >>> calu(1, 2, "*")
        2
        >>> calu(1, 2, "/")
        0.5
        >>> calu(1, 0, "/")
        Caught an Exception:
        Exception Type: ZeroDivisionError
        Exception Info: division by zero
    """
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        try:
            x = a / b
            return x
        except Exception as e:
            print('Caught an Exception:')
            info = repr(e)
            re = info[0:info.rfind('(',1)]
            print('Exception Type: '+re)
            print('Exception Info:',e)

if __name__=='__main__':
    import doctest
    doctest.testmod()
