 <h1 style="text-align: center;">VisDa: The Data Visualisation Tool</h1>
<h3 style="text-align: center;">Sukriti Macker, Sahil Harwani, Ishwant Singh Bhayana, Satya Vamsi</h3>

## 1. Introduction
Scientific data visualizations are crucial for comprehending, analyzing, and communicating scientific findings. Data visualizations can help researchers in visualizing equations by providing a way to plot and analyze the relationships between variables and parameters in the equation, making it easier to understand and interpret the data. Also, they can help researchers to identify patterns, trends, and relationships in large and complex datasets more quickly and effectively than with raw data alone, leading to new insights and discoveries. The idea of the project is to build a Python program that holds the capacity to visualize scientific data such as spectrograms, 2D or 3D plots, time series or any other representations. To construct several types of visualizations and add interaction, the application will employ various object-oriented principles such as factory methods, inheritance, abstract base classes, and decorators. The application will also include test code to check that it works properly and fits the criteria.

## 2. Project Outline
To construct a program that visualizes scientific data, the project will employ object-oriented programming techniques. The abstract base class for all visualizations will be defined as the base Visualization class. Specific classes will be generated using factory methods and will inherit from the base Visualization class to create distinct visualizations. The SpectrogramVisualization class for spectrograms will use inheritance to optimize unique visuals for certain sorts of data. Callbacks and decorators will be used to provide interactivity to the visualizations. When the user interacts with the visualization, callbacks can update it, and decorators can add tooltips or other capabilities and functions that are interactive. Pytest will be used to write test code to confirm that the software works well and meets the requirements. Each class and method in the application will have corresponding test methods to test their functioning. We intend to use the following to build the project: -

1. Programming Language: Python
2. Libraries: Matplotlib, NumPy, Pandas, and SciPy
3. Testing Framework: pytest

>Descirbe the different plots we plan to implement

>UML Diagram: Explain the different classes attributes we plan to implement

