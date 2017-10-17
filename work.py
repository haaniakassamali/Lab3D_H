import urllib.request

def requests_per_month():
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
            x = str(line)
            #creating a helpful list with date, get, number to work with
            
            a = x.split('[')
            b = a[1]
            c = b.split(']')
            d = [a[0], c[0], c[1]]
            aa = d[2]
            bb = aa.split('"')
            aaa = bb[2]
            ccc = aaa.split()
            totes = [a[0], c[0], bb[1], ccc[0],ccc[1]]
            
            
            
            count += 1
  
def main():
    requests_per_month()
    
main()
