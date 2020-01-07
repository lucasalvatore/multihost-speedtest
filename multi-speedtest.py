import subprocess
import csv

servers = open('test-servers', 'r')
output = []
cmd_list = []
cmds = "speedtest-cli --csv --server "
for line in servers:
    line = line.strip()
    cmd_list.append([cmds + line])

print("Staring test run on", len(cmd_list), "servers")

with open('results.csv', 'w', newline='') as results:
    writer = csv.writer(results, quoting=csv.QUOTE_NONE, escapechar=' ', quotechar='', lineterminator='\n')
    for line_num, i in enumerate(cmd_list, start=1):
        try:
            print("Test number", line_num, "of", len(cmd_list))
            x = subprocess.check_output(i, shell=True).decode()
            writer.writerow([x])
        except subprocess.CalledProcessError as e:
            print(e)
            pass
            
