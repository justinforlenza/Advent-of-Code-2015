import hashlib

secret = 'iwrupvqb'


def computeMD5hash(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()


print(computeMD5hash('iwrupvqb346385'))

blah = 1
count = 0

while blah:
    print('Tyring ' + secret + str(count))
    hashed = computeMD5hash(secret+str(count))
    print('The Hash is ' + hashed)
    if hashed[:6] == '000000':
        print('Success!!')
        blah = 0
    count += 1