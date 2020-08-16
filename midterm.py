

crr=[]
def read():
    with open("test.txt") as f:
    # f.readline()
        for line in f:
            line=line.strip()
            data=line.split(" ")
            brr=split(data)
            print(brr)
            for index in range(len(brr)):
                if data[10] == brr[index]:
                    print(index)
                    





            # brr.append(line[:4])
            # print(data[2])
            # print(add0)
            # for x in range(len(data)):
            #     arr.append((data[x]))
            #
            # print(arr)



def split(arr):
    if len(arr)==1:
        return arr
    else:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
        return mergeSort(split(left),split(right))


def mergeSort(left,right):
    indexLeft=0
    indexRight=0
    arr=[]
    while(indexLeft<len(left) and indexRight<len(right)):
        if left[indexLeft]<right[indexRight]:
            arr.append(left[indexLeft])
            indexLeft+=1
        elif right[indexRight]<left[indexLeft]:
            arr.append(right[indexRight])
            indexRight+=1
    if indexLeft<len(left):
        arr.extend(left[indexLeft:])
    elif indexRight<len(right):
        arr.extend(right[indexRight:])
    return arr




def main():
     read()



if __name__ == "__main__":
    main()