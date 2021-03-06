class FuncForOptions:
    def __init__(self, collection, caretaker):
        self.collection = collection
        self.caretaker = caretaker

    @staticmethod
    def getId(methodName):
        print(f"Id for {methodName}:")
        id = input()
        return id

    @staticmethod
    def getPath(isInPath=False, isOutPath=False):
        inPath, outPath = "", ""
        if isInPath:
            print("Write path to input data:")
            inPath = input()
        if isOutPath:
            print("Write path to output data:")
            outPath = input()
        return inPath, outPath

    def f1(self):
        print("String for find:")
        str = input()
        self.collection.find(str)

    def f2(self):
        print("Attribute for sort:")
        attr = input()
        self.collection.sort(attr)

    def f3(self):
        id = self.getId("delete")
        inPath, outPath = self.getPath()
        self.collection.delete(id, outPath)

    def f4(self):
        inPath, outPath = self.getPath(True)
        self.collection.add(inPath, outPath)

    def f5(self):
        id = self.getId("change")
        inPath, outPath = self.getPath(True)
        self.collection.change(id, inPath, outPath)

    def f6(self):
        self.collection.show()

    def f7(self):
        self.caretaker.addMemento()

    def f8(self):
        self.caretaker.undo()

    def f9(self):
        self.caretaker.redo()

    def f10(self):
        self.caretaker.show()

    def f0(self):
        exit()