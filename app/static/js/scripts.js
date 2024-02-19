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

// Set choice id to hidden input value with selected_choice id
function setSelectedChoice(choiceId) {
  var selectedChoiceInput = document.getElementById('selected_choice');
  if (selectedChoiceInput) {
    selectedChoiceInput.value = choiceId;
  } else {
    console.error('Could not find selected_choice input element.');
  }
}


// Enables users to select only one choice at a time from a list, 
// updating the visual representation of radio buttons accordingly
function toggleIcon(element) {
  // Get all the choice items
  const choiceItems = document.querySelectorAll('.choice-item');

  // Deselect all other choices
  choiceItems.forEach(item => {
    // Check if the item is not the parent of the clicked element
    if (item !== element.parentElement) {
      // Remove the 'selected' class from other choices
      item.classList.remove('selected');
      // Reset the display of radio button icons for other choices
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

  // Toggle the class 'selected' on the clicked choice
  element.parentElement.classList.toggle('selected');

  // Get the icons within the clicked choice
  const icons = element.parentElement.querySelectorAll('ion-icon');

  // Toggle the display of the icons based on the presence of the 'selected' class
  icons.forEach(icon => {
    if (element.parentElement.classList.contains('selected')) {
      // If the choice is selected, hide the off radio button icon and show the on radio button icon
      if (icon.classList.contains('radio-btn-off-item')) {
        icon.style.display = 'none';
      } else if (icon.classList.contains('radio-btn-on-item')) {
        icon.style.display = 'inline-block';
      }

      // Get the choice ID
      const choiceId = element.getAttribute('data-choice');
      // Set the selected choice
      setSelectedChoice(choiceId);
    }
    else {
      // If the choice is not selected, show the off radio button icon and hide the on radio button icon
      if (icon.classList.contains('radio-btn-off-item')) {
        icon.style.display = 'inline-block';
      } else if (icon.classList.contains('radio-btn-on-item')) {
        icon.style.display = 'none';
      }
    }
  });

}