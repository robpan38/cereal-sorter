def check_all(results, state):
    result = True
    for s in results:
        if s != state:
            return False
    return result

results = [1, 1, 1]

print(check_all(results, 1))
results = [1, 1, 0]
print(check_all(results, 1))