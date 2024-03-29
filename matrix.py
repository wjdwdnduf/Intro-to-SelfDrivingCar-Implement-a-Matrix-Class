import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            return a*d - b*c
        
        if self.h == 1:
            return self.g[0][0]
        # TODO - your code here

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        result = 0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        else:
            for i in range(self.h):
                for j in range(self.w):
                    result += self.g[i][j]
                    
        return result    
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            if a*d-b*c == 0:
                raise ValueError('non-invertible')
            else:
                inverse = [[(d/(a*d-b*c)),(-b/(a*d-b*c))], 
                           [(-c/(a*d-b*c)),(a/(a*d-b*c))]]
        
        if self.h == 1:
            inverse=[[1/self.g[0][0]]]
            
        return Matrix(inverse)
        # TODO - your code here

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = []
        for c in range(self.w):
            new_row = []
            for r in range(self.h):
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
        return Matrix(matrix_transpose)
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        reset = []
        add_matrix = []
        for i in range(self.h):
            for j in range(self.w):
                add = self.g[i][j] + other.g[i][j]
                reset.append(add)
            add_matrix.append(reset)
            reset = []
        return Matrix(add_matrix)
        #   
        # TODO - your code here
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        reset = []
        neg_matrix = []
        for i in range(self.h):
            for j in range(self.w):
                neg = -self.g[i][j]
                reset.append(neg)
            neg_matrix.append(reset)
            reset = []
        return Matrix(neg_matrix)
        #   
        # TODO - your code here
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        reset = []
        sub_matrix = []
        for i in range(self.h):
            for j in range(self.w):
                sub = self.g[i][j] - other.g[i][j]
                reset.append(sub)
            sub_matrix.append(reset)
            reset = []
        return Matrix(sub_matrix)
        #   
        # TODO - your code here
        #   

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        product = []
        transposeB = other.T()
        result = 0

        for r1 in range(self.h):
            new_row = []
            for r2 in range(transposeB.h):
                for r3 in range(self.w):
                    result += self.g[r1][r3] * transposeB[r2][r3]
                new_row.append(result)
                result = 0
            product.append(new_row)
            
        return Matrix(product)
            #   
            # TODO - your code here
            #

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
        
       
            reset = []
            remul_matrix = []
            for i in range(self.h):
                for j in range(self.w):
                    reset.append(self.g[i][j] * other)
                remul_matrix.append(reset)
                reset = []
                
            return Matrix(remul_matrix)
            #   
            # TODO - your code here
            #
            