function calculateTotal() {
  // Get values of maleno, femaleno, and child input fields
  var maleno = parseInt(document.getElementById("maleno").value) || 0;
  var femaleno = parseInt(document.getElementById("femaleno").value) || 0;
  var child = parseInt(document.getElementById("child").value) || 0;

  // Calculate total by adding the values
  var total = maleno + femaleno + child;

  // Set the calculated total in the Total input field
  document.getElementById("total").value = total;
}

// Call the calculateTotal function whenever any of the input fields change
document.addEventListener("DOMContentLoaded", function () {
  var inputs = document.querySelectorAll("input[type='number']");
  inputs.forEach(function (input) {
    input.addEventListener("input", calculateTotal);
  });
});
// //for default date
// document.addEventListener("DOMContentLoaded", function () {
//   var today = new Date();
//   var fromDateInput = document.getElementById("fromDate");
//   var formattedDate = today.toISOString().substr(0, 10); // Format: YYYY-MM-DD
//   fromDateInput.value = formattedDate;
// });
//to calculate to date from no of days
document.addEventListener("DOMContentLoaded", function () {
  var fromDateInput = document.getElementById("fromDate");
  var toDateInput = document.getElementById("toDate");
  var numberOfDaysInput = document.getElementById("numberOfDays");

  fromDateInput.addEventListener("change", updateNumberOfDays);
  toDateInput.addEventListener("change", updateNumberOfDays);

  function updateNumberOfDays() {
    var fromDate = new Date(fromDateInput.value);
    var toDate = new Date(toDateInput.value);

    if (!isNaN(fromDate.getTime()) && !isNaN(toDate.getTime())) {
      var differenceInTime = toDate.getTime() - fromDate.getTime();
      var differenceInDays = Math.round(differenceInTime / (1000 * 3600 * 24));

      if (differenceInDays >= 0) {
        numberOfDaysInput.value = differenceInDays + 1; // Add 1 to include both start and end dates
      } else {
        numberOfDaysInput.value = "";
      }
    } else {
      numberOfDaysInput.value = "";
    }
  }
});
//for calculating the number of days
function updateToDate() {
  var fromDateInput = document.getElementById("fromDate");
  var numberOfDaysInput = document.getElementById("numberOfDays");
  var toDateInput = document.getElementById("toDate");

  var fromDate = new Date(fromDateInput.value);
  var numberOfDays = parseInt(numberOfDaysInput.value);

  if (!isNaN(fromDate.getTime()) && !isNaN(numberOfDays)) {
    var toDate = new Date(fromDate);
    toDate.setDate(fromDate.getDate() + numberOfDays);
    toDateInput.valueAsDate = toDate;
  }
}
