Algorithm: Zigzag Conversion
Start
Read the string s and number of rows numRows.
If numRows is 1 or greater than/equal to the length of the string, return the original string.
Create numRows empty rows.
Set current_row = 0 and direction as down.
Read each character of the string one by one.
Add the character to the current row.
If the current row is the first or last row, change the direction.
Move to the next row according to the direction.
Repeat steps 6–9 until all characters are processed.
Join all the rows together to get the converted string.
Return the converted string.
Stop.