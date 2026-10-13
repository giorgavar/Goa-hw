function generateRange(min, max, step) {
  let a = min
  let b = []
  while (a <= max) {
    b.push(a)
    a += step
  }
  return b
}


function switchItUp(number) {
  let z = ""
  switch (number) {
    case 0:
      z = "Zero"
      break
    case 1:
      z = "One"
      break
    case 2:
      z = "Two"
      break
    case 3:
      z = "Three"
      break
    case 4:
      z = "Four"
      break
    case 5:
      z = "Five"
      break
    case 6:
      z = "Six"
      break
    case 7:
      z = "Seven"
      break
    case 8:
      z = "Eight"
      break
    case 9:
      z = "Nine"
      break
  }
  return z
}


function multiply(a, b) {
  let p = 0
  let c = 0
  while (c < Math.abs(b)) {
    p += Math.abs(a)
    c++
  }
  if ((a < 0 && b > 0) || (a > 0 && b < 0)) {
    return -p
  }
  return p
}



function noSpace(x) {
  let a = x.split("")
  let b = a.filter(function(c) {
    return c !== " "
  })
  let d = b.join("")
  return d
}