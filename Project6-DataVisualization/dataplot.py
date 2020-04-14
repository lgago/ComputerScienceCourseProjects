import glob
import matplotlib.pyplot as plt
import numpy as np

VT = 100
WIDTH = 50

def smooth(data):
    res = data.copy()

    for n in range(3, len(data)-3):
        res[n] = (data[n-3] + 2 * data[n-2] + 3 * data[n-1] + 3 * data[n] + 3 * data[n+1] + 2 * data[n+2] + data[n+3]) // 15

    return res

def analyze(fileName):
    #Read in the data from the file (store into nparry)
    rawData = np.loadtxt(fileName)

    #Smooth the data (store into a new np.array)
    smoothData = smooth(rawData)

    #Search for pulses in the smooth data
    pulses = []
    i = 0
    while i < len(smoothData) - 2:
        if smoothData[i + 2] - smoothData[i] > VT: #Found a pulse
            pulses.append(i)

            #skip past the rise
            i += 1
            
            while i < len(smoothData) - 2 and smoothData[i+1] > smoothData[i]:
                i += 1
        i += 1
    if not pulses:
        return
    
    #Calculate the area of the pulses
    outputString = f'{fileName}:\n'

    for i in range(len(pulses)):
        startpos = pulses[i]
        realWidth = WIDTH 

        if i < len(pulses) - 1 and pulses[i] + realWidth > pulses[i + 1]:
            realWidth = pulses[i + 1] - startpos
        realWidth = min(realWidth, len(smoothData) - startpos)
        area = int(sum(rawData[startpos : startpos + realWidth]))
        outputString += f'Pulse {i+1}: {startpos + i} ({area})\n'

    #Somefile.dat
    with open(fileName[:-3] + 'out', 'w') as outfile:
        print(outputString, file=outfile, end='')

    #Plot the data
    _, axes = plt.subplots(nrows=2)
    axes[0].plot(rawData, linewidth=.2)
    axes[0].set(title=fileName, ylabel='raw') 
    axes[1].plot(smoothData, linewidth=.3)
    axes[1].set(ylabel='smooth')
    plt.savefig(fileName[:-3] + "pdf")

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

if __name__ == "__main__":
    main()