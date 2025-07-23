import operator as op
from enum import Enum
from dataclasses import dataclass
from fractions import Fraction
from typing import List, Tuple, Literal, cast


class TokenType(Enum):
    PLUS = 0
    MINUS = 1
    MULTIPLY = 2
    DIVIDE = 3
    LPAREN = 4
    RPAREN = 5
    NUMBER = 6


@dataclass(frozen=True)
class Token:
    type: TokenType
    value: str


@dataclass(frozen=True)
class Expr:
    pass


@dataclass(frozen=True)
class BinOp(Expr):
    op: Literal["+", "-", "*", "/"]
    left: Expr
    right: Expr

    def __str__(self):
        return f"({self.left} {self.op} {self.right})"


@dataclass(frozen=True)
class Number(Expr):
    value: Fraction

    def __str__(self):
        return str(self.value)


def main():
    print("Press <ctrl-c> or type 'exit' to exit")
    while True:
        try:
            text = input("> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if text == "exit":
            break

        try:
            tokens = lexer(text)
            expr = parser(tokens)
            print(solver(expr))
        except ValueError:
            print(f"Invalid expression")


def lexer(text: str) -> List[Token]:
    tokens: List[Token] = []

    i = 0

    while i < len(text):
        char = text[i]

        if char.isspace():
            i += 1
            continue

        if char == "." or char.isdigit():
            number: str = char
            has_dot = char == '.'
            i += 1
            while i < len(text) and (text[i].isdigit() or (text[i] == '.' and not has_dot)):
                if text[i] == '.':
                    has_dot = True
                number += text[i]
                i += 1
            tokens.append(Token(TokenType.NUMBER, number))
        elif char == "+":
            tokens.append(Token(TokenType.PLUS, char))
            i += 1
        elif char == "-":
            tokens.append(Token(TokenType.MINUS, char))
            i += 1
        elif char == "*":
            tokens.append(Token(TokenType.MULTIPLY, char))
            i += 1
        elif char == "/":
            tokens.append(Token(TokenType.DIVIDE, char))
            i += 1
        elif char == "(":
            tokens.append(Token(TokenType.LPAREN, char))
            i += 1
        elif char == ")":
            tokens.append(Token(TokenType.RPAREN, char))
            i += 1
        else:
            raise ValueError(f"Invalid character: {char}")

    if len(tokens) == 0:
        raise ValueError("Empty input text")

    return tokens


def parser(tokens: List[Token]) -> Expr:
    if len(tokens) == 0:
        raise ValueError("Empty tokens.")

    expr, i = parse_expr(tokens)

    if i != len(tokens):
        raise ValueError(f"Unexpected token at position {i}: {tokens[i]}")

    return expr


def parse_expr(tokens: List[Token], i: int = 0) -> Tuple[Expr, int]:
    expr, i = parse_term(tokens, i)
    while i < len(tokens) and tokens[i].type in {TokenType.PLUS, TokenType.MINUS}:
        op = cast(Literal["+", "-", "*", "/"], tokens[i].value)
        right, i = parse_term(tokens, i + 1)
        expr = BinOp(op, expr, right)
    return expr, i


def parse_term(tokens: List[Token], i: int) -> Tuple[Expr, int]:
    expr, i = parse_factor(tokens, i)
    while i < len(tokens) and tokens[i].type in {TokenType.MULTIPLY, TokenType.DIVIDE}:
        op = cast(Literal["+", "-", "*", "/"], tokens[i].value)
        right, i = parse_factor(tokens, i + 1)
        expr = BinOp(op, expr, right)
    return expr, i


def parse_factor(tokens: List[Token], i: int) -> Tuple[Expr, int]:
    sign = 1
    expr: Expr

    if tokens[i].type in {TokenType.PLUS, TokenType.MINUS}:
        sign = 1 if tokens[i].type == TokenType.PLUS else -1
        i += 1

    if tokens[i].type == TokenType.NUMBER:
        expr = Number(Fraction(tokens[i].value))
        i += 1
    elif tokens[i].type == TokenType.LPAREN:
        expr, i = parse_expr(tokens, i + 1)
        if i >= len(tokens) or tokens[i].type != TokenType.RPAREN:
            raise ValueError("Expected ')'")
        i += 1
    else:
        raise ValueError(f"Unexpected token: {tokens[i]}")

    if sign == -1:
        if isinstance(expr, Number):
            expr = Number(sign * expr.value)
        else:
            expr = BinOp("*", Number(Fraction(sign)), expr)

    return expr, i


def solver(expr: Expr) -> Number:
    if isinstance(expr, Number):
        return expr

    if not isinstance(expr, BinOp):
        raise ValueError(f"Unexpected object: {expr!r}")

    operations = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}

    if isinstance(expr.left, Number) and isinstance(expr.right, Number):
        return Number(operations[expr.op](expr.left.value, expr.right.value))

    left = solver(expr.left)
    right = solver(expr.right)

    return Number(operations[expr.op](left.value, right.value))


if __name__ == "__main__":
    main()
