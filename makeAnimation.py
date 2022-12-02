import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as mpatches
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
plt.rcParams['image.cmap'] = 'tab10'
def initialPlot(numClasses):
    """
    Initialises the plot
    Parameters:
    ----------
    numClasses: Number of classes in the dataset

    """
    cmap = plt.get_cmap()
    patches = [mpatches.Patch(color=cmap.colors[i], label=str(i)) for i in range(10)]
    fig, ax = plt.subplots()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    # patches = [mpatches.Patch(color=colors[i], label='Class {}'.format(i)) for i in range(numClasses)]
    return fig, ax, patches

def scatterPlot(Y,labels):
    """
    Creates a scatter plot of the projected points in the lower dimensional space
    Parameters:
    ----------
    Y: <number_of_iterations>*<number_ofpoints> ka array of projected points in the lower dimensional space
    labels: Label for each point in the lower dimensional space Y
    """
    uniqueLabels = np.unique(labels).shape[0]
    fig, ax, patches = initialPlot(uniqueLabels)
    ax.scatter(Y[:,0],Y[:,1],c=labels)
    plt.show()

def createAnimation(Y,labels,figureName,savePath):
    """
    Creates an animation from a list of images.
    Parameters:
    ----------
    Y: <number_of_iterations>*<number_ofpoints> ka array of projected points in the lower dimensional space
    labels: Label for each point in the lower dimensional space Y
    figureName: Name of the figure
    savePath: Path to save the animation

    """
    fig,ax ,patches = initialPlot(uniqueLabels)

    uniqueLabels = np.unique(labels).shape[0]
    def init():
        return scatterPlot
    def animationLoop(iteration):
        """
        The main animation loop for the generated plots
        """
        ax.clear()
        plt.legend(handles=patches , loc = 'upper right')
        ax.scatter(Y[iteration][:,0],Y[iteration][:,1],c=labels)
        ax.set_title('Iteration {}'.format(iteration))
        
        return ax,scatterPlot

    animation = FuncAnimation(
        fig, animationLoop,init_func=init, frames=range(Y.shape[0]), interval=50)

    animation.save(savePath+figureName+'.mp4', writer='ffmpeg', fps=30)    
   

