class CreateAccountException(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)

    def message(self):
        return self.message


class CreateAccountCreated(Exception):
    pass

