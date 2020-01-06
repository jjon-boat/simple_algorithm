"""
两个有序数组，长度分别为m、n，将他们合并为一个有序数组，要求时间复杂度为o(m+n)

"""
def merge(lista,listb)->list:
    i,j=0,0
    result=[]
    while i<len(lista) and j<len(listb):
        if lista[i] <= listb[j]:
            result.append(lista[i])
            i+=1
        else:
            result.append(listb[j])
            j += 1
    if i==len(lista):
        result+=listb[j:]
    else:
        result += lista[i:]

    return result

# 归并排序
def merge_sort(lista):
    if len(lista)==1:
        return lista
    else:
        split_point = len(lista)//2
        return merge(merge_sort(lista[:split_point]), merge_sort(lista[split_point:]))



if __name__ == '__main__':
    A = [1,3,5,7]
    B = [2,4,5,6,7,8,9]
    C = A+B

    print(merge(A,B))
    print(merge(B,A))

    print(merge_sort(C))

