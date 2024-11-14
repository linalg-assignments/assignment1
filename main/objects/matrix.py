from numbers import Number
from typing import List


class Matrix:
    def __init__(self, data: List[List[Number]]) -> None:
        """
        Initializes the Matrix object and validates the input data.
        :param data: A list of lists where each sublist represents a row in the matrix.
        """
        self._is_valid_data(data)
        self.data = data
        self.n_rows = len(data)
        self.n_cols = len(data[0])

    def _is_valid_data(self, data: List[List[Number]]) -> None:
        """
        Validates that the input data is a list of lists containing numeric values.
        :param data: The data to be validated.
        """
        self._check_data_is_list(data)
        self._check_data_elements_are_list(data)
        self._check_data_is_not_empty(data)
        self._check_rows_have_same_size(data)
        self._check_rows_elements_are_numeric(data)

    def is_square(self) -> bool:
        """
        Check if the matrix is square (i.e., number of rows == number of columns).
        :return: True if the matrix is square, False otherwise.
        """
        return self.n_rows == self.n_cols

    @staticmethod
    def identity(n) -> 'Matrix':
        """Returns an identity matrix of size n x n."""
        if n <= 0:
            raise ValueError("Size of the identity matrix must be a positive integer.")
        identity_data = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        return Matrix(identity_data)

    @staticmethod
    def zero(n_rows: int, n_cols: int) -> 'Matrix':
        """
        Returns a zero matrix of size n_rows x n_cols.
        :param n_rows: Number of rows in the zero matrix.
        :param n_cols: Number of columns in the zero matrix.
        :return: A Matrix object representing a zero matrix.
        """
        if n_rows <= 0 or n_cols <= 0:
            raise ValueError("Number of rows and columns must be positive integers.")
        zero_data = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
        return Matrix(zero_data)

    @staticmethod
    def _check_data_is_list(data: List[List[Number]]) -> None:
        """
        Checks if the provided data is a list.
        :param data: The data to be validated.
        """
        if not isinstance(data, list):
            raise ValueError("Data must be a list of lists.")

    @staticmethod
    def _check_data_elements_are_list(data: List[List[Number]]) -> None:
        """
        Checks if each element in the outer list is a list.
        :param data: The data to be validated.
        """
        if not all(isinstance(row, list) for row in data):
            raise ValueError("Each row must be a list.")

    @staticmethod
    def _check_data_is_not_empty(data: List[List[Number]]) -> None:
        """
        Checks if the matrix is not empty (i.e., it has at least one row and one column).
        :param data: The data to be validated.
        """
        if len(data) == 0 or len(data[0]) == 0:
            raise ValueError("Matrix cannot be empty.")

    @staticmethod
    def _check_rows_have_same_size(data: List[List[Number]]) -> None:
        """
        Checks if all rows in the matrix have the same number of elements.
        :param data: The data to be validated.
        """
        row_length = len(data[0])
        if not all(len(row) == row_length for row in data):
            raise ValueError("All rows must have the same length.")

    @staticmethod
    def _check_rows_elements_are_numeric(data: List[List[Number]]) -> None:
        """
        Checks if all elements in the matrix are Numbers.
        :param data: The data to be validated.
        """
        for row in data:
            if not all(isinstance(element, Number) for element in row):
                raise ValueError("Matrix elements must be Numbers.")

    def __add__(self, other: 'Matrix') -> 'Matrix':
        """
        Adds two matrices element-wise.
        :param other: Another matrix to add to this matrix.
        :return: A new Matrix object that is the result of the addition.
        """
        # Step 1: Check if the matrices have the same dimensions.
        # Hint: The number of rows and columns must be the same for both matrices.
        if ...: # WRITE YOUR CODE HERE
            raise ValueError(
                f"Matrices must have the same dimensions to be added. One is {self.n_rows}x{self.n_cols} and the other is {other.n_rows}x{other.n_cols}")

        # Step 2: Perform element-wise addition.
        result_data = [...]

        # Step 3: Return a new Matrix object using the result_data list.
        return Matrix(result_data)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        """
        Subtracts one matrix from another element-wise.
        :param other: Another matrix to subtract from this matrix.
        :return: A new Matrix object that is the result of the subtraction.
        """
        # Step 1: Check if the matrices have the same dimensions.
        # Hint: The number of rows and columns must be the same for both matrices.
        if ...: # WRITE YOUR CODE HERE
            raise ValueError(
                f"Matrices must have the same dimensions to be subtracted. One is {self.n_rows}x{self.n_cols} and the other is {other.n_rows}x{other.n_cols}")

        # Step 2: Perform element-wise subtraction
        result_data = [...] # WRITE YOUR CODE HERE

        # Step 3: Return a new Matrix object using the result_data list.
        return Matrix(result_data)

    def __mul__(self, other) -> 'Matrix':
        """
        Performs element-wise multiplication of two matrices, or scalar multiplication if 'other' is a number.
        :param other: Another matrix to multiply element-wise or a scalar.
        :return: A new Matrix object that is the result of the multiplication.
        """
        if isinstance(other, Matrix):
            # Element-wise matrix multiplication
            if self.n_rows != other.n_rows or self.n_cols != other.n_cols:
                raise ValueError(
                    f"Matrices must have the same dimensions for element-wise multiplication. One is {self.n_rows}x{self.n_cols} and the other is {other.n_rows}x{other.n_cols}")
            result_data = [
                [self[i][j] * other[i][j] for j in range(self.n_cols)]
                for i in range(self.n_rows)
            ]
        elif isinstance(other, Number):
            # Scalar multiplication
            result_data = [
                [self[i][j] * other for j in range(self.n_cols)]
                for i in range(self.n_rows)
            ]
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Matrix' and '{}'".format(type(other).__name__))

        return Matrix(result_data)

    def __rmul__(self, other: Number) -> 'Matrix':
        """
        Handles scalar multiplication when the scalar is on the left (i.e., scalar * Matrix).
        :param other: A scalar value to multiply the matrix by.
        :return: A new Matrix object that is the result of the scalar multiplication.
        """
        return self.__mul__(other)

    def __matmul__(self, other: 'Matrix') -> 'Matrix':
        """
        Performs matrix multiplication.
        :param other: Another matrix to multiply with this matrix.
        :return: A new Matrix object that is the result of the matrix multiplication.
        """
        # Step 1: Check if the matrices can be multiplied.
        # Hint: The number of columns in the first matrix (self) must be equal to
        # the number of rows in the second matrix (other). If not, raise a ValueError.
        if ...: # WRITE YOUR CODE HERE
            raise ValueError(
                f"Number of columns in the first matrix ({self.n_cols}) must equal number of rows in the second matrix ({other.n_rows}).")

        # Step 2: Perform matrix multiplication by iterating over rows and columns.
        # - For each row in the first matrix (self), and each column in the second matrix (other),
        #   compute the dot product between the row and the column.
        # - To do this, multiply corresponding elements from the row and column, and sum them up.
        result_data = [...] # WRITE YOUR CODE HERE

        # Step 3: Return a new Matrix object using the result_data list.
        return Matrix(result_data)

    @property
    def T(self):
        """Returns the transpose of the matrix."""
        transposed_data = [[self[j][i] for j in range(self.n_rows)] for i in range(self.n_cols)]
        return Matrix(transposed_data)

    def __eq__(self, other):
        """Check if two matrices are equal."""
        if not isinstance(other, Matrix):
            return False
        if self.n_rows != other.n_rows or self.n_cols != other.n_cols:
            return False
        return all(self[i][j] == other[i][j] for i in range(self.n_rows) for j in range(self.n_cols))

    def __repr__(self) -> str:
        """
        Represents the matrix in a readable string format.
        :return: A string representation of the matrix.
        """
        return f"Matrix({self.data})"

    def __getitem__(self, idx: int) -> List[Number]:
        """
        Allows access to a specific row using matrix[row].
        :param idx: The row index to access.
        :return: The row at the specified index.
        """
        return self.data[idx]

    def __setitem__(self, idx: int, row: List[Number]) -> None:
        """
        Allows setting a specific row using matrix[row] = new_row.
        :param idx: The row index to modify.
        :param row: The new row data to set at the specified index.
        """
        if len(row) != self.n_cols:
            raise ValueError(f"Row must have exactly {self.n_cols} elements.")
        self.data[idx] = row

    def clone(self) -> 'Matrix':
        """
        Creates and returns a deep copy (clone) of the matrix.
        :return: A new Matrix object that is a clone of this matrix.
        """
        cloned_data = [row[:] for row in self.data]  # Create a deep copy of the data
        return Matrix(cloned_data)