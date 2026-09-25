from abc import ABC, abstractmethod

class PatientSystemAbstract(ABC):
    
    @abstractmethod
    def patient_storing(self, patient_file):
        pass

    @abstractmethod
    def add_patient(self, patient):
        pass

    @abstractmethod
    def filter_terms(self):
        pass

    @abstractmethod
    def get_patient(self, patient_id):
        pass
        
    @abstractmethod
    def graph_attributes(self):
        pass

    @abstractmethod
    def update_patient(self, patient):
        pass

    @abstractmethod
    def remove_patient(self, patient_id):
        pass

    @abstractmethod
    def average_attribute(self, patient_id):
        pass