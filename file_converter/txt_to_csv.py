import csv

# read the txt files
file1 = '../nyishi/nyishi_pp.txt'
file2 = '../nyishi/english_pp.txt'


def read_txt(file_name):
    # Read the contents of the text file
    with open(file_name, 'r', encoding="utf-8") as f:
        data = f.read().splitlines()
    return data


def write_csv(data1, data2, output_file_name):
    # Write the contents into a CSV file
    with open(output_file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in zip(data1, data2):
            writer.writerow(row)


# .................................................
data1 = read_txt(file_name=file1)
data2 = read_txt(file_name=file2)

write_csv(data1=data1, data2=data2, output_file_name='../nyishi/nyishi_pp.csv')
