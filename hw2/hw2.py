#Overall comment: For BFS and DFS I either used a stack or queue to implement the searches. 
#For BFS I used a stack queue implentation where I would expand/process the nodes based on
#the node at the top of the queue. For the DFS, It has the same implementation except I would
#expand/process nodes based on the top of the stack. For the depth-first iterative-deepening search
#I used a heaper funtion that runs depth fisrt search until d depth. With that helper funtion I, I would
#run a for loop that calls the helper funtion with increasing depth. For the problem stated by Homer Simpson 
#show, I implemented it based on the framwork provided. I would check if the current state is the goal state, 
#If it is I would return the path, if not I would continue to expand/ check for the goal state. 

#BFS takes in one agrument tree being the root of a tuple tree. It returns a tuple of 
#leaf nodes in the order they are visited by left-to-right breadth-first search.
def BFS(tree):
    queue = []
    queue.append(tree)
    result = []
    while(queue):
        s = queue.pop(0)
        if(type(s) != tuple):
            result.append(s)
        else:
            for node in s:
                queue.append(node)
    return tuple(result)

#DFS takes in one agrument tree being the root of a tuple tree. It returns a tuple of 
#leaf nodes in the order they are visited by left-to-right depth-first search.
def DFS(tree):
    stack = []
    stack.append(tree)
    result = []
    while(stack):
        s = stack.pop()
        if(type(s) != tuple):
            result.append(s)
        else:
            for node in reversed(s):
                stack.append(node)
    return tuple(result)

#DFSD stands for Depth First Search until D. DFSD takes two arguemnts tree being the root of a tuple tree and d being the 
#max depth this search will recurse into. It returns tuple of leaf nodes in the order they are visited by right-to-left
#depth-first search until depth d.
def DFSD(tree,d):
    if(type(tree) != tuple):
        return (tree,)
    if(d  <= 0):
        return tuple([node for node in reversed(tree) if type(node) != tuple])
    result = ()
    for node in reversed(tree): 
        result += DFSD(node, d-1)
    return result


#DFID takes two arguments, a tuple tree representing the root of a tuple tree and an integer d representing the depth of
#tree, and returns a tuple of leaf nodes in the order they are visited by a right-to-left depth-first iterative-deepening
# search
def DFID(tree, d): 
    result = ()
    if(type(tree) != tuple):
        return (tree,)
    for i in range(d):
        result += DFSD(tree,i)
    return result

# These functions implement a depth-first solver for the homer-baby-dog-poison
# problem. In this implementation, a state is represented by a single tuple
# (homer, baby, dog, poison), where each variable is True if the respective entity is
# on the west side of the river, and False if it is on the east side.
# Thus, the initial state for this problem is (False False False False) (everybody
# is on the east side) and the goal state is (True True True True).

# The main entry point for this solver is the function DFS_SOL, which is called
# with (a) the state to search from and (b) the path to this state. It returns
# the complete path from the initial state to the goal state: this path is a
# list of intermediate problem states. The first element of the path is the
# initial state and the last element is the goal state. Each intermediate state
# is the state that results from applying the appropriate operator to the
# preceding state. If there is no solution, DFS_SOL returns [].
# To call DFS_SOL to solve the original problem, one would call
# DFS_SOL((False, False, False, False), [])
# However, it should be possible to call DFS_SOL with any intermediate state (S)
# and the path from the initial state to S (PATH).

# First, we define the helper functions of DFS_SOL.

# FINAL_STATE takes a single argument S, the current state, and returns True if it
# is the goal state (True, True, True, True) and False otherwise.
def FINAL_STATE(S):
    return S == (True, True, True, True) 


# NEXT_STATE returns the state that results from applying an operator to the
# current state. It takes two arguments: the current state (S), and which entity
# to move (A, equal to "h" for homer only, "b" for homer with baby, "d" for homer
# with dog, and "p" for homer with poison).
# It returns a list containing the state that results from that move.
# If applying this operator results in an invalid state (because the dog and baby,
# or poisoin and baby are left unsupervised on one side of the river), or when the
# action is impossible (homer is not on the same side as the entity) it returns [].
# NOTE that NEXT_STATE returns a list containing the successor state (which is
# itself a tuple)# the return should look something like [(False, False, True, True)].
# (homer, baby, dog, poison)
def NEXT_STATE(S, A):
    if A == "h":
        result = (not S[0], S[1],S[2],S[3]) #posible moves
    elif A  == "b" and (S[0] == S[1]): 
        result =  (not S[0], not S[1],S[2],S[3])
    elif A == "d" and (S[0] == S[2]):
        result =  (not S[0], S[1], not S[2],S[3])
    elif A == "p" and (S[0] == S[3]):
        result =  (not S[0], S[1],  S[2], not S[3])
    else:
        return []
    if (result[1] == result[2] or result[1] == result[3]) and result[0] != result[1]: # if baby is left with dog or posion unsupervized
        return []
    return [result]


# SUCC_FN returns all of the possible legal successor states to the current
# state. It takes a single argument (S), which encodes the current state, and
# returns a list of each state that can be reached by applying legal operators
# to the current state.
def SUCC_FN(S):
    return NEXT_STATE(S, 'h') + NEXT_STATE(S, 'b')  + NEXT_STATE(S, 'd') + NEXT_STATE(S, 'p')


# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if S is a member of
# STATES and False otherwise.
def ON_PATH(S, STATES):
    return S in STATES



# MULT_DFS is a helper function for DFS_SOL. It takes two arguments: a list of
# states from the initial state to the current state (PATH), and the legal
# successor states to the last, current state in the PATH (STATES). PATH is a
# first-in first-out list of states# that is, the first element is the initial
# state for the current search and the last element is the most recent state
# explored. MULT_DFS does a depth-first search on each element of STATES in
# turn. If any of those searches reaches the final state, MULT_DFS returns the
# complete path from the initial state to the goal state. Otherwise, it returns
# [].
def MULT_DFS(STATES, PATH):
    if FINAL_STATE(PATH[-1]):
        return PATH
    for S in STATES:
        if(not ON_PATH(S, PATH)):
            return MULT_DFS(SUCC_FN(S), PATH + [S])
    return []

# DFS_SOL does a depth first search from a given state to the goal state. It
# takes two arguments: a state (S) and the path from the initial state to S
# (PATH). If S is the initial state in our search, PATH is set to []. DFS_SOL
# performs a depth-first search starting at the given state. It returns the path
# from the initial state to the goal state, if any, or [] otherwise. DFS_SOL is
# responsible for checking if S is already the goal state, as well as for
# ensuring that the depth-first search does not revisit a node already on the
# search path (i.e., S is not on PATH).
def DFS_SOL(S, PATH):
    if(FINAL_STATE(S)):
        return PATH + [S]
    if(ON_PATH(S, PATH)):
        return []
    return MULT_DFS(SUCC_FN(S), PATH + [S])

def main():

    test_1 = ("ROOT")
    test_2 = (((("L", "E"), "F"), "T"))
    test_3 = (("R", ("I", ("G", ("H", "T")))))
    test_4 = (("A", ("B",)), ("C",), "D")
    test_5 = ("T", ("H", "R", "E"), "E")
    test_6 = ("A", (("C", (("E",), "D")), "B"))

    li = [test_1, test_2, test_3, test_4, test_5, test_6]

    print("BFS TEST:")
    for i in li:
        print(BFS(i))

    print("DFS TEST:")
    for j in li:
        print(DFS(j))

    print("DFID TEST:")

    print(DFID("ROOT", 0))
    print(DFID(((("L", "E"), "F"), "T"), 3))
    print(DFID(("R", ("I", ("G", ("H", "T")))), 4))
    print(DFID(((("A", ("B",)), ("C",), "D")), 3))
    print(DFID(("T", ("H", "R", "E"), "E"), 2))
    print(DFID(("A", (("C", (("E",), "D")), "B")), 5))

    print("HOMER TEST:")
    print(FINAL_STATE((False, True, True, True)))
    print(FINAL_STATE((True, True, True, True)))

    states = ["h", "b", "d", "p"]
    start = (False, False, False, False)
    start_li = []
    start_li.append(start)

    start_2 = (True, True, False, False)

    start_3 = (False, True, False, False)

    start_4 = (True, True, True, False)
    start_4_list = [(False, False, False, False), (True, True,
                                                   False, False), (False, True, False, False), (True, True, True, False)]

    start_5 = (True, False, False, True)
    start_5_list = []

    start_6 = (True, True, False, True)
    start_6_list = [(False, False, False, False), (True, True,
                                                   False, False), (False, True, False, False)]

    start_7 = (True, True, True, True)
    start_7_li = [(False, False, False, False), (True, True, False, False), (False, True, False, False), (True,
                                                                                                          True, False, True), (False, False, False, True), (True, False, True, True), (False, False, True, True)]

    start_8 = (True, True, True, True)
    start_8_li = [(False, False, False, False), (True, True, False, False), (False, True, False, False), (False, True, False,
                                                                                                          False), (True, True, False, True), (False, False, False, True), (True, False, True, True), (False, False, True, True)]

    print("-----i-----")
    for i in states:
        print(NEXT_STATE(start, i))

    print("i successor function")
    print(SUCC_FN(start))

    print("-----j-----")
    for j in states:
        print(NEXT_STATE(start_2, j))
    print("j successor function")
    print(SUCC_FN(start_2))

    print("-----k-----")
    for k in states:
        print(NEXT_STATE(start_3, k))
    print("k successor function")
    print(SUCC_FN(start_3))

    print("Helper Function Test")
    print(MULT_DFS(SUCC_FN(start), start_li))

    print("Regular Function Test:")
    print(DFS_SOL(start, []))
    print(DFS_SOL(start_4, start_4_list))
    print(DFS_SOL(start_6, start_6_list))
    print(DFS_SOL(start_7, start_7_li))
    print(DFS_SOL(start_8, start_8_li))


if __name__ == "__main__":
    main()
