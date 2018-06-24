(function (jquery) {

  // ROW MACHINE
  jquery(".row").machine({
    inactive: {
      defaultState: true,
      events: {
        dblclick: "active"
      }
    },
    active: {
      onEnter: function( evt, previousState ) {
        jquery(this).addClass('row-selected')
      },
      onExit: function( evt, nextState ) {
        jquery(this).removeClass('row-selected')
      },
      events: {
        click: "inactive"
      }
    }
  })


  // WEBSOCKETS STUFF
  var webSocket = jquery.simpleWebSocket({
    url: 'ws://localhost:8000/ws/bci/U123/'
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
    var activeRow = jquery('.row-selected')
    if (activeRow.length == 1) {
      activeRow = activeRow.first()
    } else {
    }
  }

  jquery(document).ready(function () {
   setInterval(mainLoop, 1000);
  })
})($ || {})
