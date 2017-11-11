from math import floor
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math
import numpy as np

target = "test.hter"
prediction = "test_prediction.txt"

def deltaAvg(reference, prediction):
    data = [(pred, ref) for pred, ref in zip(prediction, reference)]
    data_sorted = sorted(data, key=lambda x: x[0], reverse=True)
    dataLen = len(data_sorted)
    
    avg = sum([x[1] for x in data_sorted])/dataLen
    deltaLen = floor(dataLen//2+1)
    
    deltaLen = int(deltaLen)
    deltaAvg = [0] * (deltaLen)
        
    for k in range(2, deltaLen):
        for i in range(1, k):
            deltaAvg[k] += sum([x[1] for x in data_sorted[:(dataLen*i/k)]])
        deltaAvg[k] = deltaAvg[k]/(k-1) - avg
    return sum(deltaAvg)*2.5/pow((deltaLen-2),2)


def printScores(target, prediction): 
    targetdata =[]
    predata = [] 
    fpRead = open(target,'r')
    targetdata = fpRead.readlines()
    fpRead.close()  
    targetdata = np.array(targetdata).astype(np.float)

    fpRead = open(prediction,'r')
    predata = fpRead.readlines()
    fpRead.close() 
    predata = np.array(predata).astype(np.float)

    print('Pearson\'s r:', pearsonr(targetdata, predata))
    print('RMSE:', math.sqrt(mean_squared_error(targetdata, predata)))
    print('MAE:', mean_absolute_error(targetdata, predata))
    print('Spearman\'s rank:', spearmanr(targetdata, predata)[0])
    print('DeltaAvg: ', deltaAvg(targetdata, predata))

if __name__ == "__main__":

 printScores(target,prediction)
