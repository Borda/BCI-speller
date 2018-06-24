(function (jquery) {
  // ROW MACHINE
  var activeRow = jquery('.row').first()
  var currentLetterBox = activeRow.children().first()
  var currentLetterDiv = null
  currentLetterBox.toggleClass('focused')

  jquery(document).keydown(function (event) {
    if (event.key === 'ArrowUp') {
      if (currentLetterDiv !== null) {
        jquery('#new-text').text(
          jquery('#new-text').text() + currentLetterDiv.innerText
        )
        currentLetterDiv = null
      }
      activateLetterBox(currentLetterBox)
    }
  })

  function runIt () {
    console.log('running it with cap!')
    if (currentLetterDiv !== null) {
      jquery('#new-text').text(
        jquery('#new-text').text() + currentLetterDiv.innerText
      )
      currentLetterDiv = null
    }
    activateLetterBox(currentLetterBox)
  }

  function focusOnNextLetterBox (letterBox) {
    currentLetterBox = letterBox.next()
    letterBox.removeClass('focused')
    if (currentLetterBox.length == 0) {
      currentLetterBox = letterBox.siblings().first()
    }
    currentLetterBox.toggleClass('focused')
  }

  function focusOnNextLetterDiv (letterDiv, position, selector) {
    selector.removeClass('place' + '-' + position)
    selector.addClass('place' + '-' + (position + 1))
  }

  function activateLetterBox (letterBox) {
    letterBox.removeClass('focused')
    letterBox.toggleClass('active')
  }

  // WEBSOCKETS STUFF
  var webSocket = jquery.simpleWebSocket({
    url: 'ws://192.168.7.14:8000/ws/bci/U123/'
  })

    // reconnected listening
    webSocket.listen(function(message) {
      var data = message.data
      console.log(data)
      if (data.amount === 1) {
        // single blinking
        if (data.eyes === 'right') {
          console.log('trigger right arrow')
        } else if (data.eyes === 'left') {
          console.log('trigger left arrow')
        } else {
          // both eyes
          console.log('trigger single click')
          // runIt()
        }
      } else {
        // double blinking
        console.log('trigger double click')
        // runIt()
      }
    })

  // MAIN LOOP
  var focusedRowIndex = 0
  var activeRow = jquery('.row').first()

  var focusedLetterBox = null
  var focusedLetter = null

  var activeLetterBox = null
  var activeLetter = null

  function mainLoop () {
    let position = 1;
    var selector = null;
    if (!currentLetterBox.hasClass('active')) {
      focusOnNextLetterBox(currentLetterBox)
    } else {
      selector = currentLetterBox.children().first()
      position = selector.attr('class').split(' ').pop()
      position = parseInt(position.split('-').pop())
      try {
        let letter = currentLetterBox.children()[position].innerText
      } catch (e) {
        console.log('cancel')
        position = 1
      }
      if(!currentLetterDiv){
        currentLetterDiv = currentLetterBox.children()[position]
      }
      focusOnNextLetterDiv(currentLetterDiv, position, selector)
    }
  }

  jquery(document).ready(function () {
   setInterval(mainLoop, 2000);
  })
})($ || {})
