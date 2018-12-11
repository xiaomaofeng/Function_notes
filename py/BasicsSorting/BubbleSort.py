import time

def BubbleSort(alist):
    for i in xrange(len(alist)):
        print(alist)
        for j in xrange(1,len(alist)-i):
            if alist[j-1]>alist[j]:
                alist[j-1],alist[j]=alist[j],alist[j-1]

        return alist

unsorted_list=[6,5,3,1,8,7,2,4]
print(BubbleSort(unsorted_list))
time.sleep(10000)
