names_ip= input("Enter the names seperated by a spaces")
names_list=sorted(names_ip.split())
names_tuple=tuple(names_list)

file_name='names_data.txt'
with open(file_name,'w') as writer:
    writer.write(f'List: {names_list}\n')
    writer.write(f'Tuple: {names_tuple}')

with open(file_name,'r') as reader:
    line_list=reader.readline()
    line_tuple=reader.readline()
    print(line_list)
    print(line_tuple) 