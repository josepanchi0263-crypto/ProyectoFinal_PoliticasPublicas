"""
Flujo de análisis para Propensity Score Matching (PSM) del Bono de Desarrollo Humano en Ecuador.

Dependencias recomendadas: pandas, numpy, matplotlib, seaborn, statsmodels, sklearn
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.metrics import pairwise_distances_argmin_min


def load_data(path):
    """Carga datos en formato CSV desde la ruta especificada."""
    return pd.read_csv(path)


def estimate_propensity_score(df, treatment_var, covariates):
    """Estimación del puntaje de propensión con un modelo logit."""
    X = df[covariates].copy()
    X = sm.add_constant(X)
    y = df[treatment_var]
    logit_model = sm.Logit(y, X).fit(disp=False)
    df['propensity_score'] = logit_model.predict(X)
    return logit_model, df


def common_support(df, treatment_var, score_var='propensity_score'):
    """Identifica el soporte común entre tratados y controles."""
    treated = df.loc[df[treatment_var] == 1, score_var]
    control = df.loc[df[treatment_var] == 0, score_var]
    lower = max(treated.min(), control.min())
    upper = min(treated.max(), control.max())
    df_cs = df[(df[score_var] >= lower) & (df[score_var] <= upper)].copy()
    return df_cs, lower, upper


def plot_propensity_density(df, treatment_var, score_var='propensity_score', title=None):
    """Grafica las densidades de puntajes de propensión para tratados y controles."""
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df.loc[df[treatment_var] == 1, score_var], label='Tratados', fill=True)
    sns.kdeplot(df.loc[df[treatment_var] == 0, score_var], label='Controles', fill=True)
    plt.title(title or 'Densidad del puntaje de propensión por grupo')
    plt.xlabel('Propensity Score')
    plt.ylabel('Densidad')
    plt.legend()
    plt.tight_layout()
    return plt.gcf()


def nearest_neighbor_matching(df, treatment_var, score_var='propensity_score', caliper=None):
    """Emparejamiento por vecino más cercano sobre el puntaje de propensión."""
    treated = df[df[treatment_var] == 1].copy()
    control = df[df[treatment_var] == 0].copy()
    treated_scores = treated[[score_var]].to_numpy()
    control_scores = control[[score_var]].to_numpy()
    idx_matches, distances = pairwise_distances_argmin_min(treated_scores, control_scores)
    matched = control.iloc[idx_matches].copy()
    matched.index = treated.index
    matched['match_distance'] = distances
    if caliper is not None:
        matched = matched[matched['match_distance'] <= caliper].copy()
        treated = treated.loc[matched.index].copy()
    matched_df = treated.copy()
    for col in matched.columns:
        matched_df[f'control_{col}'] = matched[col].values
    return matched_df


def compute_att(matched_df, outcome_var, treatment_var='tratamiento_bd_h'):
    """Calcula el ATT a partir del conjunto emparejado."""
    treated_outcome = matched_df.loc[matched_df[treatment_var] == 1, outcome_var]
    control_outcome = matched_df.loc[matched_df[treatment_var] == 1, f'control_{outcome_var}']
    att = (treated_outcome - control_outcome).mean()
    return att


def balance_table(df, covariates, treatment_var='tratamiento_bd_h'):
    """Genera una tabla de balance de covariables antes/después del emparejamiento."""
    treated = df[df[treatment_var] == 1]
    control = df[df[treatment_var] == 0]
    balance = []
    for cov in covariates:
        mean_t = treated[cov].mean()
        mean_c = control[cov].mean()
        pooled_sd = np.sqrt((treated[cov].var(ddof=1) + control[cov].var(ddof=1)) / 2)
        std_diff = (mean_t - mean_c) / pooled_sd if pooled_sd > 0 else np.nan
        balance.append({
            'covariable': cov,
            'mean_tratados': mean_t,
            'mean_controles': mean_c,
            'std_diff': std_diff
        })
    return pd.DataFrame(balance)


def run_psm_workflow(data_path, treatment_var, outcome_var, covariates, caliper=None):
    """Ejecuta el flujo completo de PSM y retorna diagnósticos."""
    df = load_data(data_path)
    logit_model, df = estimate_propensity_score(df, treatment_var, covariates)
    df_cs, lower, upper = common_support(df, treatment_var)
    density_plot = plot_propensity_density(df_cs, treatment_var)
    df_matched = nearest_neighbor_matching(df_cs, treatment_var, caliper=caliper)
    att = compute_att(df_matched, outcome_var, treatment_var=treatment_var)
    balance_before = balance_table(df, covariates, treatment_var=treatment_var)
    balance_after = balance_table(df_matched, covariates, treatment_var=treatment_var)
    return {
        'logit_model': logit_model,
        'df_common_support': df_cs,
        'common_support_bounds': (lower, upper),
        'density_plot': density_plot,
        'matched_data': df_matched,
        'att': att,
        'balance_before': balance_before,
        'balance_after': balance_after
    }

if __name__ == '__main__':
    print('Este módulo contiene funciones para ejecutar un flujo de Propensity Score Matching (PSM).')
