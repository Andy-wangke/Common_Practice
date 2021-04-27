#Fibonacci
#Write a method calculating the specified element of a Fibonacci sequence.
#sample: f(0)=0 f(1)=1 f(2)=1 f(3)=2 f(4)=3 f5=5 … f(n)=?


def Fibonacci(n):
    if n>=0:
        # if n==0: return 0
        # elif n==1: return 1
        if n <= 1: return n
        else: return Fibonacci(n-1)+Fibonacci(n-2)
    else:
        return 'Error,Fibonacci >=0'

if __name__=='__main__':

    print(Fibonacci(1))