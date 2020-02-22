#! python

num = '31.1481.1531.1551.1551.15541.4251.4631.4811.4921.49651.6021.6721.7151.7491.76461.7291.8221.8871.9441.97371.8281.9382.0202.0972.13981.9092.0322.1262.2212.27491.9772.1102.2152.3232.387102.0362.1762.2902.4102.482112.0882.2342.3552.4852.564122.1342.2852.4122.5502.636132.1752.3312.4622.6072.699142.2132.3712.5072.6592.755152.2472.4092.5492.7052.806162.2792.4432.5852.7472.852172.3092.4752.6202.7852.894182.3352.5042.6512.8212.932192.3612.5322.6812.8542.968202.3852.5572.7092.8843.001'
table = {'n': [0.900, 0.950, 0.975, 0.990, 0.995]}

for i in range(7):  #(len(num)/column):
    index_ = i*26
    key = num[index_]
    vaules = []
    for j in range(5):
        vaules.append(num[index_+1:index_+6])
        #print(vaules)
        index_ += 5
    table[key] = vaules

for i in range(10,21):
    index_ = 7*26 + (i-10)*27
    key = num[index_:index_+2]
    vaules = []
    for j in range(5):
        print(key,index_)
        print(num[index_+2:index_+7])
        vaules.append(num[index_+2:index_+7])
        print(vaules)
        index_ += 5
    table[key] = vaules
print(table)
with open('grubbs.txt','w') as f:
    f.write(str(table))