import requests

def media(stat):
  
  avg=sum(stat)/len(stat)
  
  return avg

sites = ['http://www.google.com', 'http://www.youtube.com', 'http://www.polimi,it',
         'http://www.wikipedia.org', 'http://www.amazon.com','http://www.twitter.com']

avg=[]

for url in sites:
  print('Test: ', url)
  times =[]
  for _ in range(10):
    
    r = requests.get(url)
    times.append(r.elpsed.microseconds/1000)
    
medium_time = media(times)
print('Avg: ' , medium_time)
avg.append(medium_time)

print(sites[avg.index(min(avg))], min(avg))
                    
              
