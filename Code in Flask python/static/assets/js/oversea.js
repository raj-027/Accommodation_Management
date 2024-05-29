<script>
    function submitForm() {
      // Code to handle form submission and redirection
    }

    document.addEventListener('DOMContentLoaded', function () {
      const form = document.getElementById('billForm');
      const formDataContainer = document.getElementById('formData');
      const nextEntryBtn = document.querySelector('button[data-action="next-entry"]');
      const newEntryBtn = document.querySelector('button[data-action="new-entry"]');

      let currentRow = 0;
      let currentGroup = document.createElement('tr');
      formDataContainer.appendChild(currentGroup);

      form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent form submission
        const formData = new FormData(form);
        const entry = document.createElement('td');
        entry.textContent = JSON.stringify(Object.fromEntries(formData.entries()));
        currentGroup.appendChild(entry);
        form.reset(); // Reset form fields after submission
      });

      nextEntryBtn.addEventListener('click', function () {
        currentRow++;
        currentGroup = document.createElement('tr');
        formDataContainer.appendChild(currentGroup);
      });

      newEntryBtn.addEventListener('click', function () {
        currentRow = 0;
        currentGroup = document.createElement('tr');
        formDataContainer.appendChild(currentGroup);
      });
    });
  </script>