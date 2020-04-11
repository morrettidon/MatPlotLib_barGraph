import matplotlib.pyplot as plt
import random

def ran():
    num = random.randint(0,1000)
    return num

def xPoints():
    x=[ran(), ran(), ran(), ran(), ran(), ran()]
    return x

def yPoints():
    y=[ran(), ran(), ran(), ran(), ran(), ran()]
    return y

def myGraph():
    plt.title('my COVID-19 graphs')
    plt.ylabel('billions of USD$')
    plt.xlabel('death count')
    plt.plot(xPoints(),yPoints(),'g-')
    plt.axis([-100,1000,-100,1000])
    plt.show()

def main():
    myGraph()


if '__name__' = '__main__':
    main()