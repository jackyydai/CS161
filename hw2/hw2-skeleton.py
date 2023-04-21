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
    # raise NotImplementedError


# ON_PATH checks whether the current state is on the stack of states visited by
# this depth-first search. It takes two arguments: the current state (S) and the
# stack of states visited by DFS (STATES). It returns True if S is a member of
# STATES and False otherwise.
def ON_PATH(S, STATES):
    return S in STATES
    # raise NotImplementedError 


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
    # PATH.append(S)
    return MULT_DFS(SUCC_FN(S), PATH + [S])





def main():
    # print(FINAL_STATE((True, True, True, True)))
    # print(FINAL_STATE((True, False, True, True)))
    # # print(NEXT_STATE((False, False, False ,False), 'h'))
    # # print(NEXT_STATE((False, False, False ,False), 'b'))
    # # print(NEXT_STATE((False, False, False ,False), 'd'))
    # # print(NEXT_STATE((False, False, False ,False), 'p'))
    # print(SUCC_FN((True, True, False, False)))
    # print(ON_PATH((False, False,False, False), [(False, True, False, False), (False, False, False, False)]))
    print(DFS_SOL((False, False, False, False) , []))

    

if __name__ == "__main__":
    main()