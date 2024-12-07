class SymbolTable:
    def __init__(self):
        self.symbol_tables = dict()
        self.scopes = dict()
        self.funcDict = dict()

    def insert_symbol(self, symbol_name, symbol_node, scope):
        set = {symbol_name: symbol_node}
        if scope in self.symbol_tables:
            self.symbol_tables[scope].update(set)
        else:
            self.symbol_tables[scope] = set
        if scope not in self.scopes:
            self.scopes[scope] = [None]

    def insert_value(self, symbol_name, value, scope):
        if scope in self.symbol_tables:
            if symbol_name in self.symbol_tables[scope]:
                self.symbol_tables[scope][symbol_name][2] = value
            else:
                arr = self.scopes[scope]
                if arr != None:
                    for i in arr:
                        if i in self.symbol_tables:
                            if symbol_name in self.symbol_tables[i]:
                                self.symbol_tables[i][symbol_name][2] = value
                else:
                    if None in self.symbol_tables:
                        if symbol_name in self.symbol_tables[None]:
                            self.symbol_tables[None][symbol_name][2] = value

        else:
            arr = self.scopes[scope]
            if arr != None:
                for i in arr:
                    if i in self.symbol_tables:
                        if symbol_name in self.symbol_tables[i]:
                            self.symbol_tables[i][symbol_name][2] = value
            else:
                if None in self.symbol_tables:
                    if symbol_name in self.symbol_tables[None]:
                        self.symbol_tables[None][symbol_name][2] = value



    def get_symbol(self, symbol_name, scope):
        if scope in self.symbol_tables:
            if symbol_name in self.symbol_tables[scope]:
                return self.symbol_tables[scope][symbol_name]
            else:
                check = False
                if scope == None:
                    check = True
                if check or scope[:12] == "unNamedScope" or scope[:11] == "ifStatement" or scope[:13] == "elifStatement" or scope[:13] == "elseStatement" or scope[:14] == "whileStatement" or scope[:7] == "forLoop":
                    arr = self.scopes[scope]
                    if arr != None:
                        for i in arr:
                            if i in self.symbol_tables:
                                if symbol_name in self.symbol_tables[i]:
                                    return self.symbol_tables[i][symbol_name]
                    else:
                        if None in self.symbol_tables:
                            if symbol_name in self.symbol_tables[None]:
                                return self.symbol_tables[None][symbol_name]
                else:
                    if None in self.symbol_tables:
                        if symbol_name in self.symbol_tables[None]:
                            return self.symbol_tables[None][symbol_name]
                    return None
            return None
        else:
            check = False
            if scope == None:
                check = True
            if check or scope[:12] == "unNamedScope" or scope[:11] == "ifStatement" or scope[:13] == "elifStatement" or scope[:13] == "elseStatement" or scope[:14] == "whileStatement" or scope[:7] == "forLoop":
                if scope in self.scopes:
                    arr = self.scopes[scope]
                    if arr != None:
                        for i in arr:
                            if i in self.symbol_tables:
                                if symbol_name in self.symbol_tables[i]:
                                    return self.symbol_tables[i][symbol_name]
                    else:
                        if None in self.symbol_tables:
                            if symbol_name in self.symbol_tables[None]:
                                return self.symbol_tables[None][symbol_name]
            else:
                if None in self.symbol_tables:
                    if symbol_name in self.symbol_tables[None]:
                        return self.symbol_tables[None][symbol_name]
                return None
            return None
