import datetime

def decor(function_name):
    def wrapper(some_argument):
        print('111' + '/' + str(some_argument.upper()))
        function_name(some_argument)
        print('1111' + '/' + str(some_argument.upper()))
    return wrapper


def decor2(function_name):
    def wrapper(some_argument):
        print('222' + '/' + str(some_argument))
        function_name(some_argument)
        print('2222' + '/' + str(some_argument))
    return wrapper


@decor
@decor2
def now(some_argument):
    print('ololo' + '/' + str(some_argument))
    #print(datetime.datetime.now(some_argument))


now('ololo')