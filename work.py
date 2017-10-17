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
        #displays each line in the file
            x = str(line)
            
def main():
    requests_per_month()
    
main()
