 <h1 style="text-align: center;">VisDa: The Data Visualisation Tool</h1>
<h3 style="text-align: center;">Sukriti Macker, Sahil Harwani, Ishwant Singh Bhayana, Satya Vamsi</h3>

## 1. Introduction

### 1.1. Motivation

Scientific data visualizations are crucial for comprehending, analyzing, and communicating scientific findings. Data visualizations can help researchers in visualizing equations by providing a way to plot and analyze the relationships between variables and parameters in the equation, making it easier to understand and interpret the data. Also, they can help researchers to identify patterns, trends, and relationships in large and complex datasets more quickly and effectively than with raw data alone, leading to new insights and discoveries. The idea of the project is to build a Python program that solves certain mathematical equations and algorithms and then holds the capacity to visualize scientific data obtained from them as spectrograms, 2D or 3D plots, time series or any other representations. To construct several types of visualizations and add interaction, the application will employ various object-oriented principles such as factory methods, inheritance, abstract base classes, and decorators. The application will also include test code to check that it works properly and fits the criteria. We will then use Spinx to create documentation, which will be deployed along with the program.

### 1.2. Project Outline

To construct a program that computes and visualizes scientific data, the project will employ object-oriented programming techniques. The abstract base class for all visualizations will be defined as the base Visualization class. Specific classes will be generated using factory methods and will inherit from the base Visualization class to create distinct visualizations. 

Provided below is the project outline:

1. Understand the theory of the Mathematical equations and implement them using python.
2. Compute the specified Mathematical Equation based on the input provided using a YAML file.
3. Write code to store the output in a meaningful manner to be later retrieved for visualization.
4. Implemnt appropriate visualization/graphs for the computed equations.
5. Create GUI for the program
6. Write code to generate documentation using Spinx

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

F(w) = ∫f(t) e^(-jwt) dt

where F(w) is the Fourier transform of f(t), j is the imaginary unit, w is the angular frequency, and f(t) is the signal in the time domain.

The inverse Fourier transform can be represented by the equation:

f(t) = (1/2π) ∫F(w) e^(jwt) dw

where f(t) is the signal in the time domain, F(w) is the Fourier transform of f(t), and j is the imaginary unit.

In addition to the standard Fourier transform, there are also the cosine Fourier transform and the sine Fourier transform, which are used to analyze signals that have even or odd symmetry, respectively. The cosine Fourier transform can be represented by the equation:

Fc(w) = ∫f(t) cos(wt) dt

where Fc(w) is the cosine Fourier transform of f(t), and f(t) is the signal in the time domain.

The sine Fourier transform can be represented by the equation:

Fs(w) = ∫f(t) sin(wt) dt

where Fs(w) is the sine Fourier transform of f(t), and f(t) is the signal in the time domain.

Python provides several libraries such as NumPy and SciPy which offer various functions for Fourier transforms and their inverse. In order to visualize these transforms, the Matplotlib library can be used to plot the frequency spectrum of the signal in the frequency domain.

The scientific background of Fourier transforms and their variations is crucial to understanding their use and implementation in a Python program. The program should be able to accurately calculate and visualize the forward Fourier transform, inverse Fourier transform, cosine Fourier transform, and sine Fourier transform of a given signal, with proper error handling and output formatting.

## 2. Technological Stack

Below is an overview of the technological stack that will be used:

1. Programming Language: Python
2. Libraries: Matplotlib, NumPy, Pandas, and SciPy
3. Testing Framework: pytest
4. Version Control: Github

## 3. UML Diagram and Code Structure Proposal

UML Diagram: 
![alt text][UML Diagram]

[UML Diagram]: https://github.com/ishwantsingh/Vizda-Data-Visualization/tree/updateDocument/assets/vizdaUml.png "UML Diagram"

## 4. Timeline

27 April | Understand Mathematical Equations
1 May | Transfer main computational functions
5 May | Alpha Version complete
8 May | Improve GUI and test accuracy
12 May | Project Complete

## 5. Project Extensions

1. Deploy the code for easier access on any device.
2. Implemnt more scientific algorithms and graphical representations for wider applications.

