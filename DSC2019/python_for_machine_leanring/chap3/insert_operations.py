def insert_operation(N, arr, ops):
    # given op1(currently calculated), arr(remained number), ops(remained ops),
    # return all possible values
    def recur(op1, arr, ops):
        if not arr:
            return [op1]

        results = []
        op2 = arr[0]
        for i, op in enumerate(ops):
            if op == 0:
                continue

            new_ops = ops[:]
            new_ops[i] -= 1

            if i == 0:
                value = op1 + op2
            elif i == 1:
                value = op1 - op2
            elif i == 2:
                value = op1 * op2
            elif i == 3:
                value = divmod(op1 ,op2)[0] if op1 >= 0 else -divmod(-op1 ,op2)[0]

            results.extend(recur(value, arr[1:], new_ops))

        return [min(results), max(results)]

    result = recur(arr[0], arr[1:], ops)
    print(max(result))
    print(min(result))

if __name__ == '__main__':
    N = int(input())
    arr = [int(x) for x in input().split()]
    ops = [int(x) for x in input().split()]
    insert_operation(N, arr, ops)