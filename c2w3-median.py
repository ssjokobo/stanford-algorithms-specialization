import sys
from heapq import heappop, heappush
    

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
            with open(sys.argv[1]) as file:
                data = [int(line.strip()) for line in file]
            
            top_heap = []
            bottom_heap = []
            medians = [get_median(top_heap, bottom_heap, x) for x in data]

            answer = sum(medians) % 10000
            print(answer)

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def get_median(top_heap, bottom_heap, x):
    if not bottom_heap:
        heappush(bottom_heap, -x)
    else:
        if -bottom_heap[0] < x:
            heappush(top_heap, x)
            if len(bottom_heap) < len(top_heap):
                heappush(bottom_heap, -heappop(top_heap))
        else:
            heappush(bottom_heap, -x)
            if len(bottom_heap) > len(top_heap) + 1:
                heappush(top_heap, -heappop(bottom_heap))

    return -bottom_heap[0]


if __name__ == "__main__":
    main()