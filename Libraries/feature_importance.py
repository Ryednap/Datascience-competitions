'''
	Assumption :- 
		pandas is imported as pd
	About :-
		Used for Feature preprocessing. It shows the top 10 (by default) columns
		that have most influence (high correlation) on the target variable
'''

def show_feature_importance(X : pd.DataFrame, y : pd.Series, howMany = 10) -> None:
	from sklearn.ensemble import ExtraTreesClassifier
	import matplotlib.pyplot as plt

	tree = ExtraTreesClassifier()
	tree.fit(X, y)
	print (tree.feature_importances_) #inbuilt-class
	# plot
	ft_imp = pd.Series(tree.feature_importances_, index = X.columns)
	ft_imp.nlargest(howMany).plot(kind = 'barh')
	plt.show()
	plt.clf()
