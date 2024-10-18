from unittest import TestCase

from main.objects.matrix import Matrix


class TestMatrix(TestCase):

    def test_valid_matrix(self):
        """Test for a valid matrix."""
        data = [[1, 2], [3, 4], [5, 6]]
        matrix = Matrix(data)
        self.assertEqual(matrix.data, data)
        self.assertEqual(3, matrix.n_rows)
        self.assertEqual(2, matrix.n_cols)

    def test_non_list_input(self):
        """Test if input is not a list."""
        with self.assertRaises(ValueError) as context:
            Matrix(1234)  # Not a list
        self.assertTrue("Data must be a list of lists." in str(context.exception))

    def test_non_list_rows(self):
        """Test if input contains non-list elements in the outer list."""
        with self.assertRaises(ValueError) as context:
            Matrix([1, 2, 3])  # Outer list contains non-list elements
        self.assertTrue("Each row must be a list." in str(context.exception))

    def test_empty_matrix(self):
        """Test if matrix is empty (no rows or no columns)."""
        with self.assertRaises(ValueError) as context:
            Matrix([])  # No rows
        self.assertTrue("Matrix cannot be empty." in str(context.exception))

        with self.assertRaises(ValueError) as context:
            Matrix([[]])  # No columns
        self.assertTrue("Matrix cannot be empty." in str(context.exception))

    def test_inconsistent_row_length(self):
        """Test if rows have inconsistent lengths."""
        with self.assertRaises(ValueError) as context:
            Matrix([[1, 2], [3]])  # Second row has different length
        self.assertTrue("All rows must have the same length." in str(context.exception))

    def test_non_numeric_elements(self):
        """Test if elements in the matrix are non-numeric."""
        with self.assertRaises(ValueError) as context:
            Matrix([[1, 2], [3, "four"]])  # Second row contains a non-numeric element
        self.assertTrue("Matrix elements must be Numbers." in str(context.exception))

    def test_mixed_numeric_types(self):
        """Test if matrix can handle both int and float."""
        data = [[1, 2.0], [3, 4]]
        matrix = Matrix(data)
        self.assertEqual(matrix.data, data)

    def test_square_matrix(self):
        """Test if a square matrix is correctly identified."""
        matrix = Matrix([[1, 2], [3, 4]])
        self.assertTrue(matrix.is_square())

    def test_non_square_matrix(self):
        """Test if a non-square matrix is correctly identified."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertFalse(matrix.is_square())

    def test_single_element_matrix_is_square(self):
        """Test if a 1x1 matrix is considered square."""
        matrix = Matrix([[1]])
        self.assertTrue(matrix.is_square())

    def test_add_matrices_different_sizes(self):
        """Test adding matrices of different sizes raises ValueError."""
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError) as context:
            A + B
        self.assertEqual("Matrices must have the same dimensions to be added. One is 2x2 and the other is 2x3",
                         str(context.exception))

    def test_add_valid_matrices(self):
        """Test adding two valid matrices of the same size."""
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])
        C = A + B
        self.assertEqual(C.data, [[6, 8], [10, 12]])

    def test_subtract_matrices_different_sizes(self):
        """Test subtracting matrices of different sizes raises ValueError."""
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError) as context:
            A - B
        self.assertEqual("Matrices must have the same dimensions to be subtracted. One is 2x2 and the other is 2x3",
                         str(context.exception))

    def test_subtract_valid_matrices(self):
        """Test subtracting two valid matrices of the same size."""
        A = Matrix([[10, 20], [30, 40]])
        B = Matrix([[5, 15], [25, 35]])
        C = A - B
        self.assertEqual(C.data, [[5, 5], [5, 5]])

    def test_matmul_invalid_dimensions(self):
        """Test matrix multiplication with incompatible dimensions."""
        A = Matrix([[1, 2, 3], [4, 5, 6]])
        B = Matrix([[7, 8], [9, 10]])
        with self.assertRaises(ValueError) as context:
            A @ B
        self.assertEqual(
            "Number of columns in the first matrix (3) must equal number of rows in the second matrix (2).",
            str(context.exception))

    def test_matmul_valid_matrices(self):
        """Test matrix multiplication with valid matrices."""
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])
        C = A @ B
        expected_data = [[19, 22], [43, 50]]
        self.assertEqual(C.data, expected_data)

    def test_elementwise_multiplication_valid(self):
        """Test element-wise multiplication with valid matrices."""
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])
        C = A * B
        expected_data = [[5, 12], [21, 32]]
        self.assertEqual(C.data, expected_data)

    def test_elementwise_multiplication_invalid_dimensions(self):
        """Test element-wise multiplication with incompatible dimensions."""
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6, 7], [8, 9, 10]])  # Different size (2x3)
        with self.assertRaises(ValueError) as context:
            A * B
        self.assertEqual(
            "Matrices must have the same dimensions for element-wise multiplication. One is 2x2 and the other is 2x3",
            str(context.exception))

    def test_scalar_multiplication_matrix_on_left(self):
        """Test scalar multiplication with scalar on the left."""
        A = Matrix([[1, 2], [3, 4]])
        C = A * 2
        expected_data = [[2, 4], [6, 8]]
        self.assertEqual(C.data, expected_data)

    def test_scalar_multiplication_matrix_on_right(self):
        """Test scalar multiplication with scalar on the right."""
        A = Matrix([[1, 2], [3, 4]])
        C = 3 * A  # Testing scalar on the left
        expected_data = [[3, 6], [9, 12]]
        self.assertEqual(C.data, expected_data)

    def test_transpose_matrix(self):
        """Test the transpose of a matrix."""
        A = Matrix([[1, 2, 3], [4, 5, 6]])
        A_T = A.T
        expected_data = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(A_T.data, expected_data)
        self.assertTrue(A == A_T.T)

    def test_double_transpose_equals_original(self):
        """Test that the transpose of a transpose returns the original matrix."""
        A = Matrix([[1, 2, 3], [4, 5, 6]])
        A_TT = A.T.T
        self.assertTrue(A == A_TT)

    def test_identity_matrix(self):
        """Test the creation of an identity matrix of size n x n."""
        I = Matrix.identity(3)
        expected_data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(I.data, expected_data)

    def test_identity_matrix_invalid_size(self):
        """Test that creating an identity matrix with invalid size raises an error."""
        with self.assertRaises(ValueError) as context:
            Matrix.identity(0)
        self.assertEqual(str(context.exception), "Size of the identity matrix must be a positive integer.")

    def test_zero_matrix(self):
        zero_matrix_3x4 = Matrix.zero(3, 4)
        self.assertEqual(zero_matrix_3x4, Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))


    def test_zero_matrix_invalid_dimensions(self):
        # Test for invalid dimensions
        with self.assertRaises(ValueError):
            Matrix.zero(0, 3)  # Zero rows

        with self.assertRaises(ValueError):
            Matrix.zero(3, 0)  # Zero columns

        with self.assertRaises(ValueError):
            Matrix.zero(-2, 2)  # Negative rows

        with self.assertRaises(ValueError):
            Matrix.zero(2, -2)  # Negative columns

    def test_getitem_access_element(self):
        """Test accessing an element using matrix[row][col]."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(matrix[2][2], 9)  # Access element at row 2, column 2

    def test_getitem_access_row(self):
        """Test accessing a row using matrix[row]."""
        matrix = Matrix([[1, 2], [3, 4], [5, 6]])
        self.assertEqual(matrix[1], [3, 4])  # Access row 1

    def test_setitem_modify_element(self):
        """Test modifying an element using matrix[row][col] = value."""
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix[1][2] = 10  # Set element at row 1, column 2 to 10
        self.assertEqual(matrix[1][2], 10)
        self.assertEqual(matrix.data, [[1, 2, 3], [4, 5, 10], [7, 8, 9]])

    def test_setitem_replace_row(self):
        """Test replacing an entire row using matrix[row] = new_row."""
        matrix = Matrix([[1, 2], [3, 4], [5, 6]])
        matrix[1] = [7, 8]  # Replace row 1 with [7, 8]
        self.assertEqual(matrix[1], [7, 8])
        self.assertEqual(matrix.data, [[1, 2], [7, 8], [5, 6]])

    def test_setitem_invalid_row_length(self):
        """Test that setting a row with incorrect length raises a ValueError."""
        matrix = Matrix([[1, 2], [3, 4], [5, 6]])
        with self.assertRaises(ValueError) as context:
            matrix[0] = [7, 8, 9]  # Row length does not match matrix column count
        self.assertEqual(str(context.exception), "Row must have exactly 2 elements.")

    def test_clone_equals_original(self):
        # Test that cloned matrix is equal to the original matrix
        original_matrix = Matrix([[1, 2], [3, 4]])
        cloned_matrix = original_matrix.clone()

        self.assertEqual(original_matrix, cloned_matrix, "The cloned matrix should be equal to the original matrix.")

    def test_clone_is_independent(self):
        # Test that modifying the cloned matrix does not affect the original matrix
        original_matrix = Matrix([[1, 2], [3, 4]])
        cloned_matrix = original_matrix.clone()

        # Modify the cloned matrix
        cloned_matrix[0][0] = 99

        # Check that the original matrix is unchanged
        self.assertNotEqual(original_matrix, cloned_matrix,
                            "The original matrix should not change when the cloned matrix is modified.")
        self.assertEqual(original_matrix[0][0], 1, "Original matrix value should remain unchanged.")


