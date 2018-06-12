conv = open('train.txt','r').readlines()
conv2 = []
for ic, i in enumerate(conv):
    conv2.append(i.replace('\t', ' '))
data = []
for i in conv2:
    conv3 = i.split()
    conv3 = tuple(conv3)
    data.append(conv3)
df = pd.DataFrame.from_records(data)