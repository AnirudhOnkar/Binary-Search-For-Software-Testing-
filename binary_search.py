def binary_search():
    a=[]
    n=int(input("Enter the no. of ele"))
    if n>0:
        print(f"enter {n} ele in ascending order")
        a=[int(input()) for _ in range(n)]
        key= int(input("Enter the ele to be searched"))
        low=0
        high = n-1
        while low<high:
            mid=(low+high)//2
            if a[mid]==key:
                print(f"ele found at {mid+1}")
                return
            elif a[mid]<key:
                low=mid+1
            else:
                high=mid-1
        print("Key not found")
    else:
        print("Wrong input")
if __name__=="__main__":
    binary_search()
