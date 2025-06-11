# Ridge-Regression
Here’s a polished README file draft for your **Algerian Forest Fire Prediction** project, following best practices for GitHub documentation:

---

# Algerian Forest Fire Prediction Project

This project uses the **Algerian Forest Fire dataset** to predict the **Fire Weather Index (FWI)**, a key measure of forest fire risk, using various regression models. The project includes Exploratory Data Analysis (EDA), feature engineering, model selection, hyperparameter tuning, and deployment as a Streamlit web application.

---

## Dataset

The dataset contains weather and fire-related attributes recorded between June and September 2012 in Algeria.

**Attribute Information:**

| Feature | Description                      | Range                  |
| ------- | -------------------------------- | ---------------------- |
| Date    | Date of observation (DD/MM/YYYY) | June to September 2012 |
| Temp    | Temperature at noon (°C)         | 22 to 42               |
| RH      | Relative Humidity (%)            | 21 to 90               |
| Ws      | Wind Speed (km/h)                | 6 to 29                |
| Rain    | Total Rainfall (mm)              | 0 to 16.8              |
| FFMC    | Fine Fuel Moisture Code          | 28.6 to 92.5           |
| DMC     | Duff Moisture Code               | 1.1 to 65.9            |
| DC      | Drought Code                     | 7 to 220.4             |
| ISI     | Initial Spread Index             | 0 to 18.5              |
| BUI     | Buildup Index                    | 1.1 to 68              |
| FWI     | Fire Weather Index               | 0 to 31.1              |
| Classes | Fire or Not Fire                 | Binary                 |

**Dependent Variable:**

* **FWI (Fire Weather Index)**

**Independent Variables:**

* Temp, RH, Ws, Rain, FFMC, DMC, DC, ISI, Classes, Region

---

## Project Workflow

1. **Data Preprocessing & Cleaning**

   * Handled missing values and outliers.
   * Conducted Exploratory Data Analysis (EDA) using visualizations.
   * Feature Engineering: Combined relevant features and ensured correct data types.

2. **Model Training & Evaluation**

   * Implemented multiple regression models:

     * Linear Regression
     * Ridge Regression
     * Lasso Regression
     * ElasticNet Regression
   * Performed hyperparameter tuning to identify the best model.
   * Ridge Regression achieved the highest accuracy and was selected as the final model.

3. **Deployment**

   * Developed a **Streamlit** web application to deploy the model and allow users to input data and get predictions interactively.

---

## How to Run the Project

1. Clone the repository:
   git clone <repository_url>
   cd <repository_folder>

2. Install dependencies:
   pip install -r requirements.txt

3. Run the Streamlit app:
   streamlit run app.py

4. Open your browser and go to the provided local URL (usually [http://localhost:8501](http://localhost:8501)).

---

## Results

* **Best Model:** Ridge Regression
* **Reason:** Ridge Regression outperformed other models after hyperparameter tuning, achieving the highest accuracy.

---

## Technologies Used

* Python
* Pandas, NumPy (data manipulation)
* Matplotlib, Seaborn (EDA and visualization)
* Scikit-learn (modeling and hyperparameter tuning)
* Streamlit (web application deployment)

---
