from pydantic import BaseModel, EmailStr,model_validator
#importing model_validator
from typing import List, Dict

class Patient (BaseModel):
    name : str
    email: EmailStr
    age :  int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @model_validator(mode="after") #no field mentioned as working on the whole model
    def validate_emergency_number (cls, model):
        if model.age > 60 and "emergency" not in model.contact_details :
            raise ValueError("Patients older than 60 must have emergency contact no.")
        return model
 

def insert_patient_details(patient: Patient): 
    print (patient.name)
    print (patient.age)
    print (patient.married)
    print (patient.allergies)
    print (patient.email)
    # print (patient.linkedin_id)
    print (patient.contact_details)
    print ("data inserted successfully!")

def updated_patient_details(patient: Patient):
    print (patient.name)
    print (patient.age)
    print ("data updated successfully!")


patient_info = {"name": "Vedansh","email": "abc@sbi.com", "age":"69", "weight": 75.2, "married": True, "allergies": ["pollen", "dust", "bat"], "contact_details": {"phone_no": '9530028305', 'emergency': "6595"}} 

patient1 = Patient(**patient_info) #validation -> after type coersion

insert_patient_details(patient1)