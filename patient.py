class Patient:
    # Author: Grace, Karan and Diego
    def __init__(self, age: int, sex: int, chest_pain: int, cholesterol: int, ekg: int, max_hr: int, heart_disease: str, patient_id: int):
        self._age = age
        self._sex = sex
        self._chest_pain = chest_pain
        self._cholesterol = cholesterol
        self._ekg = ekg
        self._max_hr = max_hr
        self._heart_disease = heart_disease
        self._patient_id = patient_id

    # Author:  Karan Athwal
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if(value > 0):
            self._age = value
        else:
            print("Invalid age please try again: ")

    @property
    def cholesterol(self):
        return self._cholesterol

    @cholesterol.setter
    def cholesterol(self, value):
        if(value > 0):
            self._cholesterol = value
        else:
            print("Invalid cholesterol input please try again: ")

    # Author: Diego Osorio
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        if(value == 1 or value == 0):
            self._sex = value
        else:
            print("Invalid entry try 1(Male) or 0(Female).")

    @property
    def chest_pain(self):
        return self._chest_pain

    @chest_pain.setter
    def chest_pain(self, value):
        if(value >= 1 and value <= 10):
            self._chestPain = value
        else:
            print("Invalid entry try a number between 1-10.")

    # Author: Karan Athwal, Diego Osorio
    @property
    def ekg(self):
        return self._ekg

    @ekg.setter
    def ekg(self, value):
        if(value >= 0):
            self._ekg = value
        else:
            print("Invalid number, please try again (values cannot be negative): ")

    #Author: Grace
    @property
    def max_hr(self):
        return self._max_hr

    @max_hr.setter
    def max_hr(self, value):
        if (value > 0):
            self._max_hr = value
        else:
            print("Invalid entry, please try again")

    @property
    def heart_disease(self):
        return self._heart_disease

    @heart_disease.setter
    def heart_disease(self, value):
        if (value == "Presence" or value == "Absence"):
            self._heart_disease = value
        else:
            print("Please try again: Is there a Presence or Absence of heart disease?")

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, value):
        if(value > 0):
            self._patient_id = value
        else:
            print("Invalid ID please try again: ")