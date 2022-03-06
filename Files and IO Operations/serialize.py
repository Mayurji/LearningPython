import pickle

#Object to File
data = 'serialize python obj.'
f = open('somefile', 'wb')
pickle.dump(data, f) #Unserialize pickle.load

#Object to string
pickle.dumps(data) #Unserialize pickle.loads