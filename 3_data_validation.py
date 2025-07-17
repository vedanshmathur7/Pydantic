from pydantic import BaseModel, EmailStr, AnyUrl, Field #emailstr and anyurl is the custom datatype
from typing import List, Dict, Optional, Annotated

class Patient (BaseModel):
    # name : str = Field(max_length=50) # name not longer than 50 chars
    name : Annotated[str, Field(max_length=50, title="name of the patient", description="give the name of the patient", examples=["vedansh", "kamlesh"])]
    linkedin_id : AnyUrl
    email: EmailStr
    age : int= Field(gt=0, lt=120) #gt is greater than and lt is less than
    weight: Annotated[float, Field(gt=0, strict=True)] # strict stops typeconversion 
    # married : bool = False 
    married : Annotated[bool, Field(default=None, description="is the patient married or not?")]
    # allergies: Optional[List[str]]= None 
    allergies: Annotated[Optional[List[str]], Field(default= None,max_length=5)]
    contact_details : Dict[str, str] 

def insert_patient_details(patient: Patient): 
    print (patient.name)
    print (patient.age)
    print (patient.married)
    print (patient.allergies)
    print (patient.linkedin_id)
    print (patient.contact_details)
    print ("data inserted successfully!")

def updated_patient_details(patient: Patient):
    print (patient.name)
    print (patient.age)
    print ("data updated successfully!")


patient_info = {"name": "Vedansh", "linkedin_id": "https://www.linkedin.com/in/vedansh-mathur-86767a300/","email": "abc@gmail.com", "age":"19", "weight": 75.2, "married": True, "allergies": ["pollen", "dust", "bat"], "contact_details": {"phone_no": '9530028305'}} 
# "abc@gmail.com" if @ is removed then will throw an error
# if removed https: part, will throw an error
patient1 = Patient(**patient_info) 

insert_patient_details(patient1)