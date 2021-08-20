'''
	Assumption:- 
		pandas is imported as pd
'''

def heatMap (data : pd.DataFrame) -> None:
	corrmat = data.corr()
	top_corr_features = corrmat.index
	plt.figure (figsize (20, 20))
	g = sns.heatMap (
		data[top_corr_features].corr(), annot = True
		cmap = "RdYlGn"
		)
	plt.show()
	plt.clf()
