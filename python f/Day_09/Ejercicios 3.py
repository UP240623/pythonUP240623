person={
    'first_name': 'Fernando',
    'last_name': 'Bautista',
    'age': 18,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['Python', "Blender", "Arduino"],
    'address': {
        'street': 'Alcazar Calzada Navarra',
    }
    }

if "skills" in person:
    print(person["skills"][int(len(person["skills"])//2)])
    print("Python" in person["skills"])
    if "Javascript" and "React" in person["skills"]:
        print("He is a front end developer")
    elif "Node" and "Python" and "MongoDB" in person["skills"]:
        print("He is a backend developer")
    elif "Node" and "React" and "MongoDB" in person["skills"]:
        print("He is a fullstack developer")
    elif "Python" and "Arduino" in person["skills"]:
        print("He is a student developer")
    else:
        print("Unknown title")
else:
    print("The person doesn´t have any described skills.")