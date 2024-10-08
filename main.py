
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

# 0. Читаем файл в формате csv
def read_f_csv (file_name):
  # with (open("phonebook_raw.csv", encoding="utf-8") as f):
  with (open(f"{file_name}", encoding="utf-8") as f):
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    return contacts_list

# TODO 1: выполните пункты 1-3 ДЗ
# 1. помещаем ФИО в соответствующие поля
# (Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname
# и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО,
# а может быть сразу правильно: Ф+И+О. Подсказка: работайте со срезом списка (три первых элемента)
# при помощи " ".join([:2]) и split(" "), регулярки здесь НЕ НУЖНЫ.)

def name_in_appropriate_fields (contacts_list):
# формирую словарь из полученного contacts_list
  contacts_dict = []
  table_headers = contacts_list[0]
  table_values = contacts_list[1:]
  for n, z in enumerate(table_values):
    contacts_dict.append({})
    for key, vel in zip(table_headers, z):
      contacts_dict[n].update({key:vel})
  # проверяем ФИО и расставляем в соответствующие ключи
  # проверяем фамилию (если в поле более одного слова ФИ или ФИО)
  new_contact = contacts_dict
  for full_name in new_contact:
    lastname_parts = full_name['lastname'].split()
    if len(lastname_parts) > 2:
      full_name['lastname'] = lastname_parts[0]
      full_name['firstname'] = lastname_parts[1]
      full_name ['surname'] = lastname_parts[2]
    if len(lastname_parts) > 1:
      full_name['lastname'] = lastname_parts[0]
      full_name['firstname'] = lastname_parts[1]

  # проверяем имя (если в поле более одного слова ИО)
    firstname_parts = full_name['firstname'].split()
    if len(firstname_parts) > 1:
      full_name['firstname'] = firstname_parts[0]
      full_name ['surname'] = firstname_parts[1]
  return new_contact

# 2. Привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
# Подсказка: используйте регулярки для обработки телефонов.

def fix_phone_template (new_contact):
  pattern = r"(\+7|8)?\s*\(?(\d{3})[)-]*\s*(\d{3})\-*(\d{2})\-*(\d{2})(\s\(*(\D{4})\s(\d+)\)?)*"
  substitution = r"+7(\2)\3-\4-\5 \7\8"
  for phone in new_contact:
    res = re.sub(pattern, substitution, phone['phone'])
    phone['phone'] = res
    return new_contact



  # 3. Объединить все дублирующиеся записи о человеке в одну.
  # Подсказка: группируйте записи по ФИО (если будет сложно,
  # допускается группировать только по ФИ).

def name_merging (new_contact):
  result_list = list()
  for con in new_contact:
    lastname = con['lastname']
    firstname = con['firstname']
    for n_con in new_contact:
      new_lastname = n_con['lastname']
      new_firstname = n_con['firstname']
      if firstname == new_firstname and lastname == new_lastname:
        if con['surname'] == '': con['surname'] = n_con['surname']
        if con['organization'] == '': con['organization'] = n_con['organization']
        if con['position'] == '': con['position'] = n_con['position']
        if con['phone'] == '': con['phone'] = n_con['phone']
        if con['email'] == '': con['email'] = n_con['email']
    if con not in result_list:
      result_list.append(con)
  return result_list

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

def write_to_file_csv (result_list):
  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    return datawriter.writerows(result_list)

if __name__ == '__main__':
  contacts_list = read_f_csv(file_name='phonebook_raw.csv')
  new_contact = name_in_appropriate_fields(contacts_list)
  fix_phone = fix_phone_template(new_contact)
  result_list = name_merging(fix_phone)
  write_to_file_csv(result_list)
