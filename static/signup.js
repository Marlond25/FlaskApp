const signup = document.getElementById("signup");
const name = document.getElementById("f_name");
const email = document.getElementById("f_email");
const password = document.getElementById("f_password");

const request = (name, email, password) => {
  let xhr = new XMLHttpRequest();
  xhr.open("POST", "/signUp", true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.send(JSON.stringify({
    fname: name,
    femail: email,
    fpassword: password
  }));
}

signup.addEventListener("click", () => { request(name, email, password); });
