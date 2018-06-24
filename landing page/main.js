(function (jquery) {
  // ROW MACHINE
  jquery(".letter-box").machine({
    inactive: {
      defaultState: false,
    },
    letter: {
      defaultState: true,
      events: {
        click: "writeletter",
        dblclick: "nextletter",
      },
      onEnter: function( evt, previousState ) {
        console.log('letterState')
      },
    },
    writeletter: {
      onEnter: function( evt, previousState ) {
        console.log('writeLetterState')
        if(evt.target.classList.contains('cancel')) {
          writeletter.onExit(evt, 'letter')
        }
        console.log(evt.target.innerText)
        console.log(evt.target)
      },
      onExit: function( evt, nextState ) {
        // jquery(this).removeClass('active')
      },
      events: {
        click: "letter"
      }
    },
    nextletter: {
      onEnter: function( evt, previousState ) {
        console.log("nextLetterState")
        let classes = jQuery(evt.target).next().attr('class').split(/\s+/)
        for(let class_name in classes) {
          if(class_name.startsWith('place-')) {
            console.log(class_name)
            this.firstChild().removeClass()
          }
        }
      },
      onExit: function( evt, nextState ) {
        // jquery(this).removeClass('active')
      },
      events: {
        click: "letter"
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
