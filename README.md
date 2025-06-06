# Evaluating Partisan Gerrymandering in Illinois Using Markov Chain Monte Carlo Methods

**CS464: AI for Redistricting – Final Project**  
University of San Francisco, Spring 2025  
Authors: Vanessa Le, Benjamin Puhani  
Instructor: Dr. Ellen Veomett  

---

## 📌 Project Overview

This project analyzes potential partisan gerrymandering in Illinois' 2021 congressional redistricting map using **Markov Chain Monte Carlo (MCMC)** methods via the [GerryChain](https://github.com/mggg/GerryChain) Python library.  
By simulating thousands of alternative districting plans under legal and geographic constraints, we compare the enacted map to a distribution of unbiased maps to evaluate fairness.

---

## 🗂️ Contents

- `data/` — Raw and processed shapefiles, demographic data, and election results
- `scripts/` — Python scripts for data cleaning, preprocessing, chain execution, and visualization
- `figures/` — Output plots and charts, including ensemble histograms and marginal box plots
- `final_report.pdf` — Full project write-up with methodology, analysis, and conclusions

---

## 🧪 Methodology

1. **Data Collection & Cleaning**  
   - Demographic data from the 2020 Census (PL 94-171)  
   - Election data from the 2020 Presidential and U.S. Senate races (via VEST)  
   - Repaired spatial inconsistencies using [`maup`](https://github.com/mggg/maup)

2. **Map Generation using MCMC**  
   - Used GerryChain's ReCom proposal to generate 40,000 valid districting plans  
   - Enforced constraints on population balance, compactness (cut edges), and contiguity

3. **Fairness Metrics & Visualization**  
   - Analyzed metrics such as:
     - Number of Democratic seats won
     - Cut edge counts
     - Efficiency gap
     - Marginal box plots (vote distribution per district)  
   - Compared ensemble distributions to Illinois' enacted 2021 plan

---

## 📊 Key Findings

- The enacted map is a statistical outlier in terms of:
  - **Partisan seat advantage** for Democrats
  - **Lower compactness** (higher number of cut edges)
  - **Efficiency gap**, indicating disproportionate vote wasting  
- Marginal box plots suggest intentional **packing and cracking** strategies

---

## 📁 Installation & Usage

### Requirements

- Python 3.8+
- [`GerryChain`](https://gerrychain.readthedocs.io)
- [`GeoPandas`](https://geopandas.org)
- [`maup`](https://github.com/mggg/maup)
- pandas, matplotlib, shapely, tqdm

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/gerrymandering-il-mcmc.git
cd gerrymandering-il-mcmc

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
