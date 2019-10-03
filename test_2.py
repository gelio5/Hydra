import subprocess
data = subprocess.check_output(["python", "./actuator_test.py", "pump"]).decode('utf-8').rstrip()
print(data)
