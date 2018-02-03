s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
l = [len(i.strip(',.')) for i in s.split()]
print(l)
