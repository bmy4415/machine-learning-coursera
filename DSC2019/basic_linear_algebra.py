def vector_size_check(*vector_variables):
    lens = [len(v) for v in vector_variables]
    return len(set(lens)) == 1

def vector_addition(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError

    return [sum(row) for row in zip(*vector_variables)]

def vector_subtraction(*vector_variables):
    if vector_size_check(*vector_variables) == False:
        raise ArithmeticError

    return vector_addition(vector_variables[0], *[[-n for n in v] for v in vector_variables[1:]])


def scalar_vector_product(alpha, vector_variable):
    return [alpha*n for n in vector_variable]


def matrix_size_check(*matrix_variables):
    return len(set([(len(v), len(v[0])) for v in matrix_variables])) == 1


def is_matrix_equal(*matrix_variables):
    row = len(matrix_variables[0])
    col = len(matrix_variables[0][0])
    for i in range(row):
        for j in range(col):
            if len(set([v[i][j] for v in matrix_variables])) != 1:
                return False

    return True


def matrix_addition(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError

    row = len(matrix_variables[0])
    col = len(matrix_variables[0][0])
    return [[sum([v[i][j] for v in matrix_variables]) for j in range(col)] for i in range(row)]


def matrix_subtraction(*matrix_variables):
    if matrix_size_check(*matrix_variables) == False:
        raise ArithmeticError

    row = len(matrix_variables[0])
    col = len(matrix_variables[0][0])
    return matrix_addition(matrix_variables[0], *[[[-v[i][j] for j in range(col)] for i in range(row)] for v in matrix_variables[1:]])


def matrix_transpose(matrix_variable):
    row = len(matrix_variable)
    col = len(matrix_variable[0])
    return [[matrix_variable[i][j] for i in range(row)] for j in range(col)]


def scalar_matrix_product(alpha, matrix_variable):
    return [[alpha*n for n in row] for row in matrix_variable]


def is_product_availability_matrix(matrix_a, matrix_b):
    return len(matrix_a[0]) == len(matrix_b)


def matrix_product(matrix_a, matrix_b):
    if is_product_availability_matrix(matrix_a, matrix_b) == False:
        raise ArithmeticError

    row = len(matrix_a)
    col = len(matrix_b[0])
    return [[sum([a*b for (a,b) in zip(matrix_a[i], matrix_transpose(matrix_b)[j])]) for j in range(col)] for i in range(row)]
