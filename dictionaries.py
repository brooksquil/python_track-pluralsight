student = {
    "name": "Mark",
    "student_id": 15151,
    "feedback": None
}

student["last_name"] = "Smith"
try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("error finding last_name")
except TypeError as error:
    print("nope")
    print(error)
# except Exception:
#     print("Unknown")