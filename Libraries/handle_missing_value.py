from util import *

def handle_missing_value (data : pd.DataFrame, 
						cStrat = "mode", nStrat = "median") : -> None
	# feature generation
	cat, num = seg_variables (data)
	for col in data.columns:
		if (data[col].isnull().sum() != 0):
			data[col + "_isnull"] = data[col].isnull()
