document.getElementById("f2").addEventListener("submit", function (e) {
  const val = document.getElementById("username2").value;
  if (val.length < 5 || val.length > 15) {
    e.preventDefault();
    document.getElementById("err2").textContent =
      "სახელი უნდა იყოს 5-დან 15 სიმბოლომდე";
  }
});

document.getElementById("f3").addEventListener("submit", function (e) {
  const pass = document.getElementById("pass3").value;
  const confirm = document.getElementById("confirm3").value;
  if (pass !== confirm) {
    e.preventDefault();
    document.getElementById("err3").textContent = "პაროლები არ ემთხვევა";
  }
});

document.getElementById("f4").addEventListener("submit", function (e) {
  const email = document.getElementById("email4").value;
  const age = Number(document.getElementById("age4").value);
  const phone = document.getElementById("phone4").value;
  const err = document.getElementById("err4");
  if (!email.includes("@") || !email.includes(".")) {
    e.preventDefault();
    err.textContent = "ელფოსტა არასწორია";
  } else if (age <= 18) {
    e.preventDefault();
    err.textContent = "ასაკი უნდა იყოს 18-ზე მეტი";
  } else if (!phone.startsWith("5")) {
    e.preventDefault();
    err.textContent = "ტელეფონი უნდა იწყებოდეს 5-ით";
  }
});

document.getElementById("f5").addEventListener("submit", function (e) {
  const first = document.getElementById("first5").value;
  const last = document.getElementById("last5").value;
  const isUpper = (ch) => ch === ch.toUpperCase() && ch !== ch.toLowerCase();
  if (!isUpper(first[0]) || !isUpper(last[0])) {
    e.preventDefault();
    document.getElementById("err5").textContent =
      "სახელი და გვარი უნდა იწყებოდეს დიდი ასოთი";
  }
});
