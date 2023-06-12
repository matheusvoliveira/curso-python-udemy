import csv
import pdb

data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

for line in data_lines[:5]:
    print(line)


all_emails = []

#armazena todos os emails em uma lista
def emails():
    all_emails = []
    print('\n\n')
    for line in data_lines:
        all_emails.append(line[3])
    print(all_emails)

def names():
    full_names = []
    for line in data_lines:
        full_names.append(line[1] + ' '+line[2])
    print(full_names)



file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()
f = open('to_save_file.csv',mode='a', newline='')
csv_writer = csv_writer(f)
csv_writer.writerow(['1','2','3'])
f.close()

emails()
names()
data_lines[10]


pdb.set_trace()