def input_error(func):
    def inner(*args, **kwargs):
        print('123')
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return "Give me name please."
        except ValueError as e:
            return "Give me phone please."
        except IndexError as e:
            return "Give me contacts please."

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
