import time

def rotate(text):
    rotations = []
    for char in text:
        text = text[-1] + text[:-1]
        rotations.append(text)
    return rotations

def matrix(text):
    
    return sorted(rotate(text))

def get_transform(text):
    return ''.join([t[-1] for t in matrix(text)]), text.find("$")

def get_f(text):
    return [t[1] for t in matrix(text)]


def suffixArray(s):
    satups = sorted([(s[i:], i) for i in range(len(s))])
    return list(map(lambda x: x[1], satups)) 

def bwtFromSa(t, sa=None):
    bw = []
    dollarRow = None
    if sa is None:
        sa = suffixArray(t)
    for si in sa:
        if si == 0:
            dollarRow = len(bw)
            bw.append('$')
        else:
            bw.append(t[si-1])
    return ''.join(bw), dollarRow 

class FmCheckpoints(object):

    def __init__(self, bw, cpIval=4):

        self.cps = {}        
        self.cpIval = cpIval 
        tally = {}          
        for c in bw:
            if c not in tally:
                tally[c] = 0
                self.cps[c] = []
        
        for i, c in enumerate(bw):
            tally[c] += 1 
            if i % cpIval == 0:
                for c in tally.keys():
                    self.cps[c].append(tally[c])

    def rank(self, bw, c, row):
        
        if row < 0 or c not in self.cps:
            return 0
        i, nocc = row, 0
        
        while (i % self.cpIval) != 0:
            if bw[i] == c:
                nocc += 1
            i -= 1
        return self.cps[c][i // self.cpIval] + nocc


class FmIndex():
    
    @staticmethod
    def downsampleSuffixArray(sa, n=4):
        ssa = {}
        for i, suf in enumerate(sa):
            if suf % n == 0:
                ssa[i] = suf
        return ssa
    
    def __init__(self, t, cpIval=4, ssaIval=4):
        time1 = time.time()
        t = t[:-2]
        if t[-1] != '$':
            t += '$'
        sa = suffixArray(t)
        self.bwt, self.dollarRow = get_transform(t)
        self.ssa = self.downsampleSuffixArray(sa, ssaIval)
        self.slen = len(self.bwt)
        
        self.cps = FmCheckpoints(self.bwt, cpIval)
        
        tots = dict()
        for c in self.bwt:
            tots[c] = tots.get(c, 0) + 1
        
        self.first = {}
        totc = 0
        for c, count in sorted(tots.items()):
            self.first[c] = totc
            totc += count
        time2 = time.time()
        print(f"Création de l'index : {time2-time1}")
        self.create_time = time2 - time1
    
    def count(self, c):
        
        if c not in self.first:
            
            for cc in sorted(self.first):
                if c < cc: return self.first[cc]
            return self.first[cc]
        else:
            return self.first[c]
    
    def range(self, p):
        
        l, r = 0, self.slen - 1 
        for i in range(len(p)-1, -1, -1): 
            l = self.cps.rank(self.bwt, p[i], l-1) + self.count(p[i])
            r = self.cps.rank(self.bwt, p[i], r)   + self.count(p[i]) - 1
            if r < l:
                break
        return l, r+1
    
    def resolve(self, row):
        
        def stepLeft(row):
        
            c = self.bwt[row]
            return self.cps.rank(self.bwt, c, row-1) + self.count(c)
        nsteps = 0
        while row not in self.ssa:
            row = stepLeft(row)
            nsteps += 1
        return self.ssa[row] + nsteps
    
    def hasSubstring(self, p):
    
        l, r = self.range(p)
        return r > l
    
    def hasSuffix(self, p):

        l, r = self.range(p)
        off = self.resolve(l)
        return r > l and off + len(p) == self.slen-1
    
    def occurrences(self, p):

        l, r = self.range(p)
        return [ self.resolve(x) for x in range(l, r) ]
