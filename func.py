import matplotlib.pyplot as plt

G_CONST = 9.81

def simulate_move(x, y, v_0, step : float):
    positions = [(x_new, y_new) for x_new, y_new in move_generator(x,y,v_0, step)]
    x_pos, y_pos = zip(*positions)
    
    return x_pos, y_pos

def move_generator(x, y, v_0, step : float):
    t = 0
    y_new = y
    while y_new > 0:
        x = v_0*t
        y_new = y - 0.5* G_CONST * t**2
        t += step
        yield x, y_new

def plot(xs, ys):
    plt.plot(xs, ys)
    plt.xlabel("X coord")
    plt.ylabel("Y coord")
    plt.title("Vertical projection")
    plt.show()