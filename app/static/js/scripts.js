document.addEventListener('DOMContentLoaded', () => {
  // Handle navbar burger functionality
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  if ($navbarBurgers.length > 0) {
    $navbarBurgers.forEach(el => {
      el.addEventListener('click', () => {
        const target = el.dataset.target;
        const $target = document.getElementById(target);

        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }
});

// Set option id to hidden input value with selected_option id
function setSelectedoption(optionId) {
  var selectedoptionInput = document.getElementById('selected_option');
  if (selectedoptionInput) {
    selectedoptionInput.value = optionId;
  } else {
    console.error('Could not find selected_option input element.');
  }
}


// Enables users to select only one option at a time from a list, 
// updating the visual representation of radio buttons accordingly
function toggleIcon(element) {
  // Get all the option items
  const optionItems = document.querySelectorAll('.option-item');

  // Deselect all other options
  optionItems.forEach(item => {
    // Check if the item is not the parent of the clicked element
    if (item !== element.parentElement) {
      // Remove the 'selected' class from other options
      item.classList.remove('selected');
      // Reset the display of radio button icons for other options
      const icons = item.querySelectorAll('ion-icon');
      icons.forEach(icon => {
        if (icon.classList.contains('radio-btn-off-item')) {
          icon.style.display = 'inline-block';
        } else if (icon.classList.contains('radio-btn-on-item')) {
          icon.style.display = 'none';
        }
      });
    }
  });

  // Toggle the class 'selected' on the clicked option
  element.parentElement.classList.toggle('selected');

  // Get the icons within the clicked option
  const icons = element.parentElement.querySelectorAll('ion-icon');

  // Toggle the display of the icons based on the presence of the 'selected' class
  icons.forEach(icon => {
    if (element.parentElement.classList.contains('selected')) {
      // If the option is selected, hide the off radio button icon and show the on radio button icon
      if (icon.classList.contains('radio-btn-off-item')) {
        icon.style.display = 'none';
      } else if (icon.classList.contains('radio-btn-on-item')) {
        icon.style.display = 'inline-block';
      }

      // Get the option ID
      const optionId = element.getAttribute('data-option');
      // Set the selected option
      setSelectedoption(optionId);
    }
    else {
      // If the option is not selected, show the off radio button icon and hide the on radio button icon
      if (icon.classList.contains('radio-btn-off-item')) {
        icon.style.display = 'inline-block';
      } else if (icon.classList.contains('radio-btn-on-item')) {
        icon.style.display = 'none';
      }
    }
  });

}