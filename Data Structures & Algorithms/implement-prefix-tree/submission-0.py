class node:
    def __init__(self):
        self.children= {}
        self.endofword = False

class PrefixTree:
    def __init__(self):
        self.root = node()
    def insert(self, word: str) -> None:
        temp = self.root
        for i in word:
            newnode = node()
            if i not in temp.children:
                temp.children[i] = newnode
            temp = temp.children[i]
            print(temp.children)
        temp.endofword = True
    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        if not temp.endofword:
            return False
        return True
    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if i not in temp.children:
                return False
            temp = temp.children[i]
        return True

        
        