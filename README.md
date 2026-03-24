# SCOPE: A Chemically-Aware Workflow-Automation Software for Molecules and Molecular Crystals

  This repository contains the tutorials associated with SCOPE, a Python package designed to handle computational chemistry workflows. SCOPE prepares, submits, and analyses Gaussian and Quantum Espresso computations of individual molecules or molecule-based crystals.  
  
  SCOPE has three core functionalities.
  1) Chemical Species:        Dedicated to the definition of chemistry-related classes (e.g. Molecules, Ligands, Atoms, Bonds, Cells) that can be navigated and interacted with.
  2) Computational Workflow:  Dedicated to the orchestration of dynamic computational workflows.
  3) States:                  Dedicated to the analysis of results
  4) Environment:             Dedicated to file management and job execution in HPC clusters.

---

# Documentation

  - The associated manuscript is under preparation. Partial documentation is available at: ???
  - Source code is available [here](https://github.com/QTC-IQAC/Scope)

---

# Installation

  ## Source Code

  This will install the source code of SCOPE, as well as the dependencies associated with the tutorials:

  ```bash
  # create and activate conda environment and install pip
  conda create --name scope 
  conda activate scope
  conda install pip
  
  # clone repository and enter
  git clone https://github.com/QTC-IQAC/Scope_Tutorials.git
  cd Scope_Tutorials
  
  # install with pip 
  pip install . 
  ```

  ## Dependencies

  - [scope](https://github.com/QTC-IQAC/Scope)
  - ipykernel
  - jupyter
  - nbformat
  - matplotlib
  - plotly

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

MIT

---

# Acknowledgements
  - The Spanish Ministerio de Ciencia, Innovación y Universidades for funding (Project PID2022-138265NA-I00)
  - The EuroHPC Development Access Call (Project: EHPC-DEV-2024D11-031)
  - The Centre de Supercomputació de Catalunya (CSUC) for Computational Resources

<p align="center">
  <img src="images/mciu_logo.png" alt="Logo" width="400">
</p>

