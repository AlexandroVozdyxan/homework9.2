def difference(*args):
    if not args:
        return 0
    else:
        max_value = max(args)
        min_value = min(args)
        result = max_value - min_value
        result = round(result, 2)

        return result
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print("OK")
print(difference(-111, 3, 5, 100))
print(difference(2222, 1, 434, 23))
