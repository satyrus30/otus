import requests
import json
from pathlib import Path
from csv import DictReader as DR

ENDPOINT = ('books.csv', 'users.json')
KEY_PERSON_RESULT = ('name', 'gender', 'address', 'age')
KEY_BOOK_RESULT = ('Title', 'Author', 'Genre', 'Pages')


def download_file_from_github(endpoint=ENDPOINT):
    for path in endpoint:
        url = f'https://raw.githubusercontent.com/konflic/examples/master/data/{path}'
        response = requests.get(url=url)

        with open(path, 'wb') as csv_file:
            csv_file.write(response.content)


def get_path_to_file_the_proj(file_name):
    """
    Получение пути расположения файла.
    Если файла нет -> UnboundLocalError: local variable 'path' referenced before assignment
    :param file_name: Название файла
    :return: путь до файла
    """
    for path in Path().rglob(file_name):
        continue
    return path


def read_csv_del_of_unnecessary_keys(path, desired_keys):
    with open(path) as readable_file:
        reader = DR(readable_file)
        final_list = list()
        for row in reader:
            for elem in list(row):
                if elem not in desired_keys:
                    row.pop(elem, None)
            final_list.append(row)
    return final_list, len(final_list)


def read_json_file(path):
    with open(path) as readable_file:
        return json.load(readable_file)


def dict_del_of_unnecessary_keys(file, desired_keys=KEY_PERSON_RESULT):
    final_list = list()
    for row in file:
        for elem in list(row):
            if elem not in desired_keys:
                row.pop(elem, None)
        row['books'] = []
        final_list.append(row)
    return final_list, len(final_list)


def filing_json_file(path, data):
    with open(path, 'w') as writable_file:
        json.dump(data, writable_file, indent=4)


def delete_file(*args):
    for del_elem in args:
        path = Path(get_path_to_file_the_proj(del_elem))
        path.unlink()


def result_file():
    download_file_from_github()
    book_path = get_path_to_file_the_proj('books.csv')
    user_path = get_path_to_file_the_proj('users.json')

    read_json = read_json_file(path=user_path)
    final_list, number_persons = dict_del_of_unnecessary_keys(file=read_json, desired_keys=KEY_PERSON_RESULT)
    filing_json_file(path='users.json', data=final_list)

    read_csv, number_books = read_csv_del_of_unnecessary_keys(path=book_path, desired_keys=KEY_BOOK_RESULT)
    filing_json_file(path='books.json', data=read_csv)

    books_for_person = number_books // number_persons

    read_user_json = read_json_file(path='users.json')
    read_books_json = read_json_file(path='books.json')

    add_books_to_person(read_books_json=read_books_json, read_user_json=read_user_json,
                        books_for_person=books_for_person)

    delete_file('books.csv', 'books.json', 'users.json')


def add_books_to_person(read_books_json, books_for_person, read_user_json):
    with open('result.json', 'w') as result_json:
        ind_pers = 0
        remaining_ind = False
        ind_book = 0
        while ind_pers <= len(read_user_json) - 1:

            while ind_book <= len(read_books_json) - 1:
                if (ind_book + 1) % books_for_person == 0:
                    read_user_json[ind_pers]['books'].append(read_books_json[ind_book])
                    ind_book += 1
                    if ind_book <= len(read_books_json) - 1 and ind_pers == len(read_user_json) - 1:
                        ind_pers = -1
                        remaining_ind = True
                    break
                elif remaining_ind:
                    read_user_json[ind_pers]['books'].append(read_books_json[ind_book])
                    ind_book += 1
                    break

                read_user_json[ind_pers]['books'].append(read_books_json[ind_book])
                ind_book += 1
            ind_pers += 1
        json.dump(read_user_json, result_json, indent=4)


if __name__ == "__main__":
    result_file()
