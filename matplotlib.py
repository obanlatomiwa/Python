# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Print the last item from year and pop
year= [23,45,32,67,45,234,2323,32,4,35,57,5,86,4,23,123,123,456,789]
pop=[123,3113,52,13,36,23,78,244,53,53,7,85,47,342,42,1,2,3,4]

print(year[-1])
print(pop[-1])



# Make a Line plot: year on the x-axis, pop on the y-axis
plt.scatter(year, pop)

# Display the plot with plt.show()
plt.show()
