document.addEventListener("DOMContentLoaded", function() {
  const stateSelect = document.getElementById("state");
  const citySelect = document.getElementById("city");

  // City options for each country
  const citiesByState = {
    "Karnataka": ["Bengaluru", "Belagavi", "Bijapur", "Mysuru", "Hubli", "Gulbarga", "Davanagere", "Mangaluru"],
    "Andhra Pradesh": ["Anantapur", "Vijayawada", "Visakhapatnam", "Guntur", "Kurnool", "Tirupati", "Kakinada"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Thane", "Nashik", "Aurangabad", "Solapur", "Navi Mumbai"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tiruppur", "Erode", "Vellore"],
    "Delhi": ["New Delhi", "North Delhi", "South Delhi", "East Delhi", "West Delhi", "Central Delhi", "North West Delhi"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Allahabad", "Ghaziabad", "Meerut", "Noida"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar"]
}

  // Function to populate city options based on selected country
  function populateCities() {
    const selectedState = stateSelect.value;
    const cities = citiesByState[selectedState] || [];

    // Clear existing options
    citySelect.innerHTML = "";

    // Add new options
    cities.forEach(function(city) {
      const option = document.createElement("option");
      option.value = city;
      option.text = city;
      citySelect.appendChild(option);
    });
  }

  // Event listener for country selection change
  stateSelect.addEventListener("change", populateCities);

  // Form submission event listener
  const signupForm = document.getElementById("signup-form");
  signupForm.addEventListener("submit", function(event) {
    event.preventDefault();

    // Perform form validation
    const firstNameInput = document.getElementById("first-name");
    const lastNameInput = document.getElementById("last-name");
    const dobInput = document.getElementById("date-of-birth");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirm-password");

    // Perform your validation logic here
    // Example validation: Checking if all fields are filled
    if (
      firstNameInput.value &&
      lastNameInput.value &&
      dobInput.value &&
      emailInput.value &&
      passwordInput.value &&
      confirmPasswordInput.value
    ) {
      // If all fields are filled, submit the form
      signupForm.submit();
    } else {
      // Display an error message or perform other actions
      alert("Please fill in all fields");
    }
  });
});
