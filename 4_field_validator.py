from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
#importing field_validator
#importing model_validator
from typing import List, Dict, Optional, Annotated

class Patient (BaseModel):
    name : str
    email: EmailStr
    age :  int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]

    #1st case
    @field_validator('email')
    @classmethod
    def email_validator (cls, value):
        valid_domains = ["hdfc.com", "icici.com", "sbi.com"]
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value
    

    #2nd case
    @field_validator('name')
    @classmethod
    def transform_name(cls , value):
        return value.upper()
    
    #example of mode of field_validator
    @field_validator('age', mode="before")
    @classmethod
    def validate_age (cls , value):
        if 0< value<100:
            return value
        else :
            raise ValueError("Age should be in between 0 and 100")
        #'<' not supported between instances of 'int' and 'str'
        # before type coersion str doesnt allow comparitive operator
        # thats why mode of field_validator is "after"



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


patient_info = {"name": "Vedansh","email": "abc@sbi.com", "age":"19", "weight": 75.2, "married": True, "allergies": ["pollen", "dust", "bat"], "contact_details": {"phone_no": '9530028305'}} 

patient1 = Patient(**patient_info) #validation -> after type coersion

insert_patient_details(patient1)