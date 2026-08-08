Start
Set left = 0 and right = n - 1.
Set max_water = 0.
Calculate the width between left and right.
Find the smaller height of the two lines.
Calculate the water capacity.
Update max_water if the current capacity is greater.
If height[left] < height[right], move left one step forward.
Otherwise, move right one step backward.
Repeat steps 4–9 until left and right meet.
Return max_water.
Stop.