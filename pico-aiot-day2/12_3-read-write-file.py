import utime

file = open("test.txt", "w")
file.write("Hello, File!\n")
file.close()

file = open("test.txt")
line=file.readline()
print(line)
file.close()

utime.sleep(3)

file = open("test.txt", "a")
file.write("Append, Hello!\n")
file.close()

file = open("test.txt")
line=file.readline()
line=file.readline()
print(line)
file.close()

