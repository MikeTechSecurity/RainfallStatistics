# Rainfall Statistics
# https://github.com/MikeTechSecurity/

def main():
    # Declare an array to hold the rainfall amounts for 12 months
    rainfall = [0.0] * 12
    # Declare an array to hold month names
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    # Get rainfall data from the user
    for i in range(12):
        rainfall[i] = float(input(f"Enter the rainfall for {months[i]}: "))

    # Calculate and display the statistics
    print(f"Total Rainfall for the year: {sum(rainfall)}")
    print(f"Average monthly rainfall: {average(rainfall)}")
    maxIndex = findMaxIndex(rainfall)
    minIndex = findMinIndex(rainfall)
    print(f"Month with the highest rainfall: {months[maxIndex]} with {rainfall[maxIndex]} units.")
    print(f"Month with the lowest rainfall: {months[minIndex]} with {rainfall[minIndex]} units.")

def average(array):
    return sum(array) / 12

def findMaxIndex(array):
    maxIndex = 0
    for i in range(1, 12):
        if array[i] > array[maxIndex]:
            maxIndex = i
    return maxIndex

def findMinIndex(array):
    minIndex = 0
    for i in range(1, 12):
        if array[i] < array[minIndex]:
            minIndex = i
    return minIndex

if __name__ == "__main__":
    main()
