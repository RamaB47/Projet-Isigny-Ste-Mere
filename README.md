# Milk & Carbon: Scope 3 Analysis of the Isigny Sainte-Mère Cooperative 🌾📊

This personal portfolio project presents an analysis of the 2025 Extra-Financial Performance Declaration (DPEF) of the Isigny Sainte-Mère dairy cooperative[cite: 1]. The objective is to align the cooperative's operational and logistical performance with its carbon reduction goals, focusing specifically on **upstream Scope 3 emissions** (agricultural impact)[cite: 1].

---

## 📈 Supply Chain & ESG Challenges
* **The Collection Deficit:** Every year from May to November, the cooperative's milk collection undergoes a recurring and significant drop[cite: 1].
* **The Climate Factor:** Data analysis reveals early and persistent heat stress on Normandy pastures starting as early as May[cite: 1].
* **The Business Impact:** This prolonged volume deficit disrupts industrial consistency and directly impacts the profitability of production lines from spring through late autumn[cite: 1].
* **The Carbon Challenge:** Upstream agriculture accounts for the vast majority of a dairy cooperative's Scope 3 footprint, making it a critical area of focus for major retail customers (GMS)[cite: 1].

---

## 🛠️ Methodology & Data Approach

To address this challenge, the project outlines a strategic roadmap structured in three phases:

### 1. Short-Term: 48-Hour Flow Planning (Completed)
* **Time Series Modeling:** Utilized the **Prophet** library (Python) to isolate the annual seasonality of milk collection and anticipate volume drops[cite: 1].
* **Predictive Transition (Target):** Formulated recommendations to transition toward a supervised machine learning model (**XGBoost**) as soon as daily-granularity data pipelines are fully consolidated[cite: 1].
* **Supply Chain Impact:** Optimizing transport costs, eliminating empty runs, and enhancing operational responsiveness to volume fluctuations[cite: 1].

### 2. Medium-Term: Mitigating Heat Stress
* **Concrete Action:** Installing solar panels on agricultural buildings to power ventilation and misting (misting/brumisation) systems in cow barns[cite: 1].
* **Supply & ESG Impact:** Safeguarding animal welfare during temperature peaks, maintaining milk yields, and producing local renewable energy with measurable impacts from year one[cite: 1].

### 3. Long-Term: Circular Economy & Energy Recovery
* **Concrete Action:** Setting up local collective methanization partnerships to process agricultural waste and effluents into renewable energy[cite: 1].
* **Supply & ESG Impact:** Driving deep and durable decarbonization of upstream Scope 3 emissions, securing a local biogas supply for the cooperative's transport fleet or industrial sites, and creating new revenue streams for partner farmers[cite: 1].

---

## 📂 Repository Structure & Tech Stack
* **`notebooks/`**: Data preprocessing and predictive modeling scripts using Python (Pandas, Prophet)[cite: 1].
* **`dashboards/`**: Interactive visualizations and reporting (built using Amazon QuickSight / Power BI)[cite: 1].
* **`documents/`**: Publicly sourced reports and reference materials (Isigny Sainte-Mère 2025 DPEF, industry benchmarks)[cite: 1].

---

## 📋 Data Sources
This study relies exclusively on publicly available data and reports:
* 2025 Extra-Financial Performance Declaration (DPEF) of Isigny Sainte-Mère[cite: 1].
* Historical dairy collection and seasonality data[cite: 1].
* ADEME emission factors and methodology guides for carbon modeling.
* **Email:** rama.badji47@yahoo.com 
