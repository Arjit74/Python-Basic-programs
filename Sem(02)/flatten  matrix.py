# flatten matrix
# nested lsit 
lst = eval(input())
lst = [2,[2,3,4,5],[1,3],[],[1,[0]]]
lst = str([i for i in lst if i]).replace('[','')
out = lst.replace(']','')
print(list(eval(out)))