import hashlib

hash_value = input("Please enter a string to HASH: ")

hash_obj1 = hashlib.md5()
hash_obj1.update(hash_value.encode())
print("MD 5 --> " + hash_obj1.hexdigest())

hash_obj2 = hashlib.sha1()
hash_obj2.update(hash_value.encode())
print("SHA 1 --> " + hash_obj2.hexdigest())

hash_obj3 = hashlib.sha256()
hash_obj3.update(hash_value.encode())
print("SHA 256 --> " + hash_obj3.hexdigest())

hash_obj4 = hashlib.sha512()
hash_obj4.update(hash_value.encode())
print("SHA 512 --> " + hash_obj4.hexdigest()) 