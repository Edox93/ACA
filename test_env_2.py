def typecheck(typee):
    def wrap(function):
        def valueChecker(*args):
            for arg in args:
                if type(arg) is not typee:
                    print("Վօռի Եռռօռ")
                    break

            function(*args)

        return valueChecker
    return wrap


@typecheck(str)
def checkValues(a, b, c):
    return "a, b, c"


if __name__ == '__main__':
    checkValues('1', '2', 3)
