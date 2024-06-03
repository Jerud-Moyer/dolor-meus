const nameArr = '...dolor sit amet meus'.split('')

window.addEventListener('DOMContentLoaded', () => {
  const nameDisplay = document.getElementById('name_reader')
  let idx = 0
  let popCount = 0

  let lettersTimer = setInterval(() => {
    if(!nameDisplay.classList.contains('show-cursor')) nameDisplay.classList.add('show-cursor')
    if(idx >= 17 && popCount <= 8) {
      const newArr = nameDisplay.textContent.split('')
      newArr.pop()
      nameDisplay.textContent = newArr.join('')
      popCount ++
    } else {
      nameDisplay.textContent = nameDisplay.textContent + nameArr[idx]
      idx ++
    }
    if(!nameArr[idx]) {
      nameDisplay.classList.remove('show-cursor')
      return clearInterval(lettersTimer)
    }
  }, 100)

  const modalTrigger = document.getElementById('more')
  const modal = document.getElementById('more_modal')

  modalTrigger.addEventListener('click', () => {
    modal.classList.add('visible')
  })

  modal.addEventListener('click', (e) => {
    if(e.target === modal) {
      modal.classList.remove('visible')
    }
  })
})
