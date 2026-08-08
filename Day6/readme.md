Start
Read the integer x.
Check whether x is negative and store its sign.
Convert x into a positive number.
Set rev = 0.
Repeat while x > 0:
Get the last digit of x.
Remove the last digit from x.
Add the digit to rev.
Check if rev is greater than 2147483647.
If it is greater, return 0.
Add the original sign to rev.
Return the reversed number.
Stop.