from src.exceptions.ApplicationException import ApplicationException, ApplicationSubmitted


class ApplicationLogic:
    def __init__(self):
        pass

    def handle_application_step(self, step: int, data: dict):
        if step < 1 or step > 5:
            raise ApplicationException('Invalid step')
        if step == 1:
            return self.handle_user_info(data)
        if step == 2:
            return self.handle_user_experience(data)
        if step == 3:
            return self.handle_user_recommendation(data)
        if step == 4:
            return self.handle_user_cover_letter(data)
        if step == 5:
            return self.handle_application(data)
        raise ApplicationException('Invalid step')

    def handle_user_info(self, data: dict):
        print(f'Handling user info: {data}')
        return True

    def handle_user_experience(self, data: dict):
        print(f'Handling user experience: {data}')
        return True

    def handle_user_recommendation(self, data: dict):
        print(f'Handling user recommendation: {data}')
        return True

    def handle_user_cover_letter(self, data: dict):
        print(f'Handling user cover letter: {data}')
        return True

    def handle_application(self, data: dict):
        print(f'Handling application: {data}')
        raise ApplicationSubmitted('Application submitted successfully')
