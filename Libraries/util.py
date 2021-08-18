def seg_variables (data : pandas.DataFrame) : -> tuple
	cat = [var for var in data.columns if (data[var].dtype == 'O')]
	num = [var for var in data.columns if (var not in cat)]
	return (cat, num)
