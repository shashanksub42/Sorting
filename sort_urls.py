urls = []
with open('sample_urls', 'r') as f:
    line = f.readline()
    #line, nl = line.split('\n')
    while line:
        urls.append(line)
        line = f.readline()
        #line, nl = line.split('\n')
               
def MergeSort(A, b):
    n = len(A)
    if n < 2:
        return
    mid = int(n/2)
    left = A[0:mid]
    right = A[mid:n]
    MergeSort(left, b)
    MergeSort(right, b)
    Merge(left, right, A, b)

def Merge(left, right, A, b):
    nL = len(left)
    nR = len(right)
    i, j, k = 0, 0, 0
    while i < nL and j < nR:
        if ord(left[i][b]) <= ord(right[j][b]):
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1
    while i < nL:
        A[k] = left[i]
        i += 1
        k += 1
    while j < nR:
        A[k] = right[j]
        j += 1
        k += 1

def sort_urls(urls):
    b = 13
    while b > 10:
        MergeSort(urls, b)
        b -= 1
    return urls



def print_list(stuffs):
    for stuff in stuffs:
        print(stuff)
print_list(sort_urls(urls))

