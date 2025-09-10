import pickle
flight={'flight_number':'1700','airline':'Indigo','capacity':225,'price':4500,'source':'Bangalore','destination':'Hyderabad'}
file_name='flight.dat'

print('Before',flight)
with open(file_name,'wb') as writer:
    pickle.dump(flight,writer)
    print('Saved the flight to file')

with open(file_name,'rb') as reader:
    flight_from_file=pickle.load(reader)
    print('Flight after read from file:',flight_from_file)
