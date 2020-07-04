import urllib.request
import sys
from datetime import date
default_date=date(int("2019"),int("01"),int("01"))          #Python3 can't take 0 as the first char here due to octal interpretation
default_equivalence=1546300800                          
print("Welcome! Keep Starting-Ending dates and Stock Tickers handy as we proceed :) \n")
for i in (0,2):
    if i==0:
        input_taken='Starting'
    else:
        input_taken='Ending'
    
    rawInput=input("Enter the {} date in the YYYY-MM-DD format with no spaces between the hiphens: ".format(input_taken))
    try: 
        YYYY,MM,DD=map(int,rawInput.split('-'))
        if i==False:
            starting_date=date(YYYY,MM,DD)
            delta=starting_date-default_date
            starting_equivalence=default_equivalence+(86400*delta.days)     #This can be changed by yahoo to avoid scrapers
        else:                                                               #Just let me know if that happens we can compute it again ;)
            ending_date=date(YYYY, MM, DD)
            delta=ending_date-default_date
            ending_equivalence=default_equivalence+(86400*delta.days+86400)
    except:
        print("The format of the entered date was incorrect, the program terminates here. \n")
        sys.exit()

if starting_equivalence>ending_equivalence:  #You actually deserve to be confused by a HTTPS bad request error here. But I'm a good guy :)
    print("Starting Date cannot be after ending date \n")
    sys.exit()

ticker=input("Nice, now type in the ticker for the stock (All caps): ")

url="""https://query1.finance.yahoo.com/v7/finance/download/"""+ticker+"""?period1="""+str(starting_equivalence)+"""&period2="""+str(ending_equivalence)+"""&interval=1d&events=history"""

file_name=input("What should we name the the downloaded csv file? (File name should have a .csv extension & Enter exact path if this isn't the desired download directory): ")

try: 
    urllib.request.urlretrieve(url,file_name) 
    print("Downloaded Successfully! \n")
except:
    print("Something Went wrong, I'd request you to try again and recheck your ticker.") #Invalid ticker, file name without csv and unstable internet connections are the possible issues here.
