"""
Plantilla mínima para un análisis de Diferencias en Diferencias (Python)

Dependencias recomendadas: pandas, statsmodels

Reemplace los bloques `TODO` con su código y rutas de datos.
"""
import pandas as pd
import statsmodels.formula.api as smf

def load_data(path):
    # TODO: cargar datos
    return pd.read_csv(path)

def run_did(df, outcome, treatment, time_var, group_var):
    # Ejemplo simplificado usando una especificación por diferencias
    formula = f"{outcome} ~ {treatment} * {time_var} + C({group_var})"
    model = smf.ols(formula=formula, data=df).fit(cov_type='cluster', cov_kwds={'groups': df[group_var]})
    return model

if __name__ == '__main__':
    print('Ejecute desde un notebook o pasando rutas de datos desde la línea de comandos')
