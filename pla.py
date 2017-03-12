import matplotlib.pyplot as plt
from random import randint
import random


class PerceptronLearner:
    dataset=[]
    vals=[]
    w=[]
    threshold=0
    step=0
    updates=0
    minx=0;
    maxx=0
    def __init__(self, dataset,values,weights,threshold,step,minx,maxx):
        self.dataset=dataset
        self.vals=values
        self.w=weights
        self.threshold=threshold
        self.step=step
        self.minx=minx
        self.maxx=maxx

    def rearrange(self,step, i):
        self.threshold=round(self.threshold+step*self.vals[i],3)
        for j in range(0,len(self.w)):
            self.w[j]=round(self.w[j]+step*self.vals[i]*self.dataset[i][j],2)

    def matches(self,xvector,val):
        score=0;
        score+=self.threshold
        for i in range(0,len(xvector)):
            score+=xvector[i]*self.w[i]

        if ((score>0 and val>0) or (score<=0 and val<=0)):
            # print score , " true ", self.w
            return True

        # print score, " false "
        return False


    def train(self):
        while(True):
            error=0
            for i in range(0,len(self.dataset)):
                # print self.dataset[i]
                if(self.matches(self.dataset[i],self.vals[i])==False):
                    error=1
                    # self.plot()
                    self.updates = self.updates + 1
                    self.rearrange(self.step,i)

                    # print "new w",self.w," threshold :",self.threshold
            if(error == 0):
                break



    def plot(self):
        xs = []
        ys = []

        for i in range(0, len(self.dataset)):
            if (self.vals[i] > 0):
                xs.append(self.dataset[i][0])
                ys.append(self.dataset[i][1])

        plt.scatter(xs, ys, color='red')

        xs = []
        ys = []

        for i in range(0, len(self.dataset)):
            if (self.vals[i] < 0):
                xs.append(self.dataset[i][0])
                ys.append(self.dataset[i][1])

        plt.scatter(xs, ys, color='blue')
        length = self.maxx;

        xcoord = [length]
        ycoord = [-(length * self.w[0] +self.threshold) / self.w[1]]
        # print xcoord,ycoord
        length=-self.minx;
        xcoord.append(-1 * length)
        ycoord.append(-(self.threshold - length * self.w[0]) / self.w[1])
        # print xcoord,ycoord
        plt.plot(xcoord, ycoord, color='orange')
        plt.show()

def main():

    dataset=[]
    minx=4000
    maxx=0
    for i in range(0,10) :
        pair=[]
        weight=randint(200, 250)
        height=randint(200, 250)
        pair.append(weight)
        pair.append(height)
        if(weight<minx):
            minx=weight
        if(weight>maxx):
            maxx=weight
        dataset.append(pair)

    for i in range(0,10) :
        pair = []
        weight=randint(270, 350)
        height=randint(150,220)
        pair.append(weight)
        pair.append(height)
        if (weight < minx):
            minx = weight
        if (weight > maxx):
            maxx = weight
        dataset.append(pair)

    print dataset
    vals = [1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
    #
    # dataset=[[-2,1],[1,1],[3,-1],[-2,-1],[-1,-2],[2,-2]]
    # vals=[1,1,1,-1,-1,-1]

    w = []
    x1=randint(-10,10)
    x2=randint(-10,10)

    w.append(x1)
    w.append(x2)
    print w
    threshold=randint(-5,5)
    step = 6
    pla=PerceptronLearner(dataset,vals,w,threshold,step,minx,maxx)
    pla.train()
    pla.plot()
    print "Total updates :",pla.updates
    print pla.w,pla.threshold
if __name__ == "__main__":
    main()