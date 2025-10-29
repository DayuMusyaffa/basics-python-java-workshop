class Counter:
    count = 0  # class variable

    def __init__(self):
        self.count = 0  # instance variable
        Counter.count += 1

    def increment(self):
        self.count += 1

def hello():
    print("Hello, World!")

c1 = Counter()
print(c1.count)  # 0
print(Counter.count)  # 1
c1.increment()
print(c1.count)  # 1

c2 = Counter()
print(c2.count)  # 0
print(Counter.count)  # 2

hello()  # Hello, World!
# test push