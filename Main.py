from Function import MyFunction
from SimulatedAnnealing import SimulatedAnnealing
from Probability import MyProbability
import matplotlib.pyplot as plt


myfun = MyFunction(-10,10)

"""
range nilai koefisien(a) alpha : 0.8<=a<=0.99 / [0.8,0.99]
parameter = Temperature,Minimum Temperature,koefisien,length of itenary each temperatur,Function,Probability
"""

#sA = SimulatedAnnealing(1000,1,0.9,50,myfun,MyProbability()) #tidak complete
#sA = SimulatedAnnealing(1.0,0.001,0.91,100,myfun,MyProbability()) #hampir complete
#sA = SimulatedAnnealing(1.0,0.001,0.99,2,myfun,MyProbability()) #sementara ini yang complete
#sA = SimulatedAnnealing(1.0,0.0001,0.8,50,myfun,MyProbability()) #hampir complete
sA = SimulatedAnnealing(1.0,0.0001,0.99,100,myfun,MyProbability()) #mendekati complete


solution,result = sA.getSolution()
print("Best Solution")
print(solution)
print("length of iteration",len(result))

"""grafik all solution"""
plt.plot(range(len(result)),result)
plt.show()