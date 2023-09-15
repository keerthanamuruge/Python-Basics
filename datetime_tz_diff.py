def permutations(arr):
    if len(arr) == 0:
        return [[]]

    if len(arr) == 1:
        return [arr]

    perms = []
    for i in range(len(arr)):
        print(arr, "arr")
        rest = arr[:i] + arr[i + 1:]
        print(rest, "rest")
        for p in permutations(rest):
            perms.append([arr[i]] + p)
            print(perms, "perm")

    return perms
# permutations([1,2,3,4])

def generate_permutations(arr):
    n = len(arr)
    if n == 0:
        return [[]]

    # Initialize a list to store permutations
    permutations = [[]]

    for i in range(n):
        current_element = arr[i]
        new_permutations = []

        for perm in permutations:
            print(perm, "prem")
            for j in range(len(perm) + 1):
                new_perm = perm[:j] + [current_element] + perm[j:]
                print(new_perm,perm[:j], [current_element] + perm[j:], current_element, "per")
                new_permutations.append(new_perm)

        permutations = new_permutations

    return permutations
print(generate_permutations([1,2,3,4]))