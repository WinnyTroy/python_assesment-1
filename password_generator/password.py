import random
import string


# decorator function to format password generator
def pass_decorator(func):
    def wrap_pass():
        print("Your New password")
        func()
        print("*-"*5 + "\nThank you.")
    return wrap_pass()


class Password(object):
    """
    static method will perform the random password generator
    get a random choice from the ascii letters and digits and symbols for range between 1-10
    join the string to get one full password
    validate_scale: function to check if the user scale is an integer and is in range 1-10
    """
    def __init__(self, scale):
        self.scale = scale

    @pass_decorator
    def generate_pass(self):
        return ''.join(random.choice(string.ascii_letters + string.digits + ".',={}[]-/|\£$%^&*()_+~#@?><") for _ in range(self.scale))

    @staticmethod
    def validate_scale(n):
        return isinstance(n, int) and range(1, 11)


def user_request():
    # request user pass and store user response
    user_req = input("New Password?")
    hard_pass_opt = input("How strong a password? Scale from 1-10")
    # call generate pass
    user_req = user_req.upper()
    if Password.validate_scale(hard_pass_opt):
        try:
            if user_req == "Y" or user_req == "YES":
                new_password = Password(hard_pass_opt)
                return new_password.generate_pass()
        except TypeError:
            return "Oh Shacks! Error. Please Try again."
    else:
        return "Please enter a valid number for your scale."

print(user_request())
