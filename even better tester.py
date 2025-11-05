# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        import random
        f=10000
        nlist = [random.randrange(1, 101) for x in range (f)]
        print(nlist)
        search= int(input('enter the number '))

        for x in range(len(nlist)):

            if search == nlist[x]:
                total = f*search
                print(total)

            else:
                print('nothin')
            break
        
                         
                 
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        #binary search
        nlist=[2,4,5,6,7,21,133,1341,13413, 222222, 222222222, 2222222222]
        found= True
        search= 1341

        first = 0
        last = len(nlist) -1

        while (found == False and last >= first):
            mid = (first+last)//2
            if (search == nlist[mid]):
                found = True
                break
            else:
                if (search > nlist[mid]):
                    last = mid + 1
                elif (search < nlist[mid]):
                    last = mid - 1
            if (found== True) :
                print(f'found data item')
            else:
                print('not found data item')     
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        two()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
