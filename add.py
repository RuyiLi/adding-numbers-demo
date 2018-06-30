from sklearn.linear_model import LinearRegression
import numpy as np
# from matplotlib import pyplot as plt

# <editor-fold desc="Function definitions">


def sum_(a, b):
    # return float(model.predict(np.array([a, b]).reshape(1, -1)))
    return float(model.predict([[a, b]]))


def p_err(res, expect):
    return abs((expect - res) / expect)*100
# </editor-fold>

# <editor-fold desc="Sample Datasets">


X = [
        (9, 2),
        (3, 44),
        (3.4, 52.3),
    ]
Y = [
        11,
        47,
        55.7,
    ]

# </editor-fold>

# <editor-fold desc="Generating Linear Regression">
model = LinearRegression()
model.fit(X, Y)

print('y = {0.coef_[0]}x1 + {0.coef_[1]}x2 + {0.intercept_}\n\n'.format(model))
# </editor-fold>

# <editor-fold desc="Input">
low = int(input('Lower Bound  (Leave empty for -5000): ') or -5000)
high = int(input('Higher Bound (Leave empty for  5000): ') or 5000)
numcases = int(input('Number of test cases (Leave empty for 10): ') or 10)
# </editor-fold>

# <editor-fold desc="Generating Test Cases">
print('\n\n\n')
tests = np.random.uniform(low=low, high=high, size=(numcases, 2))
# np.round([n*100 for n in np.random.ranf((10, 2))], 2)
print('Tests:', '\n'.join(list(map(lambda e: str(tuple(e)), tests))))
# </editor-fold>

# <editor-fold desc="Testing">
__import__('time').sleep(1)

print('\n=========================================')

for x, y in tests:
    s = sum_(x, y)
    print('\n%f %c %f = %f'
          '\nActual sum: %f.'
          '\nPercentage Error: %f%%' %
          (x, '+' if y >= 0 else '-', abs(y), s, x + y, p_err(s, x + y)))

print('\n=========================================')

# </editor-fold>

"""
plt.scatter(np.array(X)[:,0], Y, color='b')
for i, (x, y) in enumerate(X):
    plt.annotate('(%d, %d)'%(x,y), (x, Y[i]))
plt.plot(X, model.predict(X), color='r')
plt.show()
"""