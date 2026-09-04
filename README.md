# FA26-summer-school

This EAA summer school introduces participants to interpretable machine learning methods with applications in acoustics. The course highlights the importance of incorporating prior physical knowledge and consistency in data-driven acoustic modelling. The program begins with essential big-picture overview and key concepts in optimization that commonly appear in machine learning workflows. Participants then explore techniques for analysing complex acoustic data using dimensionality reduction methods such as principal component analysis (PCA) and dynamic mode decomposition (DMD), including their physically informed variants. Probabilistic modelling with Gaussian processes is presented as a tool for surrogate modelling and uncertainty quantification in vibroacoustic predictions. The course further introduces data-driven discovery of governing equations using sparse regression and symbolic regression, demonstrating how interpretable mathematical models of acoustic systems can be derived from data. Finally, an overview of physics-informed deep learning in acoustics is given, including physics-informed neural networks and autoencoders, showing how physical laws can be embedded into learning models.


## Repository Structure
```text
FA26-summer-school/
├── README.md
├── requirements.txt
├── 01_Introduction/
│   └── intro.ipynb
├── 02_Basics_of_Optimization/
│   ├── optimization_partA.ipynb
│   ├── optimization_partB.ipynb
│   ├── optimization_partC.ipynb
│   └── optimization_utils.py
├── 03_Dimensionality_Reduction/
│   ├── 
│   └── 
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

## How to run the codes

Scripts for hands-on coding exercises are provided on the course GitHub. Therefore, please ensure you have a working GitHub before arriving. Advantage of this option is that you don't need to download any code and any libraries.

For those used to coding in Python and dealing with library dependencies: you can download the git repo and execute the scripts on your laptop, but we unfortunately won't have enough time to help with each individual laptop setup. We provide an environment with list of necessary libraries, so you can setup this even before arriving to Graz.

### How to run via GitHub Codespaces

You can launch a full, preconfigured VS Code instance in your browser:

1. Click the green **`<> Code`** button at the top of this repository.
2. Select the **Codespaces** tab.
3. Click **Create codespace on main**.
4. Once the VS Code web interface loads, open a new integrated terminal. Wait until the libraries install themselves.
5. After the installations are finished, open the Jupyter Notebook in folder `01_Introduction`. In the upper rigth corner, click Select Kernel -> Python Environments... -> select Python 3.12 (the default recommended environment).


### How to run locally

If running codes locally, clone the repo:
```bash
git clone https://github.com/Acustica-Pragensis/FA26-summer-school.git
cd FA26-summer-school
```
and create an environment either with venv:
```bash
python -m venv fa26-summer-school
source fa26-summer-school/bin/activate  # On Windows: fa26-summer-school\Scripts\activate
pip install -r requirements.txt
python -c "import pysr; pysr.install()"
```
or with Conda:
```bash
conda create -n fa26-summer-school python=3.12 -y
conda activate fa26-summer-school
pip install -r requirements.txt
python -c "import pysr; pysr.install()"
```

Then, try to run the Jupyter notebook in folder `01_Introduction` to see, that everything works properly.





## Recommended Literature
* [Brunton, Steven L., and J. Nathan Kutz. Data-Driven Science and Engineering: Machine Learning, Dynamical Systems, and Control. Cambridge: Cambridge University Press, 2019. ](https://databookuw.com/databookV2.pdf)
* [Brunton, Steven L. Optimization: A Bootcamp for Machine Learning, Inverse Problems, and Control. Cambridge: Cambridge University Press, 2026. ](https://faculty.washington.edu/sbrunton/OptimizationBootcamp.pdf)
