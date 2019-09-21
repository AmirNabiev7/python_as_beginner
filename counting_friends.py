FRIENDS = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']


def print_friends_count(friends_count):
    if friends_count == 1:
        print('У тебя 1 друг')
    elif 2 <= friends_count <= 4:
        print('У тебя ' + str(friends_count) + ' друга')
    elif friends_count >= 5:
        print('У тебя ' + str(friends_count) + ' друзей')



def process_query(query):
    if query == 'Сколько у меня друзей?':
        print('У тебя 5 друзей')

    else:
        print('<неизвестный запрос>')
    print("Привет, я Анфиса!")
    count = len(FRIENDS)
    print_friends_count(count)
    if query == 'Кто все мои друзья?':
        print('Твои друзья: ' + ', '.join(FRIENDS))


process_query('Сколько у меня друзей?')
process_query('Как меня зовут?')
process_query('Кто все мои друзья?')
