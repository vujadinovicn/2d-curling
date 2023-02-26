import numpy as np


def rk4n(a, b, h, nfX0, dnfX):
    """
    Function for calculating velocity in every moment.
    :param a: Time when motion started.
    :param b: Time when motion ended.
    :param h: Moment in whole time.
    :param nfX0: Array with only the initial velocity value.
    :param dnfX: Derivative of velocity by time.
    :return: (tuple) Velocities in every moment.
    """
    x = np.arange(a, b, h)
    n = len(x)
    order = len(nfX0)
    fnX = np.empty([order, n])
    fnX[:, 0] = nfX0.T
    k1, k2, k3, k4 = np.empty((1, order)), np.empty((1, order)), np.empty((1, order)), np.empty((1, order))
    for it in range(1, n):
        # k1
        for itOrder in range(order - 1):
            k1[0, itOrder] = fnX[itOrder + 1, it - 1]

        args = [x[it - 1]]

        for i in range(len(fnX)):
            args.append(fnX[i, it - 1])

        k1[0, order - 1] = dnfX(*args)

        # k2
        for itOrder in range(order - 1):
            k2[0, itOrder] = fnX[itOrder + 1, it - 1] + h / 2 * k1[0, itOrder + 1]

        args = [x[it - 1] + h / 2]

        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1] + h / 2 * k1[j][0])

        k2[0, order - 1] = dnfX(*args)

        # k3
        for itOrder in range(order - 1):
            k3[0, itOrder] = fnX[itOrder + 1, it - 1] + h / 2 * k2[0, itOrder + 1]

        args = [x[it - 1] + h / 2]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1] + h / 2 * k2[j][0])
        k3[0, order - 1] = dnfX(*args)

        # k4
        for itOrder in range(order - 1):
            k4[0, itOrder] = fnX[itOrder + 1, it - 1] + h * k3[0, itOrder + 1]

        args = [x[it - 1] + h]
        for i in range(len(fnX)):
            for j in range(len(k1)):
                args.append(fnX[i, it - 1] + h * k3[j][0])

        k4[0, order - 1] = dnfX(*args)

        for itOrder in range(order):
            fnX[itOrder, it] = fnX[itOrder, it - 1] + h / 6 * (
                        k1[0, itOrder] + 2 * k2[0, itOrder] + 2 * k3[0, itOrder] + k4[0, itOrder])

    fX = fnX[0, :]
    return fX
