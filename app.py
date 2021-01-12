from collections import defaultdict

infile = open("Static/Mileage.txt", 'r')
M = [line.rstrip().split(',') for line in infile]
infile.close()

def takeSecond(elem):
    return elem[1]

sorted_list = []
with open('Static/Mileage.txt', 'w') as f:
    for item in M:
        sorted_list.append(item)
        sorted_list.sort(key=takeSecond, )#reverse=True)
    for item in sorted_list:
        f.write("%s\n" %",".join(item))

a,b,model,gal,mpg = 0,0,0,0,0
sortedL = []
observation = []

for i in sorted_list:
    t = (i[0], i[1])
    observation.append(t[0])

observation = list(dict.fromkeys(observation))

for x in sorted_list:
        model = str(sorted_list[a][0])
        gal = float(sorted_list[a][1])
        mpg = round(100 / gal,2)
        nothaL = sorted_list[a]
        nothaL.append(mpg)
        sortedL.append(nothaL)
        sortedL.sort(key=takeSecond, reverse=True)
        a+=1

model_to_observations = defaultdict(lambda: [])
def add(observation):
    model_to_observations[observation[0]].append(float(observation[2]))

list(map(add, M))
print("Model".ljust(15), "MPG".ljust(15))
for key in model_to_observations:
    print(str(key).ljust(15), str(round(sum(model_to_observations[key])/len(model_to_observations[key]),2)).ljust(15))


