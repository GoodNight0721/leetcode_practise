class BrowserHistory:

    def __init__(self, homepage: str):
        self.stream = [homepage]
        self.ptr = 0

    def visit(self, url: str) -> None:
        self.stream = self.stream[:self.ptr + 1]
        self.stream.append(url)
        self.ptr += 1

    def back(self, steps: int) -> str:
        self.ptr -= steps
        self.ptr = max(0, self.ptr)
        return self.stream[self.ptr]

    def forward(self, steps: int) -> str:
        self.ptr += steps
        self.ptr = min(len(self.stream)-1, self.ptr)
        return self.stream[self.ptr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)