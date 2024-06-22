#!/usr/bin/python3

import fractions

die_A = die_B = [1,2,3,4,5,6]

def challenge1(dieA, dieB):
	#dieA = dieB = [1,2,3,4,5,6]

	max_sum = 12

	sums = []

	for num1 in dieA:
		for num2 in dieB:
			print(f"Combo: {num1},{num2}",end="     ")
			sumnum = num1 + num2
			print(f"Sum: {sumnum}")
			sums.append(sumnum)

	#print(len(sums))

	for i in range(max_sum+1):
		probability = fractions.Fraction(sums.count(i), len(sums))
		val = sums.count(i)/len(sums)
		print(f"Probability for {i}: {probability.numerator}/{probability.denominator} Percentage: {round(val*100, 2)}%")


	return sums





def undoom_dice(die_1, die_2):
	new_die_1 = []
	new_die_2 = []
	print("\nDice Undoom!")

	for i in die_1:
		if i < 4:
			new_die_1.append(i)
			new_die_2.append(i)
		else:
			new_die_1.append(i - (i % 4))   # Make sure that Die A has no A[x] > 4
			new_die_2.append(i + (i % 4))   # Add the subtracted number to Die B

  # I couldn't match the exact probabilities of each sum in Un-doomed dice, I don't even know if that's mathematically possible or not. Tried different array combination. :)

	print(f"Undoomed Die A = {new_die_1}")
	print(f"Undoomed Die B = {new_die_2}")

	

if __name__ == "__main__":
  challenge1(die_A,die_B)
  undoom_dice(die_A,die_B)
