class MyQueue:
    def __init__(self):
        self.items = []
        self.rev = []
        
    def _pour(self, source, dest):
        while source:
            dest.append(source.pop())

    def push(self, x: int) -> None:
        self.items.append(x)
        
    def pop(self) -> int:
        if not self.empty():
            self._pour(self.items, self.rev)
            element = self.rev.pop()
            self._pour(self.rev, self.items)
            return element
            
    def peek(self) -> int:
        if not self.empty():
            self._pour(self.items, self.rev)
            element = self.rev[-1] 
            self._pour(self.rev, self.items)
            return element
            
    def empty(self) -> bool:
        return len(self.items) == 0