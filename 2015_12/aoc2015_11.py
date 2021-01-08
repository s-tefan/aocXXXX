"""The naive way..."""
"""But I solved part one by inspection"""

class Password:
    def __init__(self, word):
        self.word = word

    def check(self):
        if len(self.word) == 8:
            for c in self.word:
                if c in {'iol'}:
                    return False
            tripleflag = False
            pairflag = 0
            lastpair = ''
            if self.word[0] == self.word[0]:
                pairflag = 1
            for k, c in enumerate(reversed(self.word[2:])):
                pairflag += self.word[k-1] == c != lastpair
                tripleflag = tripleflag or ord(self.word[-k-1]) == ord(c) - 1 and ord(self.word[-k-2]) == ord(c) - 2
                if tripleflag and pairflag >= 2:
                    return True
        return False

    def increase(self):
        def increased(s):
            if s == '':
                return None
            if s[-1] == 'z':
                return increased(s[:-1]) + 'a'
            else:
                return s[:-1] + chr(ord(s[-1]) + 1)
        self.word = increased(self.word)
        #print(self.word)

    def next(self):
        while not self.check():
            self.increase()
        return self


pw = Password('hepxcrrq')
print(pw.next().word)
print(pw.next().word)
