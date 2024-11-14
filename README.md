# assignment1

## Description

This project contains a `Matrix` class that allows for matrix operations such as addition, subtraction, and multiplication. However, some methods are left incomplete for you to implement as part of an assignment.

Your task is to implement the following methods inside the `Matrix` class:

- `__sub__(self, other: 'Matrix') -> 'Matrix'`: Perform element-wise matrix subtraction.
- `__add__(self, other: 'Matrix') -> 'Matrix'`: Perform element-wise matrix addition.
- `__matmul__(self, other: 'Matrix') -> 'Matrix'`: Perform matrix multiplication (not element-wise, but true matrix multiplication).

Each of these methods has comments inside the code to guide you through the process of implementing the correct functionality.

## Instructions

1. Clone this repository to your local machine.
2. Open the project in your preferred code editor.
3. Navigate to the `Matrix` class and implement the following methods:
   - `__sub__`
   - `__add__`
   - `__matmul__`
4. You can follow the comments in each method for hints on how to complete the implementation.

## Testing

Once you've completed the implementation, you can verify that your solutions are correct by running the unit tests provided.

Run the following command in your terminal:

```bash
python -m unittest
