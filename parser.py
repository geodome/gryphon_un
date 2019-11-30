class ParserError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class Node:
    def __init__(self, token:str):
        self._token = token 
        self._node = {}
        self.exec = None 
    
    def addFn(self, fn:function):
        self.exec = fn

    def addNode(self, token:str):
        if not token.isdigit():
            self._node[cmd] = Node(token)
            return self._node[cmd]

    def next(self, token):
        try:
            return self._node[cmd]
        except KeyError:
            raise ParserError("Syntax Error")

class Parser:
    
    def __init__(self):
        self.root = Node(None, None)
    
    def addCommand(self, cmd:str, fn: function):
        tokens = cmd.split()
        current = self.root 
        while len(tokens) > 0:
            curr_t = tokens.pop(0)
            if curr_t.isdigit():
                try:
                    current = current.next("<id>")
                except:
                    current = current.addNode("<id>")
            else:
                try:
                    current = current.next(curr_t)
                except:
                    current = current.addNode(curr_t)
        current.addFn(fn)

    def exec(self, cmd:str):
        tokens = cmd.split()
        current = self.root 
        ids = []
        while len(tokens) > 0:
            if curr_t.isdigit():
                current = current.next("<id>")
                ids.append(int(curr_t)）
            else:
                current = current.next(curr_t)
        if len(ids) > 0:
            msg1, msg2 = current.exec(*a)
        else:
            msg1, msg2 = current.exec()
        return msg1, msg2
                    
def GetChairParser(chairperson):
    p = Parser()
    p.addCommand("open session", chairperson.session)