import psutil

print("cpu_percent", psutil.cpu_percent())

print("vitual memory", psutil.virtual_memory())
# you can convert that object to a dictionary 
dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
print(psutil.virtual_memory().percent)

# you can calculate percentage of available memory
print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

