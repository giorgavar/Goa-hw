function checkAlive(n) {
  let r = false
  if (n > 0) {
    r = true
  } else {
    r = false
  }
  return r
}



function capitalize(s) {
  let a = s.split("")
  let b = []
  let c = []
  
  for (let i = 0; i < a.length; i++) {
    if (i % 2 === 0) {
      b.push(a[i].toUpperCase())
      c.push(a[i].toLowerCase())
    } else {
      b.push(a[i].toLowerCase())
      c.push(a[i].toUpperCase())
    }
  }
  
  let d = b.join("")
  let e = c.join("")
  return [d, e]
}



function DNAtoRNA(dna) {
  let a = dna.split("")
  let b = []
  for (let i = 0; i < a.length; i++) {
    let c = a[i]
    if (c === "T") {
      b.push("U")
    } else {
      b.push(c)
    }
  }
  let d = b.join("")
  return d
}




function isKiss(words) {
  let a = words.split(" ")
  let b = 0
  for (let i = 0; i < a.length; i++) {
    let c = a[i].length
    if (c > b) {
      b = c
    }
  }
  let d = a.length
  let e = "Keep It Simple Stupid"
  if (b <= d) {
    e = "Good work Joe!"
  }
  return e
}