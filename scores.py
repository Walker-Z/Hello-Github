# !/usr/bin/python3
f = open('scores.txt')
lines = f.readlines()
print(lines)
print()
f.close()

results = []

for line in lines:
    data = line.split()
    # print(data)
    sum: int = 0

    for score in data[1:]:
        sum += int(score)
    # print(results)
    results.append('% s: % d' % (data[0], sum))

output = open('result.txt', 'w')
for re in results:
    output.write(re)
    output.write('\n')
output.close()
f = open('result.txt')
data = f.read()
print(data)
f.close()
