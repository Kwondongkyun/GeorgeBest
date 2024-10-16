def print_pyramid(n: int):
    # TODO: implement this function
    raise NotImplementedError


def print_inverted_pyramid(n: int):
    # TODO: implement this function
    for i in range(1,n):
        print(" "*(i) + "*"*(2*(n-i)-1))
    raise NotImplementedError


if __name__ == "__main__":
    N = input()
    print_pyramid(N)
    print_inverted_pyramid(N)