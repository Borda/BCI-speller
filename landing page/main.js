(function (jquery) {
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
})($ || {})
