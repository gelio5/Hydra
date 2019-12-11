import subprocess

process = subprocess.Popen("./TitleSnap.exe", stdout=subprocess.PIPE)
data = process.communicate()
print(data[0].decode())
