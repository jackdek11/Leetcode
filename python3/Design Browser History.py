class BrowserHistory:

    def __init__(self, homepage: str):
        self.history: list = []
        self.current_page: int = -1
        self.max_length: int = -1
        self.visit(homepage)


    def visit(self, url: str) -> None:
        self.current_page += 1
        if self.current_page < len(self.history):
            self.history[self.current_page] = url
        else:
            self.history.append(url)
        self.max_length = self.current_page
        

    def back(self, steps: int) -> str:
        self.current_page = max(0, self.current_page - steps)
        return self.history[self.current_page]


    def forward(self, steps: int) -> str:
        self.current_page = min(self.max_length, self.current_page + steps)
        return self.history[self.current_page]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)