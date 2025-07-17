from pydantic import BaseModel

class Address (BaseModel):
    city: str
    state : str
    pin : str

class Patient (BaseModel):
    name : str
    gender: str
    age: int 
    address: Address #nested model

address_info = {"city": "jaipur", "state": "rajasthan", "pin": '3020xx'}
address1= Address(**address_info)

patient_info = {"name":"vedansh", "gender": "male", "age":19, "address": address1 } #sending the details of address made above
patient1 = Patient(**patient_info)

print (patient1)
#name='vedansh' gender='male' age=19 address=Address(city='jaipur', state='rajasthan', pin='3020xx')

print (patient1.name)
print (patient1.address.city)
print (patient1.address.pin)