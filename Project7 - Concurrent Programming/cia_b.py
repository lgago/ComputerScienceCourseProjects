from time import perf_counter
from math import sqrt
import requests
from concurrent.futures import ProcessPoolExecutor


#Wrap this in download func and pass in flag country code for proj 7
def download(countryCode):# Download a flag from the CIA
    prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
    fname = prefix + countryCode + "-lgflag.gif"
    flag = requests.get(fname).content      # Note: No headers={...}
    if flag:
        with open(countryCode + ".gif","wb") as f:
            f.write(flag)
        return len(flag)

def main():
    with open("flags.txt","r") as f:
        countryCodes = f.read().split('\n')

    numBytes = 0
    
    start = perf_counter()
    with ProcessPoolExecutor() as p:
        numBytes = sum(p.map(download,countryCodes))
    stop = perf_counter()

    #These numbers need to be output to a file. 
    file1 = open("cia_b.txt","w")#write mode 
    file1.write("Elapsed time: " + str(stop - start) + "\n" + str(numBytes) + " bytes downloaded") 
    file1.close() 

if __name__ == "__main__":
    main()