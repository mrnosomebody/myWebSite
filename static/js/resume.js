window.onload = function () {
  let tabs= document.querySelectorAll('.tab-container__control');
  let contents = document.querySelectorAll('.tab-container__tab');
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].addEventListener('click', (event) => {
      let currentTabs = event.target.parentElement.children
      for (let j = 0; j < tabs.length; j++) {
        currentTabs[j].classList.remove('tab-container__control_active')
      }
      event.target.classList.add('tab-container__control_active')

      for (let j = 0; j < tabs.length; j++) {
        contents[j].classList.remove('tab-container__tab_shown')
      }
      contents[i].classList.add('tab-container__tab_shown')
    })
  }
}