use('students_db');

db.students.insertOne({
  name: "George", age: 24, gender: "Male", roll_no: "107",
  marks: { math: 85, physics: 80, chemistry: 90 },
  aggregate: 85,
  status: "Pass"
});
mongosh < project_mongodb.js 
