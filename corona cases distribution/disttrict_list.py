import re
import csv


#pattern_text = r'{\'(?P<name>\w+)\':\'(?P<name_val>\w+)\',\'(?P<age>\w+)\':\'(?P<age_val>\d+)\'}'
#pattern_text = r'{\'(?P<name>\w+)\':\'(?P<value>\w+)\'}'
#pattern_text = r'{\'(?P<name>\w+)\':[(?P<value>\d+).(?P<value>\d+)]}'
#pattern_text = r'{(?P<name>\w+)}'


with open('copy_districts_list.txt') as file1:
    lines = file1.readlines()
    lines_len = len(lines)


pattern_text = r'{\"(?P<_id>\w+)\":\"(?P<_id_val>\w+)\",\"(?P<id>\w+)\":(?P<id_val>\d+),\"(?P<title>\w+)\":\"(?P<title_val>\w+)\",\"(?P<title_en>\w+)\":\"(?P<title_en_val>\w+)\",\"(?P<code>\w+)\":\"(?P<code_val>\w+)\",\"(?P<province>\w+)\":(?P<province_val>\d+)},'
pattern = re.compile(pattern_text)

with open('\csv data\district_list.csv','a') as csv_file:
    writer_obj = csv.writer(csv_file)
    writer_obj.writerow(['district_id','district_name','province'])
    for i in range(lines_len):
        match = pattern.match(lines[i])
        district_id = match.group('id_val')
        district_name = match.group('title_val')
        province = match.group('province_val')
        print(f'id: {district_id}, District: {district_name}, Province: {province}')
        writer_obj.writerow([district_id,district_name,province])
        
        
