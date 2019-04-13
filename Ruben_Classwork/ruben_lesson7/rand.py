import itertools
import random
import string


def generate_pwd(length: int) -> str:
    """ Method for generating super-secure paswords

    Parameters
    ----------
    langth : int
        Password length to be generated

    Returns
    -------
    str
        Generated password

    """
    data = list(itertools.chain(string.ascii_letters,
                                string.digits,
                                string.punctuation))

    pwd = []
    for _ in range(length):
        pwd.append(random.choice(data))

    return "".join(pwd)


if __name__ == '__main__':
    print('Password: ', generate_pwd(20))
