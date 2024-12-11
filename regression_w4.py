from os.path import dirname, abspath, join

# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
print(THIS_DIR)


# 2
def predictedY(beta_nought_hat, beta_one_hat, X):
    res = []
    n = len(X)
    for i in range(n):
        res.append(round(beta_nought_hat, 2) + round(beta_one_hat * X[i], 2))
    return res 


# 1
def coeff_estimator(X, Y):
    n = len(X)
    Xbar = sum(X) / len(X)
    Ybar = sum(Y) / len(Y)
    XminusXbar = [(i - Xbar) for i in X]
    YminusYbar = [(j - Ybar) for j in Y]
    XY = [XminusXbar[i] * YminusYbar[i] for i in range(len(YminusYbar))]
    num = sum(XY)
    denom = sum([i**2 for i in XminusXbar])
    beta_one_hat = num / denom
    beta_nought_hat = Ybar - beta_one_hat * Xbar
    return beta_nought_hat, beta_one_hat


# 3
def tss(Y, Ybar):
    Ybar = sum(Y) / len(Y)
    res = 0
    for i in Y:
        res += (i - Ybar)**2
    return res 


# 4
def ssreg(Yhat, Ybar):
    res = 0
    for i in Yhat:
        res += (i - Ybar)**2
    return res 


# 5
def ssres(Yhat, Y):
    res = 0
    for i in range(len(Yhat)):
        res += (Yhat[i] - Y[i])**2
    return res 


def mesreg(ssreg, n):
    return ssreg / (n-2)
    

def msres(ssres, n, p):
    return ssres / (n-p)

def fvalue(msreg, mesres):
    return msreg / msres


def coeffOfDetermination(ssres_, sst_):
    return  1 - (ssres_ / sst_)


if __name__ == "__main__":
    data = {'X1' : [7, 1, 11, 11, 7, 11, 3, 1, 2, 21, 1, 11, 10],
    'X2' : [26, 29, 56, 31, 52, 55, 71, 31, 54, 47, 40, 66, 68],
    'X3' : [6, 15, 8, 8, 6, 9, 17, 22, 18, 4, 23, 9, 8],
    'X4' : [60, 52, 20, 47, 33, 22, 6, 44, 22, 26, 39, 12, 12],
    'Y' : [78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7, 72.5, 93.1, 115.9, 83.8, 113.3, 109.4]}
    print(len(data))

    coeff_estm = {'b_0_hat' : [], 'b_1_hat' : []}

    for i in range(len(data)-1):
        beta_nought_hat, beta_one_hat = coeff_estimator(data[f'X{i+1}'], data['Y'])
        beta_nought_hat, beta_one_hat = round(beta_nought_hat, 2), round(beta_one_hat, 2)
        print(f'beta_nought_hat: {beta_nought_hat}, beta_one_hat: {beta_one_hat}')
        coeff_estm['b_0_hat'].append(beta_nought_hat)
        coeff_estm['b_1_hat'].append(beta_one_hat)

    print()
    print(f"b_0_hat: {coeff_estm['b_0_hat']}")
    print(f"b_1_hat: {coeff_estm['b_1_hat']}", '\n' )

    Yhat = predictedY(coeff_estm['b_0_hat'][3], coeff_estm['b_1_hat'][3], data['X4'])
    Yhat = [round(y, 2) for y in Yhat]
    print(f"Yhat: {Yhat}")
    Ybar = round(sum(data['Y']) / len(data['Y']), 2)

    tss_   = tss(data['Y'], Ybar)
    ssreg_ = ssreg(Yhat, Ybar)
    ssres_ = ssres(Yhat, data['Y'])
    msreg_ = mesreg(ssreg_, len(data['Y']))
    msres_ = msres(ssreg_, len(data['Y']), 3)
    fval =   msreg_ / msres_
    rsquare = coeffOfDetermination(ssres_, tss_)

    print(f"\ntss_  : {tss_}")
    print(f"ssreg_: {ssreg_}")
    print(f"ssres_: {ssres_}\n")

    print(f"msreg_: {msreg_}")
    print(f"msres_: {msres_}")
    print(f"fval  : {fval}")
    print(f"rsquare  : {rsquare}")

    

    

