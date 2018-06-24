(function (jquery) {
  // ROW MACHINE
  var activeRow = jquery('.row').first()
  var currentLetterBox = activeRow.children().first()
  var currentLetterDiv = null
  currentLetterBox.toggleClass('focused')

  jquery(document).keydown(function (event) {
    if (event.key === 'ArrowUp') {
      activateLetterBox(currentLetterBox)
    }
  })

  function focusOnNextLetterBox (letterBox) {
    currentLetterBox = letterBox.next()
    letterBox.removeClass('focused')
    if (currentLetterBox.length == 0) {
      currentLetterBox = letterBox.siblings().first()
    }
    currentLetterBox.toggleClass('focused')
  }

  function focusOnNextLetterDiv (letterDiv) {
    if (letterDiv === null) {
      letterDiv = currentLetterBox.children()[1]
    }
    currentLetterDiv = letterDiv.next()
    // set selector class to selector
    if (currentLetterDiv.length == 0) {
      currentLetterDiv = letterDiv.siblings()[1]
    }
    // apply new selector position class
    currentLetterDiv.toggleClass('focused')
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
        }
      } else {
        // double blinking
        console.log('trigger double click')
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
    if (!currentLetterBox.hasClass('active')) {
      focusOnNextLetterBox(currentLetterBox)
    } else {
      var selector = currentLetterBox.children().first()
      // just update `currentLetterDiv` here
      if (selector.hasClass('place-1')) {
        // write  second letter
      } else if (selector.hasClass('place-2')) {
        // write  second letter
        // and so on fo other elements
      } else {
        // cancel button
      }
      focusOnNextLetterDiv(currentLetterDiv)
    }
  }

  jquery(document).ready(function () {
   setInterval(mainLoop, 2000);
  })
})($ || {})
