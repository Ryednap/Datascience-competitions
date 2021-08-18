from util import *

def handle_missing_value (data : pd.DataFrame, 
						cStrat = "mode", nStrat = "median") : -> None
	# feature generation
	cat, num = seg_variables (data)
	for col in data.columns:
		if (data[col].isnull().sum() != 0):
			data[col + "_isnull"] = data[col].isnull()

	# imputation
	from sklearn.impute import SimpleImputer
	imp_c_ = SimpleImputer(missing_value= np.nan, strategy = cStrat)
	imp_n_ = SimpleImputer(missing_value= np.nan, strategy = nStrat)
	cols = data.columns # save columns
	categorical = pd.DataFrame(imp_c_.fit_transform(data[cat]))
	numerical = pd.DataFrame(imp_n_.fit_transform(data[num]))

	'''
	need to finish
	'''