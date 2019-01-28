# coding: utf8

from __future__ import unicode_literals, print_function


class Token(object):
    pattern = None

    def __init__(self, match):
        self.src_value = match.group(0)
        self.value = self.to_python(match.groupdict())

    @classmethod
    def get_group_pattern(cls):
        return r'(?P<%s>%s)' % (cls.__name__, cls.pattern)

    def to_python(self, m):
        return m[self.__class__.__name__]


class OperandToken(Token):
    pass


class FloatToken(OperandToken):
    pattern = r'\d+\.\d+'

    def to_python(self, m):
        return float(super(FloatToken, self).to_python(m))


class IntToken(OperandToken):
    pattern = r'\d+'

    def to_python(self, m):
        return int(super(IntToken, self).to_python(m))


class StringToken(OperandToken):
    pattern = r'"[^"]*"'

    def to_python(self, m):
        return super(StringToken, self).to_python(m)[1:-1]


class FunctionToken(Token):
    pattern = r'[A-Z]+(?=\()'


class NameToken(Token):
    pattern = r'\w+'


class CellRangeToken(Token):
    pattern = (r'\$?(?P<row1>[A-Z]+)\$?(?P<column1>[0-9]+):'
               r'\$?(?P<row2>[A-Z]+)\$?(?P<column2>[0-9]+)')

    def to_python(self, m):
        return (m['row1'], int(m['column1'])), (m['row2'], int(m['column2']))


class CellAddressToken(Token):
    pattern = r'\$?(?P<row>[A-Z]+)\$?(?P<column>[0-9]+)'

    def to_python(self, m):
        return m['row'], int(m['column'])


class SheetNameToken(Token):
    pattern = r"(?P<ws_name>('[^']+')|(\w+))!"

    def to_python(self, m):
        v = m['ws_name']
        if v.startswith("'"):
            v = v[1:-1]
        return v


class OperationToken(Token):
    pass


class AddToken(OperationToken):
    pattern = r'\+'


class SubtractToken(OperationToken):
    pattern = r'\-'


class DivideToken(OperationToken):
    pattern = r'/'


class MultiplyToken(OperationToken):
    pattern = r'\*'


class ConcatToken(OperationToken):
    pattern = r'\&'


class ExponentToken(OperationToken):
    pattern = r'\^'


class CompareNotEqToken(OperationToken):
    pattern = r'\<\>'


class CompareGTEToken(OperationToken):
    pattern = r'\>\='


class CompareLTEToken(OperationToken):
    pattern = r'\<\='


class CompareGTToken(OperationToken):
    pattern = r'\>'


class CompareLTToken(OperationToken):
    pattern = r'\<'


class CompareEgToken(OperationToken):
    pattern = r'\='


class LeftBracketToken(OperationToken):
    pattern = r'\('


class RightBracketToken(OperationToken):
    pattern = r'\)'


class SpaceToken(Token):
    pattern = r'[ ]+'


class Separator(Token):
    pattern = r','
