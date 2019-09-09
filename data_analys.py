import csv

with open('espe_data4.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)


class Spike:
    
    date = ''
    start_index = 0
    end_index = 0
    readings = []

    def median_reading(self):
        median = 0
        i = 0
        self.readings = []
        if self.end_index != 0:
            for _, reading in your_list[self.start_index : self.end_index]:
                self.readings.append(float(reading))
                i += 1
            self.readings.sort
            
            median = self.readings[int(i/2)]
        
        else:
            #last spike is runnig median
            for _, reading in your_list[self.start_index:]:
                self.readings.append(float(reading))
                i += 1
            
            self.readings.sort
            median = self.readings[int(i/2)]
        
        return median
    
   

i = 0
last_reading = 0

spikes = [Spike]

for date, raw_reading in your_list:
    reading = float(raw_reading)
    if last_reading == 0 and reading > 0:
        spike = Spike()
        spike.start_index = i
        spike.date = date
        spikes.append(spike)
        

    if last_reading > 0 and reading == 0:
        spikes[-1].end_index = i
        

    last_reading = reading
    i += 1

#remove first item in list
spikes.remove(spikes[0])


i = 0
for spike in spikes:
    #print(spike.start_index, spike.end_index)
    if len(spikes) > i + 1:
        diff = spikes[i].median_reading() - spikes[i+1].median_reading()
        #print(diff)
        if 10 < diff < 17:
            print("Du tog 1 piller: ", spike.date,)
        if 22 < diff < 35:
            print("Du tog 2 piller: ", spike.date)
    
    i += 1
