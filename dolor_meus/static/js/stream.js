window.addEventListener('DOMContentLoaded', () => {
  const viewBox = document.getElementById('view_box')
  const requestButton = document.getElementById('request_button')
  const numSelect = document.getElementById('number')
  const subjectSelect = document.getElementById('subject')

  let number = null
  let subject = ''

  const getLorem = async() => {
    // should wrap in try-catch for errors    
    const response = await fetch('/ai', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        subject: `${number} paragraphs on ${subject}`
      })
    })

    numSelect.value = ''
    subjectSelect.value = ''

    const reader = response.body.getReader()
    viewBox.innerHTML = ''
    let isDone = false
    while(!isDone) {
      const {done, value} = await reader.read()

      const decoder = new TextDecoder()
      const freshText = decoder.decode(value)
      viewBox.innerHTML += freshText.replaceAll('\n', '</br>')
      isDone = done
    }

  }

  requestButton.addEventListener('click', getLorem)

  const assignVal = ({ target }) => {
    if(target.name == 'subject') subject = target.value
    else number = target.value
  }

  subjectSelect.addEventListener('change', assignVal)
  numSelect.addEventListener('change', assignVal)

})
