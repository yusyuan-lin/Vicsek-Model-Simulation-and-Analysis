import matplotlib.pyplot as plt
import numpy as np


def main():
    """ Finite Volume simulation """

    # Simulation parameters

    v0           = 3.5      # velocity
    eta          = 1.5      # random fluctuation in angle (in radians)

    L            = 10       # size of box
    N            = 500       # number of birds

    R            = 0.5      # interaction radius

    dt           = 0.1      # time step
    Nt           = 200      # number of time steps


    plotRealTime = True

    # Initialize
    np.random.seed(17)      # set the random number generator seed

    # bird positions
    x = np.random.rand(N,1)*L
    y = np.random.rand(N,1)*L

    # bird velocities
    theta = 2 * np.pi * np.random.rand(N,1)
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)

    # Prep figure
    fig = plt.figure(figsize=(8,8), dpi=80)
    ax = plt.gca()

    # Create file for saving data
    data_file = open("0612.txt", "w")

    # Simulation Main Loop
    for i in range(Nt):

        # move
        x += vx*dt
        y += vy*dt

        # apply periodic BCs
        x = x % L
        y = y % L

        # find mean angle of neighbors within R
        mean_theta = theta
        for b in range(N):
            neighbors = (x-x[b])**2+(y-y[b])**2 < R**2
            sx = np.sum(np.cos(theta[neighbors]))
            sy = np.sum(np.sin(theta[neighbors]))
            mean_theta[b] = np.arctan2(sy, sx)

        # add random perturbations
        theta = mean_theta + eta*(np.random.rand(N,1)-0.5)

        # update velocities
        vx = v0 * np.cos(theta)
        vy = v0 * np.sin(theta)

        # Save data to file
        data = np.concatenate((x,theta),axis=1)
        np.savetxt(data_file, data)
        print('finish save'+str(i))

        # plot in real time
        if plotRealTime or (i == Nt-1):
            plt.cla()
            plt.quiver(x,y,vx,vy)
            ax.set(xlim=(0, L), ylim=(0, L))
            ax.set_aspect('equal')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
            plt.pause(0.001)


    data_file.close()
    plt.show()

if __name__ == "__main__":
    main()
