start= int(input('enter start number: '))
end= int(input('enter end number: '))
for number in range (start,end+1):
    for num in range (1,7):
        result = number * num
        print (f'{number} X {num} = {result} ')
    print ("-------------------")
