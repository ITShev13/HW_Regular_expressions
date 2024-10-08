
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
from tkinter.font import names

with (open("phonebook_raw.csv", encoding="utf-8") as f):
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  # pprint(contacts_list)


# TODO 1: выполните пункты 1-3 ДЗ
# 1. помещаем ФИО в соответствующие поля
# (Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname
# и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО,
# а может быть сразу правильно: Ф+И+О. Подсказка: работайте со срезом списка (три первых элемента)
# при помощи " ".join([:2]) и split(" "), регулярки здесь НЕ НУЖНЫ.)


# формирую словарь из полученного contacts_list
  contacts_dict = []
  table_headers = contacts_list[0]
  table_values = contacts_list[1:]
  for n, z in enumerate(table_values):
    contacts_dict.append({})
    for key, vel in zip(table_headers, z):
      contacts_dict[n].update({key:vel})
  # pprint(contacts_dict)


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



# 2. Привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.
# Подсказка: используйте регулярки для обработки телефонов.

  pattern = r"(\+7|8)?\s*\(?(\d{3})[)-]*\s*(\d{3})\-*(\d{2})\-*(\d{2})(\s\(*(\D{4})\s(\d+)\)?)*"
  substitution = r"+7(\2)\3-\4-\5 \7\8"
  for phone in new_contact:
    res = re.sub(pattern, substitution, phone['phone'])
    phone['phone'] = res
  # pprint(new_contact)


  # 3. Объединить все дублирующиеся записи о человеке в одну.
  # Подсказка: группируйте записи по ФИО (если будет сложно,
  # допускается группировать только по ФИ).



                            #   def contacts_filter(new_contacts):
                            # for contact in new_contacts:
                            #   last_name = contact[0]
                            # first_name = contact[1]
                            # for new_contact in new_contacts:
                            #   new_last_name = new_contact[0]
                            # new_first_name = new_contact[1]
                            # if first_name == new_first_name and last_name == new_last_name:
                            #   if contact[2] == “”: contact[2] = new_contact[2]
                            # if contact[3] == “”: contact[3] = new_contact[3]
                            # if contact[4] == “”: contact[4] = new_contact[4]
                            # if contact[5] == “”: contact[5] = new_contact[5]
                            # if contact[6] == “”: contact[6] = new_contact[6]
                            # result_list = list()
                            # for i in new_contacts:
                            #   if i not in result_list:
                            #     result_list.append(i)
                            # return result_list




  # # pprint(merging_duplicates)
  # for item in new_contact:
  #   # pprint(set(item.values()))
  #   for s in merging_duplicates:
  #     pprint(s)
  #     if item not in s:
  #       merging_duplicates.add(set(item))
  #     else:
  #       set(item) | s
  #
  #
  #     # if item['lastname'] not in merging_duplicates['lastname'] and item['firstname'] not in merging_duplicates['firstname']:
  #     #   merging_duplicates.items(item)
  #     #   pprint(merging_duplicates)
  # # pprint(merging_duplicates)



    # pprint(item)
    # for name in merging_duplicates:
      # print(name)

      # if item['firstname'] and item['lastname'] == name['firstname'] and name['lastname']:
  #     if item['firstname'] == name['firstname'] and item['lastname'] == name['lastname']:
  #       pprint('они совпали')
  #       set(name)|set(item)
  #     else:
  #       pprint('несовпадают')
  #       merging_duplicates.update(item)
  # pprint(merging_duplicates)









    # d = ' '.join(key_[:3]).split(' ')
    # pprint(d)
    # unique_name = {}
    # unik key = key_['lastname']+key_['firstname']+key_['surname']
    # pprint(unique_name)


  # pprint(merging_duplicates)




















# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)

