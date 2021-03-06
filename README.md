# Outlier Detection in the Bus System of City of Rio de Janeiro

This project is divided in two parts:

1- A Convolutional Neural Network (CNN) trained on a semi-supervised fashion to automatically detect outliers on the trajections of the city of Rio de Janeiro. The models were trained using [Caffe framework](http://caffe.berkeleyvision.org/).

2- An online vizualization tool that help users identify and understand outlier buses (outliers) in the bus routes of Rio de Janeiro. These outliers can be spatial --  e.g. buses running outside their average route (far from where they are likely to be) -- or temporal -- e.g. delayed buses.
In order to run the visualization tool you only need to run a local python server (`python -m SimpleHTTPServer`). This repository already contains some sample data. However, the original data can be obtained in a stream (daily) fashion [here](http://data.rio.rj.gov.br/dataset/gps-de-onibus) or [here](http://sel.ic.uff.br/bus/).
For a more detailed explanation please refer to the [project description](project_proposal.pdf). You can try out [the live demo](http://rodrigonogueira4.github.io/BusData/Outlier_Vis/outlier_v1.html) and
watch the [video](http://vimeo.com/1234567) to better understand how to interact with the tool.
