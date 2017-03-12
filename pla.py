from random import randint
import matplotlib.pyplot as plt


class RegressionClassifier:
    dataset = []
    minx = 0
    maxx = 0
    b0=0;
    b1=0;

    def __init__(self,minx,maxx,dataset):
        self.minx=minx
        self.maxx=maxx
        self.dataset=dataset

    def makeRegressionCoefficients(self):

        xdiff=[]
        ydiff=[]
        xdiffsq=[]
        ydiffsq=[]
        product=[]
        total=0
        for i in range(0,len(self.dataset)):
            total=total+self.dataset[i][0]

        xavg=total/len(self.dataset)
        total=0

        for i in range(0,len(self.dataset)):
            total=total+self.dataset[i][1]

        yavg=total/len(self.dataset)

        for i in range(0,len(self.dataset)):
            xdiff.append(self.dataset[i][0]-xavg)
            ydiff.append(self.dataset[i][1]-yavg)

        for i in range(0,len(self.dataset)):
            xdiffsq.append(xdiff[i]*xdiff[i])
            ydiffsq.append(ydiff[i]*ydiff[i])
            product.append(xdiff[i]*ydiff[i])

        self.b1=sum(product)/sum(xdiffsq)
        self.b0=yavg-self.b1*xavg


    def plot(self):
        xs = []
        ys = []

        for i in range(0, len(self.dataset)):
                xs.append(self.dataset[i][0])
                ys.append(self.dataset[i][1])

        plt.scatter(xs, ys, color='red')

        length = self.maxx

        xcoord = [length]
        ycoord = [self.b0+length*self.b1]

        length = -self.minx
        xcoord.append(-1 * length)
        ycoord.append(self.b0+length*self.b1*-1)
        plt.plot(xcoord, ycoord, color='black')

class PerceptronLearner:
    dataset=[]
    vals=[]
    w=[]
    threshold=0
    step=0
    updates=0
    minx=0
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
                if(self.matches(self.dataset[i],self.vals[i])==False):
                    error=1
                    self.updates = self.updates + 1
                    self.rearrange(self.step,i)

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
        length = self.maxx

        xcoord = [length]
        ycoord = [-(length * self.w[0] +self.threshold) / self.w[1]]

        length=-self.minx
        xcoord.append(-1 * length)
        ycoord.append(-(self.threshold - length * self.w[0]) / self.w[1])

        plt.plot(xcoord, ycoord, color='orange')

        # plt.show()

        length = self.maxx

        xcoord = [length]
        ycoord = [10-(length * self.w[0]  + self.threshold) / self.w[1]]

        length = -self.minx
        xcoord.append(-1 * length)
        ycoord.append(-10-(self.threshold - length * self.w[0]) / self.w[1])

        plt.plot(xcoord, ycoord, color='purple')

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

    vals = [1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

    w = []
    x1=randint(-10,10)
    x2=randint(-10,10)

    w.append(x1)
    w.append(x2)

    threshold=randint(-5,5)
    step = 6


    regressor = RegressionClassifier(minx,maxx,dataset)
    regressor.makeRegressionCoefficients()
    regressor.plot()

    pla=PerceptronLearner(dataset,vals,w,threshold,step,minx,maxx)
    pla.train()
    pla.plot()
    print "Total updates :",pla.updates


if __name__ == "__main__":
    main()