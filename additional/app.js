const form = document.querySelector("#form");
let lastName = document.querySelector("#last-name");
let classSection = document.querySelector("#class-section");
let uuid = localStorage.getItem("uuid");
let main = document.querySelector(".container");

if (!uuid) {
  uuid = crypto.randomUUID();
  localStorage.setItem("uuid", uuid);
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  submission = {
    lastName: lastName.value,
    classSection: classSection.value,
    uuid: uuid,
  };
  console.log(submission);

  main.innerHTML = '<h1 class="thank-you">Thank You</h1>';
});
