class ParserError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)

class Node:
    def __init__(self, token:str):
        self._token = token 
        self._node = {}
        self.exec = None 
    
    def addFn(self, fn):
        self.exec = fn

    def addNode(self, token:str):
        if not token.isdigit():
            self._node[token] = Node(token)
            return self._node[token]

    def next(self, token):
        try:
            return self._node[token]
        except KeyError:
            raise ParserError("Syntax Error")

class Parser:
    
    def __init__(self):
        self.root = Node(None)
    
    def addCommand(self, cmd:str, fn):
        tokens = cmd.split()
        current = self.root 
        while len(tokens) > 0:
            curr_t = tokens.pop(0)
            try:
                current = current.next(curr_t)
            except:
                current = current.addNode(curr_t)
        current.addFn(fn)

    def exec(self, cmd:str):
        tokens = cmd.split()
        current = self.root 
        args = []
        isGreedy = False
        glob = []
        while len(tokens) > 0:
            curr_t = tokens.pop(0)
            if isGreedy:
                glob.append(curr_t)
            else:
                try:
                    current = current.next(curr_t)
                except ParserError:
                    try:
                        current = current.next("<*>")
                    except ParserError:
                        try:
                            current = current.next("<str>")
                        except ParserError:
                            raise ParserError
                        else:
                            args.append(curr_t)
                    else:
                        isGreedy = True
                        glob.append(curr_t)
        if isGreedy:
            args.append(" ".join(glob))
        if len(args) > 0:
            msg1, msg2 = current.exec(*args)
        else:
            msg1, msg2 = current.exec()
        return msg1, msg2
                    