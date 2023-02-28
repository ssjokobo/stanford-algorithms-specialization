import sys
from tqdm import tqdm

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
            H = dict()
            with open(sys.argv[1]) as file:
                for line in file:
                    H[int(line.strip())] = 1

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        
        n = 0
        for t in tqdm(range(-10000, 10001)):
            if two_sum(H, t):
                n += 1
        
        print(n)


def two_sum(h, t):
    for x in h.keys():
        y = t - x
        if y in h and y != x:
            return True
    
    return False

if __name__ == "__main__":
    main()