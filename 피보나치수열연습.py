book_data = [
    {'title': '파이썬의 정석', 'author': '김파이', 'publisher': 'A-Publish', 'year': 2023},
    {'title': '자바의 유혹', 'author': '박자바', 'publisher': 'Black-List', 'year': 2020}, # 차단 출판사
    {'title': 'C', 'author': '최씨', 'publisher': 'B-Publish', 'year': 1800}, # 제목 짧음 & 연도 이상
    {'title': '알고리즘', 'author': '이알고', 'publisher': 'C-Publish', 'year': 2025},
]

prohibited_publishers = ['Black-List', 'Evil-Books']

def check_book(book):
    errors = []
    if book['publisher'] in prohibited_publishers:
            return 'blcoked'
    if len(book['title']) < 2:
            errors.append('title')
    if book['year'] < 1900 or book['year'] > 2024:
            errors.append('year')
    
    if len(errors) == 0:
        return True
    else :
        return False, errors
    
def process_books(book_data):
    clean_books = []
    invalid_count = 0
    for book in book_data:
        exp = check_book(book)
        if exp is True:
            clean_books.append(book)
        elif exp == 'blcoked':
            invalid_count += 1
        else :
            invalid_count += 1
            err = exp[1]
            for i in err:
                 book[i] = None
            clean_books.append(book)

    print(f'{invalid_count}입니다.')
    return clean_books     

result = process_books(book_data)
print(result)
