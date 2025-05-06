// my comment
db.students.aggregate([
  {
    $group: {
      _id: null,
      averageScore: { $avg: "$score" }
    }
  }
]).forEach(doc => printjson(doc))

