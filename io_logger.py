class IoLogger:
    def __init__(self):
        self.log = []

    def input(self, prompt):
        # Add prompt to I/O log.
        self.log.append(prompt)

        # Prompt user.
        response = input(prompt)

        # Add response to I/O log.
        self.log.append(f'{response}\n')

        return response

    def print(self, object_):
        # Add object to I/O log.
        self.log.append(f'{str(object_)}\n')

        # Print object.
        print(object_)

    def save_log(self):
        file_name = self.input('File name:\n')

        # Write log to file.
        with open(file_name, 'w') as file:
            file.writelines(self.log)

        self.print('The log has been saved.')
