<p align="center">
  <img src="mciu_logo.png" alt="Logo" width="400">
</p>

# About SCOPE

  This repository contains the tutorials associated with the SCOPE package, developed by Sergi Vela and collaborators, at the IQAC (CSIC)
  SCOPE is a Python package designed to handle computational chemistry workflows. It prepares, submits, and analyses Gaussian and Quantum Espresso computations of individual molecules or unit cells. 
  
  SCOPE has three main modules.
  1) Chemical Species:        Enables the creation of chemistry-related classes (e.g. Molecules, Ligands, Atoms, Bonds, Cells) that can be navigated and interacted with.
  2) Computational Workflow:  Enables setting any type of computational task that chemical species must go through.
  3) Environment:             Enables the management of files within and between computers, and the submission of jobs to computational clusters. 

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

---

# License

MIT

---

# Acknowledgements
  - Manel Serrano and Raul Santiago (IQAC-CSIC) for their coding contribution, and help at setting the repository
  - The Spanish Ministerio de Ciencia, Innovación y Universidades for funding (Project PID2022-138265NA-I00)
  - The EuroHPC Development Access Call (Project: EHPC-DEV-2024D11-031)
  - The Centre de Supercomputació de Catalunya (CSUC) for Computational Resources. 
