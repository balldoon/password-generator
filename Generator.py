import string, random
def random_generator(chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    print(''.join(random.choice(chars) for x in range(size)))
    input("Please copy your password and press any key to close")
size = input("Password Length : ")
size = int(size)
random_generator()
