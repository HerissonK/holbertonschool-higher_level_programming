document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloElement = document.getElementById('hello');
      if (helloElement) {
        helloElement.textContent = data.hello;
      }
    })
});