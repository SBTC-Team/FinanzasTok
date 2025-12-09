"""
Guía completa para usar el FRED API
Federal Reserve Economic Data API
"""

from fredapi import Fred
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# 1. CONFIGURACIÓN INICIAL
# ============================================

# Reemplaza 'TU_API_KEY' con tu clave real de FRED
API_KEY = 'TU_API_KEY_AQUI'
fred = Fred(api_key=API_KEY)

# ============================================
# 2. OBTENER UNA SERIE DE DATOS
# ============================================

# Ejemplo: Obtener datos del PIB de Estados Unidos
# Series populares:
# - 'GDP': PIB de EE.UU.
# - 'UNRATE': Tasa de desempleo
# - 'CPIAUCSL': Índice de Precios al Consumidor
# - 'DGS10': Rendimiento del Tesoro a 10 años
# - 'DEXUSEU': Tipo de cambio USD/EUR

def obtener_serie_simple():
    """Ejemplo básico: obtener datos del PIB"""
    gdp = fred.get_series('GDP')
    print("PIB de Estados Unidos:")
    print(gdp.tail())  # Últimos 5 valores
    return gdp

# ============================================
# 3. OBTENER DATOS CON FECHAS ESPECÍFICAS
# ============================================

def obtener_serie_con_fechas():
    """Obtener datos entre fechas específicas"""
    unemployment = fred.get_series(
        'UNRATE',  # Tasa de desempleo
        observation_start='2020-01-01',
        observation_end='2023-12-31'
    )
    print("\nTasa de desempleo (2020-2023):")
    print(unemployment.head())
    return unemployment

# ============================================
# 4. BUSCAR SERIES
# ============================================

def buscar_series(termino_busqueda):
    """Buscar series económicas por término"""
    resultados = fred.search(termino_busqueda)
    print(f"\nResultados de búsqueda para '{termino_busqueda}':")
    print(resultados[['id', 'title', 'frequency']].head(10))
    return resultados

# ============================================
# 5. OBTENER INFORMACIÓN DE UNA SERIE
# ============================================

def obtener_info_serie(serie_id):
    """Obtener metadatos de una serie"""
    info = fred.get_series_info(serie_id)
    print(f"\nInformación de la serie {serie_id}:")
    print(f"Título: {info['title']}")
    print(f"Unidades: {info['units']}")
    print(f"Frecuencia: {info['frequency']}")
    print(f"Última actualización: {info['last_updated']}")
    return info

# ============================================
# 6. OBTENER MÚLTIPLES SERIES
# ============================================

def comparar_series():
    """Obtener y comparar múltiples series"""
    # Obtener varias series económicas
    gdp = fred.get_series('GDP', observation_start='2010-01-01')
    unemployment = fred.get_series('UNRATE', observation_start='2010-01-01')
    inflation = fred.get_series('CPIAUCSL', observation_start='2010-01-01')
    
    # Crear un DataFrame combinado
    df = pd.DataFrame({
        'PIB': gdp,
        'Desempleo': unemployment,
        'IPC': inflation
    })
    
    print("\nDatos combinados:")
    print(df.tail())
    return df

# ============================================
# 7. VISUALIZAR DATOS
# ============================================

def graficar_serie(serie_id, titulo):
    """Crear gráfico de una serie temporal"""
    datos = fred.get_series(serie_id, observation_start='2010-01-01')
    
    plt.figure(figsize=(12, 6))
    plt.plot(datos.index, datos.values, linewidth=2)
    plt.title(titulo, fontsize=14, fontweight='bold')
    plt.xlabel('Fecha', fontsize=12)
    plt.ylabel('Valor', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

# ============================================
# 8. ANÁLISIS AVANZADO
# ============================================

def analisis_estadistico(serie_id):
    """Realizar análisis estadístico básico"""
    datos = fred.get_series(serie_id)
    
    print(f"\nAnálisis estadístico de {serie_id}:")
    print(f"Media: {datos.mean():.2f}")
    print(f"Mediana: {datos.median():.2f}")
    print(f"Desviación estándar: {datos.std():.2f}")
    print(f"Mínimo: {datos.min():.2f}")
    print(f"Máximo: {datos.max():.2f}")
    
    return datos.describe()

# ============================================
# 9. CALCULAR CAMBIOS PORCENTUALES
# ============================================

def calcular_cambios(serie_id):
    """Calcular cambios porcentuales"""
    datos = fred.get_series(serie_id, observation_start='2020-01-01')
    
    # Cambio porcentual mensual
    cambio_mensual = datos.pct_change() * 100
    
    # Cambio porcentual anual
    cambio_anual = datos.pct_change(periods=12) * 100
    
    print(f"\nCambios porcentuales de {serie_id}:")
    print("Últimos cambios mensuales:")
    print(cambio_mensual.tail())
    
    return cambio_mensual, cambio_anual

# ============================================
# 10. EJEMPLO COMPLETO: ANÁLISIS DE INFLACIÓN
# ============================================

def analisis_inflacion():
    """Análisis completo de la inflación en EE.UU."""
    print("\n" + "="*50)
    print("ANÁLISIS DE INFLACIÓN EN ESTADOS UNIDOS")
    print("="*50)
    
    # Obtener datos del IPC
    cpi = fred.get_series('CPIAUCSL', observation_start='2020-01-01')
    
    # Calcular inflación anual
    inflacion = cpi.pct_change(periods=12) * 100
    
    print("\nInflación anual (últimos 12 meses):")
    print(inflacion.tail())
    
    # Graficar
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(cpi.index, cpi.values, linewidth=2, color='blue')
    plt.title('Índice de Precios al Consumidor', fontweight='bold')
    plt.xlabel('Fecha')
    plt.ylabel('IPC')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.plot(inflacion.index, inflacion.values, linewidth=2, color='red')
    plt.title('Tasa de Inflación Anual (%)', fontweight='bold')
    plt.xlabel('Fecha')
    plt.ylabel('Inflación (%)')
    plt.axhline(y=2, color='green', linestyle='--', label='Meta Fed (2%)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return cpi, inflacion

# ============================================
# MAIN - EJEMPLOS DE USO
# ============================================

if __name__ == "__main__":
    print("GUÍA DE USO DEL FRED API")
    print("="*50)
    
    # Descomentar las funciones que quieras ejecutar:
    
    # 1. Obtener serie simple
    # gdp = obtener_serie_simple()
    
    # 2. Obtener serie con fechas
    # unemployment = obtener_serie_con_fechas()
    
    # 3. Buscar series
    # resultados = buscar_series('inflation')
    
    # 4. Obtener información de una serie
    # info = obtener_info_serie('GDP')
    
    # 5. Comparar múltiples series
    # df = comparar_series()
    
    # 6. Graficar una serie
    # graficar_serie('UNRATE', 'Tasa de Desempleo en EE.UU.')
    
    # 7. Análisis estadístico
    # stats = analisis_estadistico('GDP')
    
    # 8. Calcular cambios porcentuales
    # cambios = calcular_cambios('CPIAUCSL')
    
    # 9. Análisis completo de inflación
    # analisis_inflacion()
    
    print("\n¡Recuerda reemplazar 'TU_API_KEY_AQUI' con tu clave real!")
    print("Obtén tu API key en: https://fred.stlouisfed.org/docs/api/api_key.html")


# ============================================
# SERIES ECONÓMICAS POPULARES
# ============================================
"""
SERIES MÁS UTILIZADAS:

ECONOMÍA GENERAL:
- GDP: PIB de EE.UU.
- GDPC1: PIB Real
- UNRATE: Tasa de desempleo
- PAYEMS: Nóminas no agrícolas

INFLACIÓN Y PRECIOS:
- CPIAUCSL: Índice de Precios al Consumidor
- CPILFESL: IPC sin alimentos y energía
- PCEPI: Índice de Precios PCE
- PCEPILFE: PCE sin alimentos y energía

TASAS DE INTERÉS:
- DGS10: Rendimiento del Tesoro a 10 años
- DGS2: Rendimiento del Tesoro a 2 años
- FEDFUNDS: Tasa de fondos federales
- MORTGAGE30US: Tasa hipotecaria a 30 años

MERCADO LABORAL:
- UNRATE: Tasa de desempleo
- CIVPART: Tasa de participación laboral
- EMRATIO: Ratio empleo-población
- ICSA: Solicitudes iniciales de desempleo

DIVISAS:
- DEXUSEU: USD/EUR
- DEXJPUS: JPY/USD
- DEXCHUS: CNY/USD

MERCADOS:
- SP500: Índice S&P 500
- VIXCLS: Índice de volatilidad VIX
- DCOILWTICO: Precio del petróleo WTI

VIVIENDA:
- CSUSHPISA: Índice Case-Shiller
- HOUST: Inicios de construcción
- MORTGAGE30US: Tasa hipotecaria

CONSUMO:
- PCE: Gasto de consumo personal
- RSXFS: Ventas minoristas
- UMCSENT: Confianza del consumidor
"""