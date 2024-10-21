import helpers

class SLL_Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        if self.next == None:
            return str(self.data)
        return str(self.data) + " " + str(self.next)

       

    def __str__(self):
        return self.__repr__()

def nth_from_end_rec(head, n):
    if head is None:
        return (None, 0)

    val, num_returns = nth_from_end_rec(head.next, n)

    if num_returns == n:
        val = head.data
    
    return val, num_returns + 1


def nth_from_end(head, n):
    val, _ = nth_from_end_rec(head, n)
    return val


class SentenceTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = []


class SentenceTree:
    def __init__(self):
        self.root = SentenceTreeNode("")
    
    def store_sentence(self, sentence):
        #this line helps you match the sentence to the tree structure
        sentence_list = sentence.split()

        curr_node = self.root
        for word in sentence_list:

            found_node = False
            for child in curr_node.children:
                if child.word == word:
                    curr_node = child
                    found_node = True
                    break

            if not found_node:
                new_node = SentenceTreeNode(word)
                curr_node.children.append(new_node)
                curr_node = new_node
           

    def contains_sentence(self, sentence):
        #the lines below help you match the sentence to the tree structure
        sentence_list = sentence.split()    

        curr_node = self.root

        for word in sentence_list:

            found_node = False
            for child in curr_node.children:
                if child.word == word:
                    curr_node = child
                    found_node = True
                    break

            if not found_node:
                return False
        
        return True



if __name__ == "__main__":
    print("testing nth from end")
    l = list(range(10, -1, -1))
    sll = helpers.make_sll(l)

    print(nth_from_end(sll, 2))

    print(l)
    for i in range(len(l)):
        print(f"{i}th from end: {nth_from_end(sll, i)}, expected {l[len(l) - i - 1]}")
