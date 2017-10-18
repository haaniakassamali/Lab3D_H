import urllib.request
from datetime import datetime

def requests_per_month_and_month_files():
    count = 0
    
    Oct = 0
    Nov = 0
    Dec = 0
    Jan = 0
    Feb = 0
    Mar = 0
    Apr = 0
    May = 0
    Jun = 0
    Jul = 0
    Aug = 0
    Sep = 0
    
    
    data = urllib.request.urlopen('https://s3.amazonaws.com/tcmg412-fall2016/http_access_log')
    
    for line in data:
        while count < 5:
            #Turning each line into strings
            x = str(line)
            #ignore the weird lines #couldn't figure out how to work with them
            if len(x) < 50: pass
            
            else:    
                #creating a helpful list that seperates each line into sections
                a = x.split('[')
                b = a[1]
                c = b.split(']')
                d = [a[0], c[0], c[1]]
                aa = d[2]
                bb = aa.split('"')
                aaa = bb[2]
                ccc = aaa.split()
                totes = [a[0], c[0], bb[1], ccc[0],ccc[1]]
                
                #counting requests for each month 
            
                if 'Oct' in totes[1]:
                    Oct += 1
                if 'Nov' in totes[1]:
                    Nov += 1 
                if 'Dec' in totes[1]:
                    Dec += 1
                if 'Jan' in totes[1]:
                    Jan += 1
                if 'Feb' in totes[1]:
                    Feb += 1
                if 'Mar' in totes[1]:
                    Mar += 1
                if 'Apr' in totes[1]:
                    Apr += 1
                if 'May'in totes[1]:
                    May += 1
                if 'Jun' in totes[1]:
                    Jun += 1
                if 'Jul' in totes[1]:
                    Jul += 1
                    
                print('Total requests made for October:  ...', Oct)
                print('Total requests made for November:   ', Nov)
                print('Total requests made for December: ...', Dec)
                print('Total requests made for January:     ', Jan)
                print('Total requests made for February: ...', Feb)
                print('Total requests made for March:       ', Mar)
                print('Total requests made for April:    ...', Apr)
                print('Total requests made for May:         ', May)
                print('Total requests made for June:     ...', Jun)
                print('Total requests made for July:        ', Jul)
                
                count += 1

def total_requests():
    #still in progress 
    total = 0
    print('\n The total requests made during this time period: ')
    
def main():
    print('\n-----------------------------------------\n')
    requests_per_month_and_month_files()
    
main()
