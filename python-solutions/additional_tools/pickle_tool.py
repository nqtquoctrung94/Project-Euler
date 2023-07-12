import pickle
import os

class pickle_dictionary:
    def __init__(self, file_name: str):
        self.path = fr"additional_tools\pickle_{file_name}.pickle"

    def save(self, input_dict: dict):
        with open(self.path, "wb") as file:
            pickle.dump(input_dict, file)

    def load(self):
        if os.path.exists(self.path):
            with open(self.path, "rb") as file:
                return pickle.load(file)
        return None

# Sample code
# from additional_tools.pickle_tool import pickle_dictionary
# pickle_dictionary(file_name="fibonacci").save(input_dict=fibonacci_dict)
# fibonacci_dict = pickle_dictionary(file_name="fibonacci").load()