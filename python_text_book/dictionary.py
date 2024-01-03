"""
 store values in key value pair is known as doictionay
"""

#create a a person personal details 
justin = {
    "first_name":"Justin",
    "last_name":"biber",
    "age":24,
    "city":"hydrabad"
    }
for keys in justin:
    print(f"{keys} is {justin[keys]}")

#write a five members names and their favorite numbers
guys ={
    "muthu":2,
    "arasu":2,
    "pandi":7,
    "uthaya":7,
    "archunan":8
    }
for key in guys.keys():
    print(f"{key} favrt number is {guys[key]}")

programming_words ={
    "list":"The list is collection of values we can access them via index.",
    "dictionary":"The dictionaay is a collection of the key and value pairs. assign name of the values instead of index.",
    "if-condition":"In programming language conditional statements plays crusial roles ike if you want to buy book search under 500rs that's also one of filter.",
    "tuples":"tuple is string pool and this values are immutable.",
    "looping":"In your code you do some piece of code repeated multiple time that you go to looping statements."
    }
for key in programming_words.keys():
    print(f"{key}:\n \t{programming_words[key]}")


# in dictionary we have the key and value pair and also we can  access seperately 
rivers={"ganga":"allahabad",
        "arayu":"ayodhaya",
        "gomti":"lucknow",
        "vaigai":"madurai",
        "kaveri":"erode"
        }

for river in sorted(rivers.keys()):
    print(f"we have the river {river.title()} in india.")
    print(f"The {river.title()} pass through {rivers.get(river)}")