// my comment
db.students.find({}, { _id: 0, name: 1, score: 1 }).sort({ score: -1 }).forEach(doc => printjson(doc))

