from HyperEvalSR import sr

import scipy.io as scio

HSI = scio.loadmat('./test/HSI.mat')['HSI']
MSI = scio.loadmat('./test/MSI.mat')['MSI']

con = sr.CNMF(MSI, HSI) 

print("finish")