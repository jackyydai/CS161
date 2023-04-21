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


def DFSD(tree,d):
    if(type(tree) != tuple):
        return (tree,)
    if(d  <= 0):
        return tuple([node for node in reversed(tree) if type(node) != tuple])
    result = ()
    for node in reversed(tree): 
        result += DFSD(node, d-1)
    return result

def DFID(tree, d): 
    result = ()
    if(type(tree) != tuple):
        return (tree,)
    for i in range(d):
        result += DFSD(tree,i)
    return result


def main():
    # print(BFS("ROOT"))
    # print(BFS(((("L", "E"), "F"), "T")))
    # print(BFS(("R", ("I", ("G", ("H", "T"))))))
    # print(BFS((("A", ("B",)), ("C",), "D")))
    # print(BFS(("T", ("H", "R", "E"), "E")))
    # print(BFS(("A", (("C", (("E",), "D")), "B"))))

    # print(DFS("ROOT"))
    # print(DFS(((("L", "E"), "F"), "T")))
    # print(DFS(("R", ("I", ("G", ("H", "T"))))))
    # print(DFS((("A", ("B",)), ("C",), "D")))
    # print(DFS(("T", ("H", "R", "E"), "E")))
    print(DFSD(((("L", "E"), "F"), "T"), 3))
    # print(DFID(("R", ("I", ("G", ("H", "T")))), 4))
    # print(DFID(((("A", ("B",)), ("C",), "D")), 3))
    # print(DFID(("T", ("H", "R", "E"), "E"), 2))
    # print(DFID(("A", (("C", (("E",), "D")), "B")), 5))

    

if __name__ == "__main__":
    main()
