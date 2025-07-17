from pydantic import BaseModel, EmailStr,computed_field
#importing computed_field
from typing import List, Dict

class Patient (BaseModel):
    name : str
    email: EmailStr
    age :  int
    weight : float #kgs
    height : float #mtr
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float: #model ka instance as input milta h and the output will be float
        #bmi will be the name of the field of the model now!
        bmi = round(self.weight/(self.height**2),2) #rounding upto 2 decimal values
        return bmi

 

def insert_patient_details(patient: Patient): 
    print (patient.name)
    print (patient.age)
    print (patient.married)
    print (patient.allergies)
    print (patient.email)
    # print (patient.linkedin_id)
    print ("bmi:", patient.bmi)
    print (patient.contact_details)
    print ("data inserted successfully!")

def updated_patient_details(patient: Patient):
    print (patient.name)
    print (patient.age)
    print ("data updated successfully!")


patient_info = {"name": "Vedansh","email": "abc@sbi.com", "age":"69", "weight": 75.2, "married": True,
"height": 1.72, "allergies": ["pollen", "dust", "bat"], "contact_details": {"phone_no": '9530028305', 'emergency': "6595"}} 

patient1 = Patient(**patient_info) #validation -> after type coersion

insert_patient_details(patient1)