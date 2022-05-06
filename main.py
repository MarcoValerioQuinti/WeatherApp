from data import GetData

# data = GetData.get_data()

# GetData.jprint(data)

gd = GetData('rome')

temp = gd.max_temp()
print(temp)