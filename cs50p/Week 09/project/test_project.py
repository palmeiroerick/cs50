import re
import pytest
from project import Token, TokenType, lexer, Expr, BinOp, Number, parser, solver
from typing import List
from fractions import Fraction


@pytest.mark.parametrize("text, tokens", [
    ("  1 +2 - 3 * 4  /5  ", [
        Token(TokenType.NUMBER, "1"),
        Token(TokenType.PLUS, "+"),
        Token(TokenType.NUMBER, "2"),
        Token(TokenType.MINUS, "-"),
        Token(TokenType.NUMBER, "3"),
        Token(TokenType.MULTIPLY, "*"),
        Token(TokenType.NUMBER, "4"),
        Token(TokenType.DIVIDE, "/"),
        Token(TokenType.NUMBER, "5"),
    ]),
    ("(3 -    2) / 5 ", [
        Token(TokenType.LPAREN, "("),
        Token(TokenType.NUMBER, "3"),
        Token(TokenType.MINUS, "-"),
        Token(TokenType.NUMBER, "2"),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.DIVIDE, "/"),
        Token(TokenType.NUMBER, "5"),
    ]),
    ("-.5+5.25/5", [
        Token(TokenType.MINUS, "-"),
        Token(TokenType.NUMBER, ".5"),
        Token(TokenType.PLUS, "+"),
        Token(TokenType.NUMBER, "5.25"),
        Token(TokenType.DIVIDE, "/"),
        Token(TokenType.NUMBER, "5"),
    ])
])
def test_lexer(text: str, tokens: List[Token]):
    assert lexer(text) == tokens


@pytest.mark.parametrize("text, error_msg", [
    ("", "Empty input text"),
    ("  \r\n \t", "Empty input text"),
    ("1 + 2 = 3", "Invalid character: ="),
    ("1 + 2 # 3", "Invalid character: #"),
    ("2 + $4 - 10", "Invalid character: $"),
    ("4 @ 3 - 7", "Invalid character: @"),
    ("5 + 3  ?10", "Invalid character: ?"),
    ("4 + 2 % 8", "Invalid character: %"),
    ("1 + 2 - 3!", "Invalid character: !"),
    ("4[ + 2 / 8", "Invalid character: ["),
    ("2^2 + 3 ", "Invalid character: ^"),
])
def test_lexer_invalid(text: str, error_msg: str):
    with pytest.raises(ValueError, match=re.escape(error_msg)):
        lexer(text)


@pytest.mark.parametrize("tokens, expr", [
    # (1 + 2) * 3
    ([Token(TokenType.LPAREN, "("), Token(TokenType.NUMBER, "1"), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, "2"), Token(TokenType.RPAREN, ")"), Token(TokenType.MULTIPLY, "*"), Token(TokenType.NUMBER, "3")],
     BinOp("*", BinOp("+", Number(Fraction("1")), Number(Fraction("2"))), Number(Fraction("3")))),

    # (1 + 2) / ((3 - 4) * (5 - 2))
    ([Token(TokenType.LPAREN, "("), Token(TokenType.NUMBER, "1"), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, "2"), Token(TokenType.RPAREN, ")"), Token(TokenType.DIVIDE, "/"), Token(TokenType.LPAREN, "("), Token(TokenType.LPAREN, "("), Token(TokenType.NUMBER, "3"), Token(TokenType.MINUS, "-"), Token(TokenType.NUMBER, "4"), Token(TokenType.RPAREN, ")"), Token(TokenType.MULTIPLY, "*"), Token(TokenType.LPAREN, "("), Token(TokenType.NUMBER, "5"), Token(TokenType.MINUS, "-"), Token(TokenType.NUMBER, "2"), Token(TokenType.RPAREN, ")"), Token(TokenType.RPAREN, ")"),],
     BinOp("/", BinOp("+", Number(Fraction("1")), Number(Fraction("2"))), BinOp("*", BinOp("-", Number(Fraction("3")), Number(Fraction("4"))), BinOp("-", Number(Fraction("5")), Number(Fraction("2")))))),

    # 2 + (-(-3 * 2))
    ([Token(TokenType.NUMBER, "2"), Token(TokenType.PLUS, "+"), Token(TokenType.LPAREN, "("), Token(TokenType.MINUS, "-"), Token(TokenType.LPAREN, "("), Token(TokenType.MINUS, "-"), Token(TokenType.NUMBER, "3"), Token(TokenType.MULTIPLY, "*"), Token(TokenType.NUMBER, "2"), Token(TokenType.RPAREN, ")"), Token(TokenType.RPAREN, ")"),],
     BinOp("+", Number(Fraction("2")), BinOp("*", Number(Fraction("-1")), BinOp("*", Number(Fraction("-3")), Number(Fraction("2")))))),

    # +.4 + (-.2)
    ([Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, ".4"), Token(TokenType.PLUS, "+"), Token(TokenType.LPAREN, "("), Token(TokenType.MINUS, "-"), Token(TokenType.NUMBER, ".2"), Token(TokenType.RPAREN, ")"),],
     BinOp("+", Number(Fraction("0.4")), Number(Fraction("-0.2")))),

    # 3 + 4 + 5 + 6 + 9
    ([Token(TokenType.NUMBER, "3"), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, "4"), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, "5"), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, "6"), Token(TokenType.PLUS, "+"), Token(TokenType.NUMBER, "9"),],
     BinOp("+", BinOp("+", BinOp("+", BinOp("+", Number(Fraction("3")), Number(Fraction("4"))), Number(Fraction("5"))), Number(Fraction("6"))), Number(Fraction("9")))),
])
def test_parser(tokens: List[Token], expr: Expr):
    assert parser(tokens) == expr


@pytest.mark.parametrize("tokens, error_msg", [
    ([], "Empty tokens"),
    (
        [Token(TokenType.NUMBER, "."),
         Token(TokenType.PLUS, "+"),
         Token(TokenType.NUMBER, "1")],
        "Invalid literal for Fraction: '.'"
    ),
    (
        [
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.LPAREN, "("),
            Token(TokenType.NUMBER, "3"),
            Token(TokenType.MULTIPLY, "*"),
            Token(TokenType.NUMBER, "4"),
        ],
        "Expected ')'"
    ),
    (
        [
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.NUMBER, "3"),
        ],
        "Unexpected token"
    ),
    (
        [
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.RPAREN, ")"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "3"),
        ],
        "Unexpected token"
    ),
    (
        [
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.NUMBER, "2"),
            Token(TokenType.PLUS, "+"),
            Token(TokenType.NUMBER, "3"),
        ],
        "Unexpected token"
    ),
])
def test_parser_invalid(tokens: List[Token], error_msg: str):
    with pytest.raises(ValueError, match=re.escape(error_msg)):
        parser(tokens)


@pytest.mark.parametrize("expr, expected", [
    # 1 + 2 * 3 = 7
    (BinOp("+", Number(Fraction("1")), BinOp("*", Number(Fraction("2")), Number(Fraction("3")))),
     Number(Fraction("7"))),

    # (4 + 6) / 5 = 2
    (BinOp("/", BinOp("+", Number(Fraction("4")), Number(Fraction("6"))), Number(Fraction("5"))),
     Number(Fraction("2"))),

    # ((2 - 3) * (5 + 1)) = -6
    (BinOp("*", BinOp("-", Number(Fraction("2")), Number(Fraction("3"))), BinOp("+", Number(Fraction("5")), Number(Fraction("1")))),
     Number(Fraction("-6"))),

    # ((-2) * (-4)) + 3 = 11
    (BinOp("+", BinOp("*", Number(Fraction("-2")), Number(Fraction("-4"))), Number(Fraction("3"))),
     Number(Fraction("11"))),

    # 1 + 1/2 + 1/4 = 7/4
    (BinOp("+", BinOp("+", Number(Fraction(1)), Number(Fraction(1, 2))), Number(Fraction(1, 4))),
     Number(Fraction(7, 4))),

     # 2 - 2 - 2 = -2
    (BinOp("-", BinOp("-", Number(Fraction("2")), Number(Fraction("2"))), Number(Fraction("2"))),
     Number(Fraction("-2"))),

     # 2 - (2 - 2) = 2
    (BinOp("-", Number(Fraction("2")), BinOp("-", Number(Fraction("2")), Number(Fraction("2")))),
     Number(Fraction("2"))),
])
def test_solver(expr: Expr, expected: Fraction):
    assert solver(expr) == expected
