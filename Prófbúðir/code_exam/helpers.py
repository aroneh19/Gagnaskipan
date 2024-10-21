from graphviz import Digraph
import solutions
from itertools import count
from PIL import Image
from IPython.display import SVG, display


def make_sll(lis):
    if len(lis) == 0:
        return None

    head = solutions.SLL_Node(lis[0])
    cur = head
    for el in lis[1:]:
        next_node = solutions.SLL_Node(el)
        cur.next = next_node
        cur = cur.next

    return head


def show_sentence_tree(tree):

    stack = [(None, tree.root)]

    net = Digraph()

    node_id_generator = count()

    while len(stack) > 0:
        parent, el = stack.pop()

        node_id = str(next(node_id_generator))

        net.node(name=node_id, label=el.word)

        if parent is not None:
            net.edge(tail_name=parent, head_name=node_id)

        for child in el.children:
            stack.append((node_id, child))

    svg = net.pipe(format="svg").decode("utf-8")

    return display(SVG(svg))

 


