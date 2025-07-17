from pydantic import BaseModel
from typing import List, Dict, Optional #to implement List[str] and Dict[str]

class Patient (BaseModel):
    name : str
    age : int
    weight: float
    married : bool = False #default value
    allergies: Optional[List[str]]= None #but andr ki saari values str honi chaiye and none is the default value
    contact_details : Dict[str, str] #for both the key:value pairs

def insert_patient_details(patient: Patient): 
    print (patient.name)
    print (patient.age)
    print (patient.married)
    print (patient.allergies)
    print (patient.contact_details)
    print ("data inserted successfully!")

def updated_patient_details(patient: Patient):
    print (patient.name)
    print (patient.age)
    print ("data updated successfully!")


patient_info = {"name": "Vedansh", "age":"19", "weight": 75.2, "married": True, "allergies": ["pollen", "dust", "bat"], "contact_details": {"email":"vedanshmathur007@gmail.com", "phone_no": '9530028305'}} 
#giving values to all the fields in must otherwise error
patient1 = Patient(**patient_info) #raw data

insert_patient_details(patient1)
# updated_patient_details(patient1)


