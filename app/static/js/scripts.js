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

  // Handle plus and minus button functionality
  const minusButton = document.getElementById('minusButton');
  const plusButton = document.getElementById('plusButton');
  const itemAmountInput = document.getElementById('itemAmount');

  minusButton.addEventListener('click', function () {
    let currentValue = parseInt(itemAmountInput.value);
    if (currentValue > 1) {
      itemAmountInput.value = currentValue - 1;
    }
  });

  plusButton.addEventListener('click', function () {
    let currentValue = parseInt(itemAmountInput.value);
    itemAmountInput.value = currentValue + 1;
  });

});