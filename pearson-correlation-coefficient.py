
import numpy as np

# https://en.wikipedia.org/wiki/Pearson_correlation_coefficient
def pearson_correlation_coefficient(x, y):

    # just to assure data consistency
    np_x = np.array(x)
    np_y = np.array(y)

    n = len(np_x)  # sample size

    x_mean = np.mean(np_x)
    y_mean = np.mean(np_y)

    d_xy = (np.sum(np_x * np_y) - n * x_mean * y_mean)
    d_xx = np.sqrt(np.sum(np_x * np_x) - n * (x_mean * x_mean))
    d_yy = np.sqrt(np.sum(np_y * np_y) - n * (y_mean * y_mean))

    r_xy = d_xy / (d_xx * d_yy)

    return r_xy


if __name__ == "__main__":
    weight = [3.63, 3.02, 3.82, 3.42, 3.59, 2.87, 3.03, 3.46, 3.36, 3.3]
    length = [53.1, 49.7, 48.4, 54.2, 54.9, 43.7, 47.2, 45.2, 54.4, 50.4]

    r_wl = pearson_correlation_coefficient(weight, length)
    print(f'{r_wl:.3f}')

    corr = np.corrcoef(weight, length)
    print(f'{corr}')
