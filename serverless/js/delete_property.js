const resource_url = "https://vkkm38khe4.execute-api.us-east-1.amazonaws.com/dev/property";
const form = document.getElementById("delete-property-form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const formData = new FormData(form);
  const plainFormData = Object.fromEntries(formData.entries());
  const fetchOptions = {
    method: "DELETE",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(plainFormData),
  };
  fetch(resource_url, fetchOptions)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });
  form.reset();
});
