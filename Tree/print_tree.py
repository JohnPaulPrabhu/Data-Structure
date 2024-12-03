from main import build_tree
from tree import BinaryTree


node = build_tree()
check = BinaryTree(node)

def print_tree(node):
    l = []
    for i in range(check.height(node)+1):
        l.append(check.height_print(node, 0, i))
    print(l)
    ran = len(l) * 2
    for i in l:
        if len(i) != 1:
            count = 0
            for j in i:
                if j is None:
                    j = "_"
                if count%2==0:
                    k="/"
                else:
                    k="\\"
                print(ran * ' ', k, end='')
                count+=1
        print()
        for j in i:
            if j is None:
                j = "-"
            print(ran * ' ', j, end='')
        print()
        ran = int(ran/2)

print(print_tree(node))