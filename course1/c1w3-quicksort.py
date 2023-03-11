import sys
from math import floor

COUNTER = 0

def main():

    # check argv
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".txt"):
        sys.exit("Must be a .txt file")
    else:
        try:
            array = []
            with open(sys.argv[1]) as file:
                for line in file:
                    array.append(int(line.strip()))

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

    quick_sort(array, 0, len(array) - 1)
    print(COUNTER)
    

def quick_sort(array, l, r):
    global COUNTER
    # base case
    if len(array[l:r + 1]) <= 1:
        return

    # pivot l
    # pivot = l

    # pivot r
    # pivot = r
    
    # pivot median
    m = int((r - floor((r - l + 1)/2)))
    choice = [array[l], array[m], array[r]]
    choice.remove(max(choice))
    choice.remove(min(choice))
    pivot = array.index(choice[0])

    # preprocess
    i = l + 1
    if pivot != l:
        array[l], array[pivot] = array[pivot], array[l]

    # partition
    for j in range(l + 1, r + 1):
        if array[j] < array[l]:
            array[i], array[j] = array[j], array[i]
            i += 1
    COUNTER += len(array[l:r + 1]) - 1
    # move pivot to the right place
    array[i - 1], array[l] = array[l], array[i - 1]
    
    # recursives
    quick_sort(array, l, i - 2)
    quick_sort(array, i, r)

    return array

if __name__ == "__main__":
    main()