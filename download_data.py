from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pylab as p

start = dt(2010, 1, 1)
end = dt(2015, 7, 24)

#Download Public Bank 5 years stocks price 
data = DR("1295.KL", 'yahoo', start, end)
PB = data['Close'].values
num = len(PB)

# 5-day moving average of Public Bank stock price

mean2 = p.zeros_like(PB)
for i in range(num+1):
 
    if i >=5:
        mean = PB[i-5:i]
        mean2[i-5] = sum(mean)/5
        
#plot the graph
t = p.linspace (0,num-4,num-4);
p.title('5-day moving average')
p.xlabel('Day', fontsize=16)
p.ylabel('Average Stock Price, $RM$ ', fontsize=16)
p.plot(t,mean2[0:-4]); p.show();  # do not need the last 4 value 


#calculate the correlation of Public Bank with FTSEKLCI
Alldata=['^KLSE','1295.KL']
cor = DR(Alldata, 'yahoo', start, end)['Close']
cor1 = cor.corr()
print('The correlation is : ')
print(cor1)

