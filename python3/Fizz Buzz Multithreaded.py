from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.c = 1
        self.lock1 = Lock()
        self.lock2 = Lock()
        self.lock3 = Lock()
        self.lock4 = Lock()
        
        self.lock1.acquire()
        self.lock2.acquire()
        self.lock3.acquire()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        self.func(printFizz, self.lock1)
    	

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        self.func(printBuzz, self.lock2)
    	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        self.func(printFizzBuzz, self.lock3)
        

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            self.lock4.acquire()
            if self.c >= self.n + 1:
                break
            printNumber(self.c)
            self.release()
        self.lock4.release()
    
    def func(self, f, l):
        while True:
            l.acquire()
            if self.c >= self.n + 1:
                break
            f()
            self.release()
        l.release()
    
    def release(self):
        self.c += 1
        if self.c >= self.n + 1:
            self.lock1.release()
            self.lock2.release()
            self.lock3.release()
            self.lock4.release()
        elif self.c % 15 == 0:
            self.lock3.release()
        elif self.c % 3 == 0:
            self.lock1.release()
        elif self.c % 5 == 0:
            self.lock2.release()
        else:
            self.lock4.release()