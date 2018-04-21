from sklearn import tree

names = ["F", "D", "A+"]
features = [[35], [39], [42], [83]]
labels = [0, 0, 1, 2]

classifier = tree.DecisionTreeClassifier()

classifier.fit(features, labels)

output = classifier.predict([[32], [39], [38], [37], [44], [96], [80]])

print(output)

import graphviz 
dot_data = tree.export_graphviz(classifier, out_file=None) 
graph = graphviz.Source(dot_data)
graph.render("scores")
