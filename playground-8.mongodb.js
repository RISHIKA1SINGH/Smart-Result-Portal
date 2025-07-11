use("resultdb");

db.students.insertMany([
  {
    name: "John Doe",
    age: 21,
    gender: "Male",
    roll_no: "R001",
    marks: { Math: 60, Science: 55, English: 70, aggregate: 61.67, status: "Pass" }
  },
  {
    name: "Jane Smith",
    age: 21,
    gender: "Female",
    roll_no: "R002",
    marks: { Math: 35, Science: 40, English: 60, aggregate: 45.0, status: "Pass" }
  },
  {
    name: "Ravi Kumar",
    age: 22,
    gender: "Male",
    roll_no: "R003",
    marks: { Math: 80, Science: 85, English: 75, aggregate: 80.0, status: "Pass" }
  },
  {
    name: "Sneha Patil",
    age: 20,
    gender: "Female",
    roll_no: "R004",
    marks: { Math: 68, Science: 72, English: 70, aggregate: 70.0, status: "Pass" }
  },
  {
    name: "Amit Shah",
    age: 23,
    gender: "Male",
    roll_no: "R005",
    marks: { Math: 60, Science: 55, English: 65, aggregate: 60.0, status: "Pass" }
  },
  {
    name: "Priya Mehta",
    age: 22,
    gender: "Female",
    roll_no: "R006",
    marks: { Math: 30, Science: 25, English: 28, aggregate: 27.67, status: "Fail" }
  }
]);
