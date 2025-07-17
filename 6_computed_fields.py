from pydantic import BaseModel, EmailStr
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