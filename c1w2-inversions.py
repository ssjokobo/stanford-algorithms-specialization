import sys
from math import ceil

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
            input_array = []
            with open(sys.argv[1]) as file:
                for line in file:
                    input_array.append(int(line.strip()))

            size = len(input_array)

            print(sort_count(input_array, size))

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

def sort_count(array, size):
    if size == 1:
        return array, 0
        
    resize = int(ceil(size/2))
    
    B, X = sort_count(array[:resize], len(array[:resize]))
    C, Y = sort_count(array[resize:], len(array[resize:]))
    Z = X + Y

    for k in range(size):
        try:
            if B[0] < C[0]:
                array[k] = B.pop(0)
            else:
                array[k] = C.pop(0)
                Z += len(B)
        except IndexError:
            if len(B) == 0:
                array = array[:k] + C
                break
            else:
                array = array[:k] + B
                break
            
    return array, Z

def sort_count_split(array, size):
    pass

if __name__ == "__main__":
    main()