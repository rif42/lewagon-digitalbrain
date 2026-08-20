---
type: notion-import
notion-id: 144fa0a1933e483fabd5b30fd7303256
source-url: https://app.notion.com/p/lewagon/Teacher-Selection-Data-144fa0a1933e483fabd5b30fd7303256
imported: 2026-07-23
---
# Teacher Selection (Data)
> [!note] 
> This document explains how to select teachers for a Data Science bootcamp. Please reach out to @Kevin Robert for validating your new teachers before onboarding them on Kitt. He will plan a background check (+ interview?) with them and one member of the Data core engineering team.
# How to
How to turn a contact into a DS lecturer? Follow this steps:
- Background interview: Freelance? Tech employee? PhD? Analyst? Data Scientist? Engineer? Developer? Teaching experience? 👉 Understand the qualification level in the different modules
- Product/culture interview: Startup? Big data company? Research? Consultant? 👉 Understand how the DS is used and felt
- Pedagogical interview:
        - For a given module, ask explanations about fundamentals ([see below](https://www.notion.so/lewagon/Selection-144fa0a1933e483fabd5b30fd7303256#302b00b4d5f44feca82df644930d05c0))
        - Teaching demo: lecture preparation ([see below](https://www.notion.so/lewagon/Selection-144fa0a1933e483fabd5b30fd7303256#afd4e999426d42a4b28f3575a8c10432)) and live test
# Pedagogical interview resources
## Technical questions
### Data Science toolkit (Weeks 1-2)
- [Setup](https://github.com/lewagon/data-setup): it's easier than the Web bootcamp. You want teachers with some Windows/Linux/macOS experience in the crew and some strong troubleshooting skills.
- Python:
        - CRUD on dict (Hash in Ruby)
        - Can you explain list comprehension in your own words?
- SQL: Advanced requests (WITH clause, Window functions)
- NumPy/Pandas
        - "What's the difference between a Ndarray, a Series and a DataFrame"?
        - "How would you count the number of unique elements in a column of a DataFrame?"
- Matplotlib/Seaborn/Plotly
        - **"What's your favorite plotting library? Why?"**
- Python OOP/packaging
        - What notebooks are made for?
        - "What is a "package" vs. a "module"?
        - **"When you work or collaborate on a project, what's your best practice for making sure all your packages are always available for imports?"**
> [!note] 
> For this first days, no need to find a ML expert in your network. Look at your Web Dev teachers who might also have experience with Python. They can upskill very fast and be staffed on those days.
### Maths/Decision Science (Weeks 2-3)
Linear Algebra
Statistics
- Have you used the libraries "Scipy" and "Statsmodels" ?
- Define an A/B test and how would you measure if it is a success or not?
- Give an example of the application of the Central Limit Theorem?
**Linear models (inference)**
- "What's the difference between a simple correlation coefficient and a partial regression coefficient?" Let's take an example:
        - Say you model gives: flatpricek$=5∗surfacem2+2∗floor+ϵflatprice_{k\$} = 5 * surface_{m^2} + 2 * floor + \epsilonflatpricek$​=5∗surfacem2​+2∗floor+ϵ
        - "How would you interpret coef the **5** in your own words?
- "What's the p-value of a regression coefficient? "
        - "Say your model gives you a "p-value" of 0.23 associated with the coef 5. What would it mean?"
- "What's the r-squared of a linear regression? "
        - Answer: Share of the variance of YYY that can be explained by the combined variance of the XiX_iXi​​
> [!note] 
> You want to staff someone with a good Mathematical + Statistical background (at least 3-5 years after High School in studies) + Programming experience and who can make this knowledge accessible to all.
### Machine Learning (Weeks 4-5)
Questions from Math/Decision-Science ☝️ should also be checked for ML weeks. In addition:
Fundamentals:
Unsupervised: clustering (centroids) and dimensional reduction (PCA), recommender systems....
ML advanced: Random Forest, Time series, NLP
> [!note] 
> This is where you need expertise. If possible, staff 1-2 person on those two weeks, not more, so that there is some coherence jumping from one lecture to the other
### Deep Learning (Week 6)
- TensorFlow Keras knowledge?
- Neural network 101: neuron, layer, stack, activation function
- NN applications: CNN è!to images and RNN to time-series
> [!note] 
> This is a good week to staff a Deep Learning expert for 5 days. Look for PhD candidates / graduates, people who are used to explain this complex subject to beginners. We don't need the 10+ year expert in the field, this week is about showing what DL is about (we only have 5 days) and how they could use it during Projects.
### ML Ops (Week 7)
- Python packaging
- GCP knowledge
- MLFlow knowledge
- Training pipelines
- Training scaling
- Test
        - "*Have you written any tests?"*
- Deployment
        - "*What is CI/DD?"*
        - "*What containerization is?" *
> [!note] 
> For that week, you need someone with some DevOps + Data experience and strong programming / OOP skills.
### Projects (Weeks 8-9)
- Project management
- Fullstack ML/DL engineering
- Fullstack ML/DL developer
> [!note] 
> You need *at least one* 4+ years experienced Data Scientist who has worked on different projects in companies. The knowledge and pragmatism acquired during those is very valuable for the students.
## Test lectures
> [!warning] Database view not exported
> https://app.notion.com/p/lewagon/16863067e6fa4af88b2195b97d622420?v=f5bf1866ce6c4dc69d11c6ea10ab86cd&pvs=18
## Related
- [[Candidates]]
- [[Onboarding]]
