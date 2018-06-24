(function (jquery) {
  // jquery(".row").machine({
  //   inactive: {
  //     defaultState: true,
  //     events: {
  //       dblclick: "active"
  //     }
  //   },
  //   active: {
  //     onEnter: function( evt, previousState ) {
  //       jquery(this).addClass('row-selected')
  //     },
  //     onExit: function( evt, nextState ) {
  //       jquery(this).removeClass('row-selected')
  //     },
  //     events: {
  //       click: "inactive"
  //     }
  //   }
  // })

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
})($ || {})
