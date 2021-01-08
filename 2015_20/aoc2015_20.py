class Sigma:
    def __init__(self):
        self.memory = {1: 1}

    def __call__(self, n):
        #return self.euler(n)
        return self.naive(n)

    def naive(self, n):
        s = 0
        for k in range(1,n+1):
            if not (n % k):
                s += k
        return s

    def euler(self, n):
        if n in self.memory:
            return self.memory[n]
        else:
            s = 0
            i = 1
            p = 1
            while p < n:
                #print("n={}, i = {}, p = {}".format(n,i,p))
                sig = self(n-p)
                s += (sig if i % 2 else -sig)
                i += 1
                p += 3*i - 2
            if p == n:
                s += (n if i % 2 else -n)
            i = -1
            p = 2
            while p < n:
                #print("n={}, i = {}, p = {}".format(n,i,p))
                sig = self(n-p)
                s += (sig if i % 2 else -sig)
                p -= 3*i - 2
                i -= 1
            if p == n:
                s += (n if i % 2 else -n)
        self.memory[n] = s
        return s


'''
sigma = Sigma()
for n in range(1,12):
    print(sigma(n))
print(sigma.memory)
'''

sigma = Sigma()

nump = 33100000
num = nump//10

n = 1   
while True:
    if sigma(n) >= num:
        break
    n += 1
print(n, sigma(n))