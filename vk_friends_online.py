import vk
import getpass


def get_user_login():
    return input("Login: ")


def get_user_password():
    return getpass.getpass()


def get_online_friends(login, password, APP_ID):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friend_online_ids = api.friends.getOnline()
    return api.users.get(user_ids=friend_online_ids)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    APP_ID = int(input('APP ID: '))  # get here: https://vk.com/dev
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password, APP_ID)
    output_friends_to_console(friends_online)
