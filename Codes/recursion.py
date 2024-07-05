array = [1,2,3,4,5,6,7,8,9,10]
sum = 0

def getSum(index):
    global array, sum
    if index >= len(array):
        return

    sum += array[index]
    getSum(index+1)

getSum(0)
print(f'Sum of array is : {sum}')