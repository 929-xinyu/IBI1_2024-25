# Project Plan:
# 1. The purpose of this code is to create a class named "Patients" that represents patients in a hospital.
# 2. The class will have attributes such as name, age, admission date, and medical history.
# 3. It will include a method to print the patient's details in a formatted manner.
# 4. The class will be instantiated with sample patient data to demonstrate its functionality.
# 5. The code will be organized and structured for clarity and readability.
# 6. The code will be tested with sample data to ensure it works as intended.

class Patients:
    def __init__(self, name, age, admission_date, medical_history):
        self.name = name
        self.age = age
        self.admission_date = admission_date
        self.medical_history = medical_history

    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Admission Date: {self.admission_date}, Medical History: {self.medical_history}")

# the example I give is to use it to test the code.
patient1 = Patients("Zhang San", 29, "2024-05-28", "Diabetes")
patient1.print_details()