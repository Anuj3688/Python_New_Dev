## TODO: Error handling

try:

    user_age = int(input())

    if user_age > 18:
        print("You can vote")
    else:
        raise Exception('YOUR AGE IS LESS')

except ValueError as err:
    print('We have got a value error because of the user')
except Exception as err:
    print('Problem is being logged')
    print(err)
finally:
    print('FINALLY: PROCESS COMPLETED AFTER HANDLING EXCEPTIONS')
