class PassController:
    def __init__(self):
        self.user_inputs = []

    def generate_passwords(self, answers):
        # Store the user inputs in a list
        self.user_inputs.append(answers)

    def print_user_inputs(self):
        print(self.user_inputs)