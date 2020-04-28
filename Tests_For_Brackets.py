import unittest
def gen_breckets(N, prefix='', A = []):
    if N == 0:
        A.append(prefix)
    else:
        gen_breckets(N-1, prefix + '(')
        gen_breckets(N-1, prefix + ')')
    return A

def BalancedParentheses(N):
    M = 2*N
    A = gen_breckets(M)
    B = []
    for i in range(len(A)):
        Ability = True
        Count1 = 0
        Count0 = 0
        for j in range(len(A[i])):
            if A[i][j] == '(':
                Count1 += 1
            else:
                Count0 += 1
            if Count0 > Count1:
                Ability = False
        if Ability and A[i][0] == '(' and A[i][-1] == ')' and Count1 == Count0:
            B.append(A[i])
    return ' '.join(B)

class MyTestCase(unittest.TestCase):    
    
    def test_1(self):
        N = 1
        A = '()'
        X = BalancedParentheses(N)
        self.assertEqual(A, X)  
        
    def test_2(self):
        M = 2
        B = '(()) ()()'
        B = B.split()
        Y = BalancedParentheses(M)
        Y = Y.split()
        for i in B:
            b = B.count(i)
            y = Y.count(i) 
            self.assertEqual(b, y)       

    def test_3(self):
        M = 3
        B = '((())) (()()) (())() ()(()) ()()()'
        B = B.split()
        Y = BalancedParentheses(M)
        Y = Y.split()
        for i in B:
            b = B.count(i)
            y = Y.count(i) 
            self.assertEqual(b, y)  

    def test_4(self):
        M = 4
        B = '(((()))) ((()())) ((())()) ((()))() (()(())) (()()()) (()())() (())(()) (())()() ()((())) ()(()()) ()(())() ()()(()) ()()()()'
        B = B.split()
        Y = BalancedParentheses(M)
        Y = Y.split()
        for i in B:
            b = B.count(i)
            y = Y.count(i) 
            self.assertEqual(b, y)  

if __name__ == '__main__':
    unittest.main()
