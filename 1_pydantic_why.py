from pydantic import BaseModel

class Patient (BaseModel): #importing basemodel class 
    name : str
    age : int
#made pydantic model in whuch we defined the schema

def insert_patient_details(patient: Patient): #object patient of Patient (model) type 
    print (patient.name)
    print (patient.age)
    print ("data inserted successfully!")

def updated_patient_details(patient: Patient): #object patient of Patient (model) type 
    print (patient.name)
    print (patient.age)
    print ("data updated successfully!")


patient_info = {"name": "Vedansh", "age":"19"} 
patient1 = Patient(**patient_info) #raw data

insert_patient_details(patient1)
updated_patient_details(patient1)


