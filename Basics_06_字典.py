'''
字典
'''

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print('You just earned ' + str(new_points) + ' points!')

# 添加键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# 修改字典中的值
alien_0['color'] = 'yellow'

print(alien_0)
