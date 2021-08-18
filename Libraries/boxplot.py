
def box_plot (data, x, y) -> None:
	try:
		plt.clf()
		plt.figure (figsize = (14, 6))
		sns.boxplot (x = x, y = y, data = df, palette = "Set1")
		plt.xlabel(x)
		plt.ylable(y)
		plt.yticks(fontSize = 16)
		plt.show()
	except NameError as nerr:+
		print ("Name Error occurred in box_plot function")
		print ("One of the plt or sns is not defined")


box_plot("", "", "")

