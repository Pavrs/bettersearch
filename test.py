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
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        one()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
