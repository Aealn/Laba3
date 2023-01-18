import yaml

with open('bz.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

'''
print(data,'\n')
print(data['Objects'],'\n')
print(data['Connection'],'\n')
print("длина Objects: ", len(data['Objects']),'\n')
print("длина Connection: ", len(data['Connection']),'\n')

objects = data['Objects']
print(objects)
connection = data['Connection']
print(connection)
print(connection[0],'\n')

print(data['Objects'][0])
print(data['Connection'][0]['type'])
'''
print("Объекты:")
j = 0
for i in data['Objects']:
    print(i)  # data['Objects'][a]
    j += 1

simpt = str(input("Введите объект: "))
# num1 = int(input("Введите номер объекта: "))

print("Связи:")
conn = ['качества', 'навыки', 'кто']  # conn[i]
j = 0
for i in conn:
    print(i)
    j += 1

svyaz = str(input("Введите связь: "))
# num2 = int(input("Введите номер связи: "))

for i in range(len(data['Connection'])):
    if (simpt == data['Connection'][i]['src']):
        if (data['Connection'][i]['type'] == svyaz and data['Connection'][i]['src'] == simpt):
            print("Результат: ", data['Connection'][i]['dst'])
    if (simpt == data['Connection'][i]['dst']):
        if (data['Connection'][i]['type'] == svyaz and data['Connection'][i]['dst'] == simpt):
            print("Результат: ", data['Connection'][i]['src'])

# rezult = кто(num1, num2, data)
# print(rezult)
