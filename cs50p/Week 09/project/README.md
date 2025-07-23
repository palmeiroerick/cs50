# Arithmetic Interpreter

## Video Demo: https://youtu.be/KuPzkrMGkkY

## Table of Contents

- [Description](#description)
  - [Usage](#usage)
  - [Supported](#supported)
- [Data Model](#data-model)
- [Functions](#functions)
  - [Parsing Functions](#parsing-functions)
- [Grammar (EBNF)](#grammar-ebnf)
- [Tests](#tests)

## Description

A simple arithmetic interpreter that supports basic operations and fractions.

### Usage

```bash
python project.py
```

#### Program output example

```text
Press <ctrl-c> or type 'exit' to exit
> 2 + 2
4
> 3/2 * 2/3
1
> (2 * 3) / 4
3/2
> 12345 - 67890
-55545
```

#### Supported

- The four basic mathematical operations `+`, `-`, `*`, `/`
  - `1 + 2 * 3 / 4`
- Integers and rational numbers using python's `Fraction()`
  - `10.5 / 5.25`, `.25 + .75`, `3/2 * 2/3`
- Unary operations (`+` and `-`) before numbers or subexpressions
  - `-(-25 + 75)`, `+3 + (-2)`
- Parentheses for precedence
  - `(1 + 2) / ((3 - 4) * (5 - 2))`, `2 - (2 - 2)`

No supports implicit multiplication (e.g., `2(3 + 4)`, `(5 + 6)(7 + 8)`).

### Data Model

- **Tokens**
  - `class TokenType(Enum)`: Defines a set of symbolic constants that represent the type of a `Token()`.
  - `class Token()`: Class that represents an individual token with type and value.
- **Abstract Syntax Tree**
  - `class Expr()`: Base class for all AST nodes representing an expression.
  - `class BinOp(Expr)`: Node that represents a binary operation.
  - `class Number(Expr)`: Leaf node that represents a numeric literal stored as a `Fraction()`.

### Functions

- `main()`: Read-Eval-Print Loop (REPL) of the interpreter.
- `lexer(text: str) -> List[Token]`: Converts an input string into a list of tokens.
- `parser(tokens: List[Token]) -> Expr`: Entry point of the parser. Converts a list of tokens into an Abstract Syntax Tree.
- `solver(expr: Expr) -> Number`: Evaluates the AST, applying the operations and returning the result of the expression.

#### Parsing Functions

These functions implement a **recursive descent parser**, a top-down approach where each of the **mutually recursive functions** parses a part of the grammar.

- `parse_expr(tokens: List[Token], i: int = 0) -> Tuple[Expr, int]`: Parses addition and subtraction (`+`, `-`).
- `parse_term(tokens: List[Token], i: int) -> Tuple[Expr, int]`: Parses multiplication and division (`*`, `/`).
- `parse_factor(tokens: List[Token], i: int) -> Tuple[Expr, int]`: Parses unary operations, numbers, and parentheses.

> Note: the `i` parameter is the index of the current token.

### Grammar (EBNF)

```EBNF
expr    = term { ("+" | "-") term };
term    = factor { ("*" | "/") factor };
factor  = [ ("+" | "-") ] ( number | "(" expr ")" );
number  = digit { digit } [ "." digit { digit } ]
        | "." digit { digit };
digit   = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
```

### Tests

Unit tests are defined using `pytest`

```bash
pytest test_project.py
```
