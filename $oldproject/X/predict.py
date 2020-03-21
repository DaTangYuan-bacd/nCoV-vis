
class 插值器:
    def __init__(self):
        self.n = 0
        self.x = []
        self.y = []

    def __call__(self, x):
        def P(iterable):
            r = 1
            for i in iterable:
                r *= i
            return r
        X = self.x
        Y = self.y
        n = self.n
        l = [        P([    ((x-X[j])/(X[i]-X[j]) if i != j else 1)    for j in range(n)])       for i in range(n)]
        return sum(Y[i]*l[i] for i in range(n))
##        self.__lagrange(self.x, self.y, self.n, x)
        
##    def __lagrange(self, x, y, num_points, x_test):
##        l = [1] * num_points
##        for i in range(num_points):
##            for j in range(num_points):
##                l[i] *= (l[i]*(x_test-x[j])/(x[i]-x[j])) if i != j else 1
##        return [y[i]*l[i] for i in range(num_points)]

    def 加入数据(self, 输入, 输出):
        assert len(输入) == len(输出)
        self.x.extend(输入)
        self.y.extend(输出)
        self.n += len(输入)
        
    def 预测():
        self.__call__()
