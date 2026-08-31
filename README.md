# FA26-summer-school
Hands-on tutorials for the EAA Summer School on Interpretable Machine Learning in Acoustics.

This EAA summer school introduces participants to interpretable machine learning methods with applications in acoustics. The course highlights the importance of incorporating prior physical knowledge and consistency in data-driven acoustic modelling. The program begins with essential big-picture overview and key concepts in optimization that commonly appear in machine learning workflows. Participants then explore techniques for analysing complex acoustic data using dimensionality reduction methods such as principal component analysis (PCA) and dynamic mode decomposition (DMD), including their physically informed variants. Probabilistic modelling with Gaussian processes is presented as a tool for surrogate modelling and uncertainty quantification in vibroacoustic predictions. The course further introduces data-driven discovery of governing equations using sparse regression and symbolic regression, demonstrating how interpretable mathematical models of acoustic systems can be derived from data. Finally, an overview of physics-informed deep learning in acoustics is given, including physics-informed neural networks and autoencoders, showing how physical laws can be embedded into learning models.


If running codes locally, we recommend creating an environment, e.g. with conda:

```bash
conda env create -f environment.yml
conda activate fa26-summer-school
python -c "import pysr; pysr.install()"
```

The following packages are used during the summer school: `numpy matplotlib pymoo scikit-learn pysr`.
Install e.g. with pip: `pip install numpy matplotlib pymoo scikit-learn pysr`




### Repository Structure
```text
FA26-summer-school/
├── README.md
├── environment.yml
├── 01_Introduction/
│   └── intro.ipynb
├── 02_Basics_of_Optimization/
│   ├── optimization_partA.ipynb
│   ├── optimization_partB.ipynb
│   ├── optimization_partC.ipynb
│   └── optimization_utils.py
├── 03_Dimensionality_Reduction/
│   ├── dimred_steady.ipynb
│   ├── dimred_transient.ipynb
│   ├── dimred_all.txt
│   ├── dimred_steady.txt
│   ├── dimred_transient.txt
│   ├── dimred_utils.py
│   └── propagation.mp4
├── 04_Gaussian_Processes/
│   ├── 
│   └── 
├── 05_Data-driven_Discovery/
│   ├── 
│   └── 
├── 06_Symbolic_Regression/
│   ├── sr_data.csv
│   └── sr.ipynb
├── 07_Deep_Learning/
│   ├── 
│   └── 
```

### Recommended Literature
* [Brunton, Steven L., and J. Nathan Kutz. Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control. Cambridge: Cambridge University Press, 2019. ](https://databookuw.com/databookV2.pdf)
* [Brunton, Steven L. Optimization: A Bootcamp for Machine Learning, Inverse Problems, and Control. Cambridge: Cambridge University Press, 2026. ](https://faculty.washington.edu/sbrunton/OptimizationBootcamp.pdf)
