 <h1 style="text-align: center;">VisDa: The Data Visualisation Tool</h1>
<h3 style="text-align: center;">Sukriti Macker, Sahil Harwani, Ishwant Singh Bhayana, Satya Vamsi</h3>

## 1. Introduction

### 1.1. Motivation

Scientific data visualizations are crucial for comprehending, analyzing, and communicating scientific findings. Data visualizations can help researchers in visualizing equations by providing a way to plot and analyze the relationships between variables and parameters in the equation, making it easier to understand and interpret the data. Also, they can help researchers to identify patterns, trends, and relationships in large and complex datasets more quickly and effectively than with raw data alone, leading to new insights and discoveries. The idea of the project is to build a Python program that solves certain mathematical equations and algorithms and then holds the capacity to visualize scientific data obtained from them as spectrograms, 2D or 3D plots, time series or any other representations. To construct several types of visualizations and add interaction, the application will employ various object-oriented principles such as factory methods, inheritance, abstract base classes, and decorators. The application will also include test code to check that it works properly and fits the criteria. We will then use Sphinx to create documentation, which will be deployed along with the program.

### 1.2. Project Outline

To construct a program that computes and visualizes scientific data, the project will employ object-oriented programming techniques. The abstract base class for all visualizations will be defined as the base Visualization class. Specific classes will be generated using factory methods and will inherit from the base Visualization class to create distinct visualizations. 

Provided below is the project outline:

1. Understand the theory of the Mathematical equations and implement them using Python.
2. Compute the specified Mathematical Equation based on the input provided using a YAML file.
3. Write code to store the output in a meaningful manner to be later retrieved for visualization.
4. Implemnt appropriate visualization/graphs for the computed equations.
5. Create GUI for the program
6. Write code to generate documentation using Sphinx

### 1.3. Desired Code Functionality

1. Input: The program should accept the user's equation as an input in a mathematical format, such as a string or a function. The input can be taken through a user interface or as an argument in a function. The equation should be in a form that can be processed by the program, such as a symbolic expression.

2. Mathematical Processing: The program should process the equation using existing Python libraries like SymPy, NumPy, SciPy, or other relevant libraries. The libraries can be used to perform various mathematical operations, such as integration, differentiation, Fourier transforms, Laplace transforms, etc. The libraries can also be used to manipulate the equation to solve for a specific variable or parameter.

3. Visualization: The program should plot the visualizations of the solved equations using Matplotlib or other relevant libraries. The program should provide various types of plots, such as line plots, scatter plots, and 3D plots, depending on the input and operation selected. The program should also provide options to customize the plot, such as axis labels, legend, and color.

4. Output: The program should output the solution to the equation in a clear and concise format. The output can be presented in a graphical format for visualization purposes, or as a numerical result. The program should also provide informative error messages to the user, such as incorrect input format or unsupported mathematical functions.

5. Documentation: The program should include detailed documentation on how to use the solver and visualizer, including examples of how to input equations and use various mathematical functions. The documentation should also include any necessary setup or installation instructions.

6. Testing: The program should undergo extensive testing to ensure accurate and reliable results. It should be tested on a range of equations with varying complexities and conditions to ensure it can handle a wide range of mathematical problems.

7. Optimization: The program can be optimized to improve efficiency by reducing unnecessary computations, using efficient algorithms, or parallel computing. It can also be optimized to handle large datasets or complex equations.

8. Future Enhancements: The program can be enhanced to support more mathematical functions, improve efficiency, and incorporate additional features such as data analysis and optimization.


### 1.4. Scientific Background

The Fourier transform is a powerful mathematical tool used to analyze and represent signals and functions in the frequency domain. It converts a signal from the time domain to the frequency domain by decomposing it into its constituent frequency components. The forward Fourier transform is used to transform a signal from the time domain to the frequency domain, while the inverse Fourier transform is used to transform a signal from the frequency domain back to the time domain.

The forward Fourier transform of a signal can be represented by the equation:

F(k)=F<sub>x</sub> \[f(x)\](k) = ∫<sub>∞</sub><sup>−∞</sup> F(k)e<sup>-2πikx</sup>dk


The inverse Fourier transform can be represented by the equation:

f(x)=F<sub>K</sub><sup>−1</sup> \[F(k)\](x) = ∫<sub>∞</sub><sup>−∞</sup> F(k)e<sup>2πikx</sup>dk

In addition to the standard Fourier transform, there are also the cosine Fourier transform and the sine Fourier transform, which are used to analyze signals that have even or odd symmetry, respectively. 

The Fourier transform for cosines of a real function is defined as the real part of a full complex Fourier transform.

F<sub>x</sub><sup>(c)</sup>\[f(x)\](k) = ∫<sub>∞</sub><sup>−∞</sup> cos (2πkx) f(x)dx

The Fourier sine transform is defined as the imaginary part of full complex Fourier transform, and it is given by:

F<sub>x</sub><sup>(s)</sup>\[f(x)\](k) = ∫<sub>∞</sub><sup>−∞</sup> sin (2πkx) f(x)dx

Python provides several libraries such as NumPy and SciPy which offer various functions for Fourier transforms and their inverse. In order to visualize these transforms, the Matplotlib library can be used to plot the frequency spectrum of the signal in the frequency domain.

The scientific background of Fourier transforms and their variations is crucial to understanding their use and implementation in a Python program. The program should be able to accurately calculate and visualize the forward Fourier transform, inverse Fourier transform, cosine Fourier transform, and sine Fourier transform of a given signal, with proper error handling and output formatting.

## 2. Technological Stack

Below is an overview of the technological stack that will be used:

1. Programming Language: Python
2. Libraries: Matplotlib, NumPy, Pandas, and SciPy
3. Testing Framework: pytest
4. Version Control: Github

## 3. UML Diagram

The UML diagram provides a class diagram, which is a type of structural diagram that shows the classes, their attributes, operations, and the relationships between them.

The diagram consists of several classes, represented by rectangles with the class name written inside. The classes are connected by various types of relationships, represented by lines with arrowheads. 

In the given UML diagram, there are two abstract base classes: FourierTransform and PlotCurve.

FourierTransform is an abstract base class that contains a private abstract method called transform(). This class is inherited by four concrete classes that implement different types of Fourier transforms:- 
- ForwardFourierTransform
- InverseFourierTransform
- CosineFourierTransform
- SineFourierTransform. 

These classes override the transform() method to provide their respective implementations.

PlotCurve is also an abstract base class that defines the interface for plotting different types of curves. This class has two abstract methods: plot() and show(). This class is inherited by two concrete classes:-

- LineGraph
- ScatterGraph

which implement these methods according to their specific requirements. The LineGraph class plots data points with a line, while the ScatterGraph class plots data points with individual markers.

Both of these abstract base classes define the interfaces for their respective functionalities and provide a common structure for their concrete implementations. The concrete classes that inherit these abstract base classes must implement the methods defined in the abstract base class, ensuring adherence to the interface and providing flexibility in the implementation of specific functionalities.

The factory pattern is a design pattern that allows the creation of objects without specifying the exact class of object that will be created. In Python, the factory pattern can be implemented using factory functions or classes that return instances of different classes based on input parameters. 

The FourierTransformFactory is responsible for creating different types of Fourier transforms, which are implemented as subclasses of the FourierTransform abstract base class. This factory method has a create_transform method which takes a parameter that specifies the type of transform to create, and returns an instance of the appropriate subclass.

Similarly, the PlotCurveFactory is responsible for creating different types of plot curves, which are implemented as subclasses of the PlotCurve abstract base class. This factory method has a create_graph method which takes a parameter that specifies the type of plot curve to create, and returns an instance of the appropriate subclass.

 UML Diagram: 
![UML Diagram](https://github.com/ishwantsingh/Vizda-Data-Visualization/blob/updateDocument/assets/vizdaUml.png?raw=true)


## 4. Timeline

27 April | Understand Mathematical Equations

1 May | Implement functions to compute output

5 May | Plot visualization graphs

8 May | Perform unit and system tests

12 May | Create documentation using Sphinx and finalize the project.

## 5. Project Extensions

1. Deploy the code for easier access on any device.
2. Implement more scientific algorithms and graphical representations for wider applications.

