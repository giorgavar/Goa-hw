function show(id, text, ok) {
  const el = document.getElementById(id)
  el.textContent = text
  el.className = ok ? "msg ok" : "msg err"
}

document.getElementById("f2").addEventListener("submit", function (e) {
  e.preventDefault()
  const val = document.getElementById("username2").value
  if (val.length < 5 || val.length > 15) {
    show("err2", "სახელი უნდა იყოს 5-დან 15 სიმბოლომდე", false)
    return
  }
  show("err2", "წარმატებით გაიგზავნა", true)
})

document.getElementById("f3").addEventListener("submit", function (e) {
  e.preventDefault()
  const pass = document.getElementById("pass3").value
  const confirm = document.getElementById("confirm3").value
  if (pass !== confirm) {
    show("err3", "პაროლები არ ემთხვევა", false)
    return
  }
  show("err3", "წარმატებით გაიგზავნა", true)
})

document.getElementById("f4").addEventListener("submit", function (e) {
  e.preventDefault()
  const email = document.getElementById("email4").value
  const age = Number(document.getElementById("age4").value)
  const phone = document.getElementById("phone4").value
  if (!email.includes("@") || !email.includes(".")) {
    show("err4", "ელფოსტა არასწორია", false)
  } else if (age <= 18) {
    show("err4", "ასაკი უნდა იყოს 18-ზე მეტი", false)
  } else if (!phone.startsWith("5")) {
    show("err4", "ტელეფონი უნდა იწყებოდეს 5-ით", false)
  } else {
    show("err4", "წარმატებით გაიგზავნა", true)
  }
})

document.getElementById("f5").addEventListener("submit", function (e) {
  e.preventDefault()
  const first = document.getElementById("first5").value
  const last = document.getElementById("last5").value
  const isUpper = (ch) => ch === ch.toUpperCase() && ch !== ch.toLowerCase()
  if (!isUpper(first.charAt(0)) || !isUpper(last.charAt(0))) {
    show("err5", "სახელი და გვარი უნდა იწყებოდეს დიდი ასოთი", false)
    return
  }
  show("err5", "წარმატებით გაიგზავნა", true)
})
