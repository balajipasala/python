
def lostElement(A,B):

    C= set(A)
    D= set(B)

    if len(C) > len(D):
        print(set(C-D))
    else:
        print(set(D-C))


if __name__ == "__main__":
    A = [1, 4, 5, 7, 9]
    B = [4, 5, 7, 9]
    lostElement(A,B)