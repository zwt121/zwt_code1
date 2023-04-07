# 研究人员正在研究大量样本中的细胞分裂。对每个样本中的细胞进行计数是自动化的，但是当她查看数据时，她立即注意到有些不对劲。

# 数据是整数数组，对应于一段时间内样本中的单元格数。第一个元素是初始计数。下一个元素是稍后的单元格计数。 是下一个计数，依此类推。data[0]data[1]data[2]

# 细胞正在繁殖，因此数组的元素应该是不减少的（没有细胞死亡），但自动细胞计数器被低估了。事实上，研究人员已经验证了计数器随机少计。错误率未知。1

# 您的任务是创建一个与数组差异最小的新非递减数组。例如，如果返回的数组应该是因为显然是一个错误。datadata = [1, 1, 2, 2, 1, 2, 2, 2, 2][1, 1, 2, 2, 2, 2, 2, 2, 2]data[4] < data[3]

# 数组的第一个条目是正确的，不需要调整。
# 数组永远不会为空。
a=[3,1,3,6,9,1,2]
c=[]
def cleaned_counts(data):
    c.append(data[0])
    for i in range(1,len(data)):
        if data[i]<data[i-1]:
            data[i]=data[i-1]
            c.append(data[i])
        else:
            c.append(data[i])
    return c


print(cleaned_counts(a))