"""
    STORAGE = {
        'B': 1,
        'KB': 1 * 1024,
        'MB': 1 * 1024 * 1024,
        'GB': 1 * 1024 * 1024 * 1024,
        'TB': 1 * 1024 * 1024 * 1024 * 1024,
        'PB': 1 * 1024 * 1024 * 1024 * 1024 * 1024,
        'EB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'ZB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'YB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'NB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'DB': 1 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
    }


    def format_storage(size):
        last_item = ''

        for item in STORAGE:
            if size < STORAGE[item]:
                return '%.2f%s' % (size / STORAGE[last_item], last_item)
            else:
                last_item = item

    print(format_storage(1025))
"""

"""
import json

user_info = json.dumps({'username': 'bamboo', 'password': 123}).encode('utf-8')

print(user_info)
print(type(json.loads(user_info.decode('utf-8'))))
"""

"""
b = bytes()

b += bytes('我们', encoding='utf-8')

print(b.decode('utf-8'))
"""

inp = 'post|E:\project\domain.txt'

commad_list = inp.split("|")
local_path = commad_list[1]
target_path = ''

if len(commad_list) == 3:
    target_path = commad_list[2]

if target_path == '':
    local_path = local_path.replace('\\', '/')
    print(local_path)
    print(local_path.split('/'))
