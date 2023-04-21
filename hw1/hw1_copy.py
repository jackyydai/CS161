
#Overall I used recursion to create the solution for each of these problems. 
#For each there is a base case so that the recursion can eventually converge
#For PAD and SUMS, they converge when n = 0, 1, or 2. For ANON, TREE_HEIGHT, and
#TREE_ORDER, the base case is when the input is no longer a tuple. When it is not the base case
#it would use recursively call itself each in a way that would solve the problem.  


#PAD takes in one arguement N, an integer greater than 1
#It returns an integer that represents the Nth Padovan number by adding the previous 2 Padovan numbers. 
def PAD(N):
    if N == 0 or N == 1 or N == 2:
        return 1
    else:
        return PAD(N - 2) + PAD(N - 3)

#SUMS takes in one arguement N, an integer greater than 1
#It returns an integer that represents the number of additions required for PAD to find the Nth Padovan number
def SUMS(N):
    if N == 0 or N == 1 or N == 2:
        return 0
    else:
        return SUMS(N-2) + SUMS(N-3)  + 1 

#ANON takes in one argument TREE, a tuple that represents a TREE
#It returns a tuple, that represents the anonymized TREE with the same structure as TREE
def ANON(TREE): 
    if(type(TREE) != tuple):
        return '?'
    return tuple([ANON(node) for node in TREE])

#TREE_HEIGHT takes in one argument TREE, a tuple that represents a TREE
#It returns the length of the longest path from the root node to the farthest leaf node of TREE
def TREE_HEIGHT(TREE):
    if(type(TREE) != tuple):
        return 0
    return max([TREE_HEIGHT(node) for node in TREE]) + 1

#TREE_HEIGHT takes in one argument TREE, a tuple that represents a TREE
#It returns the postorder traversal of the numbers in TREE
def TREE_ORDER(TREE):
    if(type(TREE) != tuple):
        return (TREE,)
    return TREE_ORDER(TREE[0]) + TREE_ORDER(TREE[2]) + TREE_ORDER(TREE[1])

    
    

# def main():
#     for i in range(10):
#         print(PAD(i))
#     for i in range(10):
#         print(SUMS(i))
#     # print(SUMS(3))



#     print(ANON("FOO"))
#     print(ANON(((("L", "E"), "F"), "T")))
#     print(ANON((5, "FOO", 3.1, -0.2)))
#     print(ANON((1, ("FOO", 3.1), -0.2)))
#     print(ANON((((1, 2), ("FOO", 3.1)), ("BAR", -0.2))))
#     print(ANON(("R", ("I", ("G", ("H", "T"))))))


#     print(TREE_HEIGHT(1))
#     print(TREE_HEIGHT((5, "FOO", 3.1, -0.2)))
#     print(TREE_HEIGHT((1, ("FOO", 3.1), -0.2)))
#     print(TREE_HEIGHT(("R", ("I", ("G", ("H", "T"))))))

#     print(TREE_ORDER(42))
#     print(TREE_ORDER(((1, 2, 3), 7, 8)))
#     print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))

# if __name__ == "__main__":
#     main()
if __name__ == "__main__":
    print("Hello")

    print(PAD(5))
    print(PAD(3))
    print(PAD(4))
    print(PAD(20))
    print(PAD(11))

    print(SUMS(5))
    print(SUMS(10))
    print(SUMS(7))

    test_case_1 = 42
    test_case_2 = "FOO"
    test_case_3 = (((("L", "E"), "F"), "T"))
    test_case_4 = ((5, "FOO", 3.1, -0.2))
    test_case_5 = ((1, ("FOO", 3.1), -0.2))
    test_case_6 = ((((1, 2), ("FOO", 3.1)), ("BAR", -0.2)))
    test_case_7 = (("R", ("I", ("G", ("H", "T")))))

    print(TREE_HEIGHT(test_case_1))
    print(TREE_HEIGHT(test_case_4))
    print(TREE_HEIGHT(test_case_5))
    print(TREE_HEIGHT(test_case_7))

    print(TREE_ORDER(test_case_1))
    print(TREE_ORDER(((1, 2, 3), 7, 8)))
    print(TREE_ORDER(((3, 7, 10), 15, ((16, 18, 20), 30, 100))))

    print("Goodbye")
