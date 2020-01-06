"""
实现链表结构的快排，空间复杂度为o(1)
"""
# python标准库没有实现链表
# 如果要用链表实现快排，以链表的尾巴作为partition的key，从头开始遍历，把大于key的数通过链表指针链接到尾部
# 然后按照key的位置截断，再递归

# 实现list的快排
def quick_sort(lista,l,r):
    if l<r:
        i = partition(lista, l, r)
        quick_sort(lista, l, i)
        quick_sort(lista, i+1, r)
    return  lista

def partition(lista, l, r):
    key=lista[l]
    i=l  # i作为存放比key小的数的index
    for j in range(i+1,r):
        if lista[j] < key:
            i+=1
            lista[i],lista[j] = lista[j],lista[i]
    lista[l],lista[i] = lista[i],lista[l]  # 把key插入到中间的位置
    return i  # i为切分点

if __name__ == '__main__':
    lista = [4,5,6,6,3,1,6,8,9,5,23,12,3,5,2,5]
    print(quick_sort(lista,0,len(lista)))