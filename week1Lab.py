# Part l
def linear_search(needle, haystack):
    haystack = sorted(haystack)
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return i
    # if the loop finishes, its not in haystack
    return None

print(linear_search(5, [6, 2, 8, 4]))
print(linear_search(8, [6, 2, 8, 4]))

# Part ll
def binary_search(needle, haystack):
    #sort the list
    haystack = sorted(haystack)
    #find the range 
    minn = 0
    maxx = len(haystack) - 1

    # search for middle and keep going tilkl found
    while minn <= maxx:
        #middle
        midd = (minn + maxx) // 2
        found = haystack[midd]

        if found == needle:
            return midd
        # if found is too low, look for abov the midd
        elif found < needle:
            minn = midd + 1
        # if found is too high, look below the midd
        elif found > needle:
            maxx = midd - 1
        # if the loop is complete needle is not in haystack
        else:
            return None
print(binary_search(8, [6, 2, 8, 4]))
print(binary_search(5, [6, 2, 8, 4]))


# Part 3
def linear_search_multi(needle, haystack):
    result = []
    for i in range(len(haystack)):
        if haystack[i] == needle:
            result.append(i)
    return result

print(linear_search_multi(5, [4, 5, 3, 5])) 
print(linear_search_multi(7, [4, 5, 3, 5]))  
