import login
import run
import utils


def main():
    if not utils.check_config():
        return

    cookie = login.get_cookie()
    if cookie == 0 or cookie == -1:
        return

    run.run(cookie)


if __name__ == '__main__':
    main()
