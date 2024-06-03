window.addEventListener('DOMContentLoaded', () => {
  const selects = document.querySelectorAll('.control-group select')
  console.log('this thing on?')

  const manageLabelClass = (element, remove = false) => {
    if(!remove) element.classList.add('up')
    else element.classList.remove('up')
  }

  selects.forEach(select => {
    console.log(select)
    const label = document.querySelector(`label[for=${select.name}]`)

    select.addEventListener('focus', () => {
      manageLabelClass(label)
    })

    select.addEventListener('blur', (e) => {
      if(e.target.value) manageLabelClass(label)
      else manageLabelClass(label, true)
    })
  })

})
