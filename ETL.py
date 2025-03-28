import pandas as pd

# 1) Funcion para Eliminar filas con valores nulos en ciertas columnas
def eliminar_filas():
     print("TODO")

# 2) Sustituir valores erróneos o inconsistentes en columnas categóricas (no funciona correctamente)
def sustituir_valores(df, columna, valores_erroneos, valor_nuevo):
    # Nos asegurarnos de que la columna existe
    if columna not in df.columns:
        raise ValueError(f"La columna '{columna}' no se encuentra")
    
    try:
        df[columna] = df[columna].replace(valores_erroneos, valor_nuevo) 
        
    except Exception as e: 
         print(f"Error al sustituir valores: {e}")
    return df 
    
# 3) Convertir tipos de datos
def convertir_datos():
     print("TODO")

# 4) Convertir formatos de fecha a un estandar
def convertir_fechas(df, columna, formato="%Y-%m-%d"):
    try:
        # Nos asegurarnos de que la columna existe
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra")

        # Lista de formatos que se encuentran en el dataset
        formatos_validos = ["%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y", "%m.%d.%Y"]
        fechas_convertidas = pd.Series(index=df.index, dtype="datetime64[ns]") #datetime64[ns] es un formato específico de Pandas

        # Intentar convertir las fechas con cada formato
        for fmt in formatos_validos:
            mask = fechas_convertidas.isnull()  # Procesar solo valores no convertidos
            fechas_convertidas[mask] = pd.to_datetime(df.loc[mask, columna], format=fmt, errors="coerce")

        # Formatear las fechas convertidas al formato deseado
        df[columna] = fechas_convertidas.dt.strftime(formato)

    except Exception as e:
        print(f"Error al convertir fechas: {e}")
    return df


# 5) Extraer el día de la semana de una fecha
def obtener_dia():
     print("TODO")

# 6) Comparar la fecha de reservación con fechas precias para detectar patrones.
def comparar_reservacion():
     print("TODO")

# 7) Crear una nueva columna basada en operaciones con otras columnas
def nueva_columna():
     print("TODO")

# 8) Ajustar valores atípicos dentro de un rango permitido
def ajustar_valores():
     print("TODO")

# 9) Redondear valores numéricos en columnas específicas
def redondear_valores():
     print("TODO")

# 10) Analizar tendencias de reservaciones por mes, tipo de habitación, etc.
def analizar_reservaciones():
     print("TODO")

# 11) Identificar y eliminar registros duplicados
def eliminar_duplicados():
     print("TODO")

# 12) Calcular acumulados de ingresos por mes
def ingresos_por_mes():
     print("TODO")