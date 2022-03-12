import hashlib
message = hashlib.sha256()
message.update(b"Itp2022*")

print(message.hexdigest())
