# SCOPE: A Chemically-Aware Workflow-Automation Software for Molecules and Molecular Crystals

  This repository contains the tutorials associated with SCOPE, a Python package designed to orchestrate computational chemistry workflows. SCOPE prepares, submits, and analyses quantum chemistry computations of individual molecules or molecule-based crystals, and organizes the results to simplify analysis.  
  
  SCOPE has four core pillars.
  1) Chemical Species:        Dedicated to encode the chemistry of the systems of interest. It can be expanded through add-ons
  2) Computational Workflow:  Dedicated to define dynamic computational workflows.
  3) States:                  Dedicated to the analysis of results
  4) Environment:             Dedicated to file management and job execution in HPC clusters.

---

# Documentation

  - The associated manuscript is under preparation. Preprint available [here](https://doi.org/10.26434/chemrxiv.15001415/v1)
  - Source code is available [here](https://github.com/QTC-IQAC/Scope)

---

# Installation

Python 3.12 is a strict requirement for these tutorials and the associated SCOPE packages.

This repository requires the installation of SCOPE and its add-ons. Once installed, then clone this repository to access the tutorial notebooks and data.

  ## 1-Environment setup

  ```bash
  # create and activate a Python 3.12 environment
  conda create --name scope python=3.12
  conda activate scope
  conda install pip
  ```

  ## 2-Install all SCOPE packages

  Follow the installation instructions of SCOPE, and install all add-ons:

  - [scope-qc](https://pypi.org/project/scope-qc/)

  ## 3-Install notebook tools

  ```bash
  pip install jupyter ipykernel nbformat matplotlib plotly
  ```

  ## 4-Download the tutorials

  ```bash
  git clone https://github.com/QTC-IQAC/Scope_Tutorials.git
  cd Scope_Tutorials
  ```

  Then open any notebook from the `tutorials/` directory and explore the accompanying files in `Data/`.

---

# Content

  - Data folder with material discussed along the tutorials
  - Tutorials, as python Notebooks

These are the topics covered in each tutorial:
1) The **System** class and its sources: the **Specie**, **Cell** and **Atom** classes  
2) The Computational workflow: **Branch**, **Workflow**, **Job**, and **Computation** classes  
3) The **State** class  
4) The **Data**, **Collection** and **VNM** classes
5) The **Input_data** class, and **scope input files**
6) Running <span style="color:blue">**SCOPE**</span> - Part 1: File Structure
7) Running <span style="color:blue">**SCOPE**</span> - Part 2: Execution 
8) Running <span style="color:blue">**SCOPE**</span> - Part 3: Detailed Actions
9) The Azo add-on: Subclasses, Analysis and Creation of Azo Systems

---

# License

This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International license (`CC BY-NC-ND 4.0`). See the [LICENSE](LICENSE) file for the full text.

---

# Acknowledgements
  - The Spanish Ministerio de Ciencia, Innovación y Universidades for funding (Project PID2022-138265NA-I00)
  - The EuroHPC Development Access Call (Project: EHPC-DEV-2024D11-031)
  - The Centre de Supercomputació de Catalunya (CSUC) for Computational Resources

<p align="center">
  <img src="images/mciu_logo.png" alt="Logo" width="400">
</p>
