import pylab as p

#Setup parameters
mu = 0.1 ; sigma = 0.26 ;S0 = 39 ; time=3
n_path = 1000 ; n= n_partitions = 1000;


# Theoritical expectation and variance
Expected = S0 * p.exp(mu*time)
Variance = (S0**2)*(p.exp(2*mu*time))*(p.exp(sigma*sigma*time)-1)

msg = 'The theoritical expected value of S(3) is %.13f' %Expected
print(msg)
msg = 'The theoritical vaiance of S(3) is %.13f' %Variance
print(msg)


#create brownian motion 
t = p.linspace (0,3,n+1);
dB = p.randn(n_path, n+1) / p.sqrt(n/time); dB[:,0]=0;
B= dB.cumsum(axis=1);

#calculate stock price 
nu = mu - sigma *sigma / 2.0
S = p.zeros_like(B); S[:,0]=S0
S[:,1:] = S0*p.exp (nu*t[1:] + sigma*B[:,1:])

S2 = S[0:5]
p.title('Brownian Motion')
p.xlabel('Time, $t$', fontsize=16)
p.ylabel('X(t)', fontsize=16)
p.plot(t,S2.transpose()); p.show();

#calculate expectation value of S(3)
S3=S[:,-1]
E= S3.sum() / n_path
msg = 'The expected value of S(3) is %.13f' %E
print(msg)

#calculate variance of S(3)
V1 = (S3 - E)**2
V2 = V1.sum() / (n_path - 1) 
msg = 'The variance of S(3) is %.13f' %V2
print(msg)

# Calculate P[S(3)> 39] and E[S(3) | S(3) > 39]
count =0 
total = 0

for i in range(n_path):
    if S3[i] > S0:
        count = count + 1
        total = total + S3[i]

count2 = count / n_path
CE = total / count

msg = 'The probability that S(3) is more than 39 is %.13f' %count2
msg2 = ' and the E[S(3) | S(3) > 39] is %.13f' %CE
print (msg, msg2)




