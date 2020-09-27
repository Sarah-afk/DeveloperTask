class Fibonacci:

    def __init__(self, cache):
        #the cache here saves the last calculated fibonacci of n for 500 seconds to be used instead of recalculating
        @cache.memoize(timeout=500)
        def fibo_calc(i):
            if i == 1:
                return 2
            if i <= 0:
                return 1
            return fibo_calc(i-1)+fibo_calc(i-2)

        self.fibo_calc = fibo_calc

    def array_fibo(self, n):
        #this method returns an array of fibonacci numbers between two and n
        arr = []
        i = 1
        while True:
            fib_val = self.fibo_calc(i)
            i += 1
            if fib_val > n:
                break
            arr.append(fib_val)
        return arr

    def fibo_sum(self, arr_fib, target, partial=[]):
        #this is a recursive method to find all possible combinations of arr_fib that sum up to target
        if target == 0:
            return [partial]
        if target < 0:
            return []
        output = []
        for i, n in enumerate(arr_fib):
            remaining = arr_fib[i:]
            output += self.fibo_sum(remaining, target - n, partial + [n])
        return output

    def calculate(self, n):
        arr_fib = self.array_fibo(n)
        return self.fibo_sum(arr_fib, n)
