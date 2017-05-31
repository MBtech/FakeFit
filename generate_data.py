import numpy
import csv
def get_steps():
    return int(numpy.random.normal(7500,2500))

def get_hb_resting():
    return numpy.random.normal(80,10)

def get_hb_exercise():
    return numpy.random.normal(130,30)

def get_weight():
    return numpy.random.normal(160,30)

def get_height():
    return numpy.random.normal(70,5)

def get_age():
    u = numpy.random.uniform(0,1) 
    b = numpy.random.beta(1,3)
    return min(u,b)*100

def get_sleep():
    return numpy.random.normal(8.5,1)


data = [get_age(), get_height(), get_weight(), get_steps(), get_sleep(), get_hb_resting(), get_hb_exercise()]
myfile = open('data.csv', 'wb')
wr = csv.writer(myfile)
wr.writerow(['Age', 'Height', 'Weight', 'Steps', 'Sleep', 'Heart rate Resting', 'Heart rate Exercise'])
myfile.close()

with open('data.csv', 'a') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(data)
