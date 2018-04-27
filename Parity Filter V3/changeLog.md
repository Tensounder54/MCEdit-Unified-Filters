# Parity Filter Change Log  #

----------

V1: 

- **Released!**

V2:

- **Added** option to replace. This means that you can now select a specific block to replace rather than just filling the selection.

- **Improvement** Made the algorithm more efficient and generally cleaned up the code.


V3: 

- **Removed** tick boxes for selection by ‘X’, ‘Y’ and ‘Z’.

- **Removed** line from UI that says: “Enabling 'Output Log?' will slow down the filter and write a lot of text to the 
console.” and added this to the Notes Tab.

- **Added** line to Notes Tab that says: “Count mode works best when the height of the selection box is odd.”

- **Added** line to Perform Tab that says: “*See Notes tab for details.”

- **Added** `Mode` function to Perform Tab that allows for a selection of different modes.

- **Migrated** existing ‘X’, ‘Y’ and ‘Z’ selection options to the `Mode` dropdown. Drop Down options include:
 - "X&Y&Z"
 - "X&Y"
 - "X&Z"
 - "Y&Z"
 - "X"
 - "Y"
 - "Z"
 - "Count"

- **Added** new selection mode called `Count`. This allows the user to select even blocks when from an arbitrary counter rather than ‘X’, ‘Y’ and ‘Z’.