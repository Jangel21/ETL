import pandas as pd

# 1) Funcion para Eliminar filas con valores nulos en ciertas columnas
def eliminar_filas():
     print("TODO")

# 2) Sustituir valores erróneos o inconsistentes en columnas categóricas (replace solo funciona para cadenas de texto)
def sustituir_valores(df, columna, valores_erroneos, valor_nuevo):
    try:
        # Nos asegurarnos de que la columna existe
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra")
    
        # Reemplazar los valores erróneos
        df[columna] = df[columna].replace(valores_erroneos, valor_nuevo)

    except Exception as e: 
         print(f"Error al sustituir valores: {e}")
    return df 
    
# 3) Convertir tipos de datos
def convertir_tipo_dato(df, columna, nuevo_tipo):
    try:
        # Nos asegurarnos de que la columna existe
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra")
        
        # Convertir la columna al tipo especificado
        df[columna] = df[columna].astype(nuevo_tipo)
    except Exception as e:
        print(f"Error al convertir el tipo de datos: {e}")
    return df

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
def obtener_dia_semana():
     print("TODO")

# 6) Comparar la fecha de reservación con fechas precias para detectar patrones.
def comparar_reservacion():
     print("TODO")

# 7) Crear una nueva columna basada en operaciones con otras columnas
def total_personas(df):
    try:
        # Se suman todas las personas que estuvieron en la habitación, si es nulo se convierte en 0
        df["total_people"] = df["adults"].fillna(0) + df["children"].fillna(0) + df["babies"].fillna(0)
        print("\nSe ha agregado la columna 'total_people' correctamente.\n")

    except Exception as e:
        print("\nError al calcular total de personas: {e}\n")

    #Se regresa el nuevo dataframe con la nueva columna  
    return df
     
# 8) Ajustar valores atípicos dentro de un rango permitido
def ajustar_valores(dataframe, column, min_value, max_value):
    try:
        #Con una expresion lambda compara que cada valor se encuentre dentro del rango deseado
        dataframe[column] = dataframe[column].apply(
            lambda x: min(max(x, min_value), max_value)
        )
    except Exception as e:
        print("\nError al ajustar valores: {e}\n")
     #Se retorna el dataframe con los valores ya ajustados
    return dataframe

# 9) Redondear valores numéricos en columnas específicas
def redondear_valores():
     print("TODO")

# 10) Analizar tendencias de reservaciones por mes, tipo de habitación, etc.
def analizar_reservaciones():
     print("TODO")

# 11) Identificar y eliminar registros duplicados
def eliminar_duplicados(original_dataframe):
    
    #Se eliminan los registros duplicados
    filter_dataframe = original_dataframe.drop_duplicates()

    #Se mezclan el dataframe original y el ya filtrado, posteriormente solo se conservan los duplicados 
    eliminated_registers = pd.merge(
        original_dataframe,
        filter_dataframe,
        how='outer',
        indicator=True
    ).query('_merge == "left_only"').drop(columns=['_merge'])

    # Se retornan tanto el dataframe original como el ya filtrado 
    return filter_dataframe, eliminated_registers

# 12) Calcular acumulados de ingresos por mes
def ingresos_por_mes():
     print("TODO")