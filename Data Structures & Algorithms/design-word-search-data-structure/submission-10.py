class Node:
    def __init__(self,val = None,end = False):
        self.val = val
        self.end = end 
        self.children = {}
class WordDictionary:
    def __init__(self):
        self.root = Node("root")

    def addWord(self, word: str) -> None:
        head = self.root
        for i in range(len(word)):
            val = word[i]
            itend = True if i == len(word) - 1 else False
            node = Node(val,itend)
            if val not in head.children:
                head.children[val] = node
            head = head.children[val]
        head.end = True

    def search(self, word: str) -> bool:
        def rec(node,ind):
            if ind == len(word):
                return node.end
            if word[ind] in node.children:
                return rec(node.children[word[ind]],ind + 1)
            else:
                if word[ind] == ".":
                    for child in node.children:
                         temp =  rec(node.children[child], ind + 1)
                         if temp:
                            return True
                    return False
                else:
                    return False
        return rec(self.root,0)
            
    
