import pymongo

# Step 1: Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["resultdb"]

users_collection = db["users"]
students_collection = db["students"]

# Step 2: Get user input
username = input("Enter your username: ")
password = input("Enter your password: ")

# Step 3: Authenticate the user
user = users_collection.find_one({"username": username, "password": password})

if user:
    roll_no = user["roll_no"]
    student = students_collection.find_one({"roll_no": roll_no})

    if student:
        print("\n✅ Login successful! Here's your result:\n")
        print(f"👤 Name     : {student.get('name', 'N/A')}")
        print(f"🎓 Roll No  : {student.get('roll_no', 'N/A')}")

        marks = student.get("marks", {})
        aggregate = marks.get("aggregate", "N/A")
        status = marks.get("status", "N/A")

        print(f"📊 Aggregate: {aggregate}")
        print(f"📌 Status   : {status}")
    else:
        print("❌ Student record not found.")
else:
    print("❌ Invalid username or password.")
