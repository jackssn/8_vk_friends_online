import vk


APP_ID = 5398267  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input("Login: ")


def get_user_password():
    return input("Password: ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    all_friends = api.friends.get(fields='online')
    friends_online = [d for d in all_friends if d['online'] == 1]
    friend_names = []
    for friend in friends_online:
        first_name = friend['first_name']
        last_name = friend['last_name']
        friend_name = "%s %s" % (first_name, last_name)
        friend_names.append(friend_name)
    return friend_names

def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend)

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
