# Project Plan:
# 1. The purpose of this code is to create a class named "Patients" that represents patients in a hospital.
# 2. Define the function and input the parameter such as name, age, admission date and medical history.
# 3. Print the patient's details,
# 4. Set an example(patient data) to demonstrate its functionality.
# 5. Test the sample data to ensure it works as the way we want.

class Patients: # define a method for the coordinator class
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history

    def print_details(self): # define the "print_details" method to print the patient's details
        # print the patient's details
        print(f"Name: {self.name}, Age: {self.age}, Admission Date: {self.admission_date}, Medical History: {self.medical_history}")

# the example I give is to use it to test the code.
patient1 = Patients("Zhang San", 29, "2024-05-28", "Diabetes")
patient1.print_details()