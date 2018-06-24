# Working with different interaction states

## If you need to highlight which row of button is active
- add class `row-selected` to that row (and remove it from all other rows so only one row is highlighted at one time)

## If you need to highlight letter box
- add class `focused` to that letter box (and remove it from all other letter boxes so only one letter box is highlighted at one time)

## If needs to zoom-in letter box
- add class `active` to the div with `letter-box` class and it will scale it up. when you remove the `active` class, it will scale back down (so only one letter box is scaled-up at one time)

### If needs to move with the green selection in active `.letter-box`
- add class `place-2` or `place-3` or `place-cancel` to the div with `selector` class and it will move to correct position

## If you need to fill "input" for new message text
- fill content into the div with ID `#new-text`


# Functional specs:
- When you have some row highlighted, automatically switch from one letter box to another (every 3 seconds). If you reach the last letter box in the row, start again with first letter box in that same row ( = switching between rows should user does intentionally)
- When you have some letter box scaled up, automatically switch from one letter to another (every 3 seconds), and then to Cancel button. Then continue with again with first letter in that letter box (until user selects something)

# Gestures / Signals
- When some letter box is focused, and user sends signal (`1 click`), letter box will scale-up. It should be appliad new class `.letter-activated` to the div with the class `keyboard`
- When some letter box is scaled up, and user sends signal (`1 click`), letter will be written into text area. Letter box then scales down and we automatically start another automatic switching from "A B C" letter box
- When user send `2-click signal`, we switch between rows. When we get to the 3rd row, and user sends 2-click signal, we switch to first row again. When user has 3rd highlighted and sends `1-click signal`, we send the message (message should appear up in the white area and text from input should be deleted).

