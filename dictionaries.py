customer = {
    "name": "Saurabh",
    "age": "22",
    "is_verified": True
}
print(customer.get("d.o.b"))
print(customer.get("name"))
print(customer.get("d.o.b", "Aug 8 2001"))

