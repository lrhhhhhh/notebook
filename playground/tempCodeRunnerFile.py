BUFSIZE = 65536
def get_lines(filename):
    with open(filename, 'r') as fp:
        while True:
            chunk = fp.readlines(8)
            if not chunk:
                raise StopIteration
            yield chunk

cnt = 0

for each in get_lines('playground/test_data.txt'):
    print(each)
print('yes')