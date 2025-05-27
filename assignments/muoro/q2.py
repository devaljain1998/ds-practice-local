def func(a, L=[]):
    L.append(a)
    return L

print(func(1)) # [1]
print(func(2)) # [2]
print(func(3, [])) # [3]
print(func(4)) # 4

# [1]
# [1, 2]
# [3]
# [1, 2, 4]

def quiz():
    try:
        return 'try'
    finally:
        return 'finally'

print(quiz())