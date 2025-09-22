
---

## ✅ Fases Implementadas (CRISP-DM)

### **Fase 1 – Business Understanding**
- Objetivos del proyecto definidos.
- Problema de negocio identificado: **predecir precios de autos usados BMW**.
- Plan de fases documentado.

### **Fase 2 – Data Understanding**
- Exploración de datasets.
- Revisión de valores nulos y duplicados.
- Gráficos de distribución, correlación y tendencias.
- Conclusiones preliminares.

### **Fase 3 – Data Preparation**
- Eliminación de duplicados.
- Tratamiento de valores nulos.
- Creación de nuevas variables (ej. `edad_auto`).
- Codificación de variables categóricas.
- Guardado de datos limpios en `03_primary` y features en `04_feature`.

### **Fase 4 – Modeling**
- Pipeline con **LinearRegression** y `ColumnTransformer`.
- Entrenamiento con variables categóricas y numéricas.
- Modelo guardado en `06_models/linear_regression.pkl`.

### **Fase 5 – Evaluation**
- Métricas: **R²** y **RMSE**.
- Gráfico **Predicción vs Real**.
- Gráfico de **residuos**.
- Conclusiones sobre desempeño del modelo.

### **Fase 6 – Deployment**
- Carga del modelo entrenado.
- Ejemplo de predicción con un auto nuevo.
- Posibilidad de exportar resultados a `07_model_output`.

---


## 🚀 Tecnologías Utilizadas
- [Kedro](https://kedro.org/) – Framework de orquestación de pipelines.  
- [Pandas](https://pandas.pydata.org/) – Manipulación de datos.  
- [Scikit-learn](https://scikit-learn.org/) – Modelado y evaluación.  
- [Matplotlib & Seaborn](https://seaborn.pydata.org/) – Visualización de datos.  
- [Joblib](https://joblib.readthedocs.io/) – Guardado y carga de modelos.  

---

## 📌 Autor
**Franco Ruz**
**Cesar veliz**
**Hector Aguila**
Proyecto académico - Evaluación Parcial Machine Learning
