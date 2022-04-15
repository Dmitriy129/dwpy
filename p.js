const res = require("./s.json")

const arr = res.usergrades
  .map(usergrade => usergrade.courseid === 47 && usergrade.gradeitems)
  .reduce((acc, gradeitems) => (
    gradeitems
      ? [
        ...acc,
        ...gradeitems.filter(item => item.iteminstance === 552)
      ]
      : acc
  ), [])
  .map(({ iteminstance, categoryid, cmid }) => ({ iteminstance, categoryid, cmid }))

console.log(arr.length)
console.log(arr.every(({ cmid }) => cmid === 1553))

// userfullname
const arr2 = Array.from(/* new Set */(
  res.usergrades
    .map(usergrade => {
      const grade = usergrade.gradeitems.filter(item => item.iteminstance === 552)[0].graderaw
      return usergrade.courseid === 47
        && !isNaN(String(grade))
        && grade
    }
      // && (usergrade.userfullname)
    )
    .filter(e => !isNaN(String(e)) || !!e)

  // .map(usergrade =>
  //   usergrade.courseid === 47
  //   && usergrade.gradeitems.filter(item => item.iteminstance === 552 && (item.graderaw ?? false))[0]
  //   && (usergrade.userfullname + usergrade.gradeitems.filter(item => item.iteminstance === 552)[0].graderaw)
  // )
))

console.log(arr2.length)
