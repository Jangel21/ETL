import pandas as pd
import re

# 1) Función para eliminar filas con valores nulos en ciertas columnas
def eliminar_filas(df, columnas):
    try:
        # Verificar si las columnas existen en el DataFrame
        for columna in columnas:
            if columna not in df.columns:
                raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame. Columnas disponibles: {list(df.columns)}")

        # Eliminar filas con valores nulos en las columnas especificadas
        df = df.dropna(subset=columnas)
        print(f"Filas con valores nulos en las columnas {columnas} eliminadas correctamente.")
    
    except Exception as e:
        print(f"Error al eliminar filas con valores nulos: {e}")
    return df


# 2) Sustituir valores erróneos o inconsistentes en columnas categóricas (replace solo funciona para cadenas de texto)
def sustituir_valores(df, columna, valores_erroneos, valor_nuevo):
    try:
        # Verificar si la columna existe en el DataFrame
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame. Columnas disponibles: {list(df.columns)}")

        # Convertir valores erróneos a su tipo correcto si es necesario
        valores_erroneos = [int(val) if val.isdigit() else val for val in valores_erroneos]

        # Sustituir los valores erróneos por el nuevo valor
        df[columna] = df[columna].replace(valores_erroneos, valor_nuevo)
        print(f"Valores {valores_erroneos} en la columna '{columna}' sustituidos por '{valor_nuevo}'.")
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


# 5) Reemplazar valores nulos en una columna específica
def reemplazar_nulos(df, columna, valor_reemplazo):
    try:
        # Verificar si la columna existe en el DataFrame
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame. Columnas disponibles: {list(df.columns)}")

        # Reemplazar valores nulos con el valor especificado
        df[columna] = df[columna].fillna(valor_reemplazo)
        print(f"Valores nulos en la columna '{columna}' reemplazados con '{valor_reemplazo}'.")
    
    except Exception as e:
        print(f"Error al reemplazar valores nulos: {e}")
    return df


# 6) Agrupar datos y calcular estadísticas
def agrupar_y_calcular(df, columna_grupo, columna_calculo, operacion="suma"):
    try:
        # Verificar si las columnas existen en el DataFrame
        if columna_grupo not in df.columns:
            raise ValueError(f"La columna '{columna_grupo}' no se encuentra en el DataFrame.")
        if columna_calculo not in df.columns:
            raise ValueError(f"La columna '{columna_calculo}' no se encuentra en el DataFrame.")

        # Verificar si la columna de cálculo es numérica
        if not pd.api.types.is_numeric_dtype(df[columna_calculo]):
            df[columna_calculo] = pd.to_numeric(df[columna_calculo], errors='coerce')

        if df[columna_calculo].isna().all():
            raise TypeError(f"La columna '{columna_calculo}' no contiene valores numéricos válidos.")

        # Diccionario de operaciones permitidas
        operaciones = {
            "suma": "sum",
            "promedio": "mean",
            "conteo": "count",
            "max": "max",
            "min": "min"
        }

        # Verificar si la operación es válida
        if operacion not in operaciones:
            raise ValueError(f"La operación '{operacion}' no es válida. Use: {', '.join(operaciones.keys())}.")

        # Aplicar la operación
        resultado = df.groupby(columna_grupo, as_index=False).agg({columna_calculo: operaciones[operacion]})

        print(f"Operación '{operacion}' realizada correctamente.")
        return resultado

    except Exception as e:
        print(f"Error: {e}")
        return None

    except Exception as e:
        print(f"Error al agrupar y calcular: {e}")
        return None


# 7) Busca las anomalias en el dataset y las elimina
def eliminar_anomalias(df):
     try:
         # Calcular los cuartiles y el rango intercuartílico (IQR)
        Q1 = df.quantile(0.25)  # Primer cuartil (25%)
        Q3 = df.quantile(0.75)  # Tercer cuartil (75%)
        IQR = Q3 - Q1           # Rango intercuartílico

        # Definir límites para detectar anomalías
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identificar anomalías
        df_cleaned = df[~((df < lower_bound) | (df > upper_bound)).any(axis=1)]
 
     except Exception as e:
         print("\nError al eliminar las anomalias {e}\n")
     return df_cleaned
     

# 8) Ajustar valores atípicos dentro de un rango permitido
def ajustar_valores(df, column, min_value, max_value):
    try:
        #Se utiliza la funcion clip para normalizar los valores dentro de un rango
        df[column].clip(min_value, max_value)
    except Exception as e:
        print("\nError al ajustar valores: {e}\n")
     #Se retorna el df con los valores ya ajustados
    return df


# 9) Redondear valores numéricos en columnas específicas
def redondear_valores(df, columna, decimales):
    try:
        # Verificar si la columna existe en el DataFrame
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame. Columnas disponibles: {list(df.columns)}")

        # Verificar si la columna es numérica
        if not pd.api.types.is_numeric_dtype(df[columna]):
            raise TypeError(f"La columna '{columna}' no es numérica y no se puede redondear.")

        # Redondear los valores de la columna
        df[columna] = df[columna].round(decimales)
        print(f"Columna '{columna}' redondeada a {decimales} decimales correctamente.")
    
    except Exception as e:
        print(f"Error al redondear valores: {e}")
    return df


# 10) Ordenar el DataFrame por una columna específica
def ordenar_por_columna(df, columna, ascendente=True):
    try:
        # Verificar si la columna existe en el DataFrame
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame. Columnas disponibles: {list(df.columns)}")

        # Ordenar el DataFrame por la columna especificada
        df = df.sort_values(by=columna, ascending=ascendente)
        print(f"DataFrame ordenado por la columna '{columna}' en orden {'ascendente' if ascendente else 'descendente'}.")
        return df
    
    except Exception as e:
        print(f"Error al ordenar el DataFrame: {e}")
        return df
    

# 11) Identificar y eliminar registros duplicados
def eliminar_duplicados(df, columnas=None):
    try:
        # Limpiar espacios adicionales y normalizar cadenas en las columnas seleccionadas
        if columnas:
            for col in columnas:
                if col in df.columns and df[col].dtype == "object":
                    df[col] = df[col].str.strip().str.lower()  # Eliminar espacios y convertir a minúsculas

        # Eliminar duplicados
        df_sin_duplicados = df.drop_duplicates(subset=columnas)

        print(f"\nSe han eliminado {len(df) - len(df_sin_duplicados)} registros duplicados.\n")
        return df_sin_duplicados

    except Exception as e:
        print(f"\nError al eliminar duplicados: {e}\n")
        return df


# 12) Limpiar y formatear números de teléfono
def limpiar_telefonos(df, columna):
    try:
        # Verificar si la columna existe en el DataFrame
        if columna not in df.columns:
            raise ValueError(f"La columna '{columna}' no se encuentra en el DataFrame. Columnas disponibles: {list(df.columns)}")

        # Función para limpiar y formatear un número de teléfono
        def formatear_telefono(numero):
            # Eliminar caracteres no numéricos
            solo_numeros = re.sub(r"[^\d]", "", str(numero))
            
            # Verificar si el número tiene al menos 10 dígitos
            if len(solo_numeros) == 10:
                return f"({solo_numeros[:3]}) {solo_numeros[3:6]} {solo_numeros[6:]}"
            elif len(solo_numeros) == 11 and solo_numeros.startswith("1"):
                # Si tiene 11 dígitos y comienza con "1", eliminar el "1"
                solo_numeros = solo_numeros[1:]
                return f"({solo_numeros[:3]}) {solo_numeros[3:6]} {solo_numeros[6:]}"
            else:
                # Si no tiene un formato válido, devolver el número original
                return numero

        # Aplicar la función a la columna
        df[columna] = df[columna].apply(formatear_telefono)
        print(f"Columna '{columna}' formateada correctamente.")
    
    except Exception as e:
        print(f"Error al formatear los números de teléfono: {e}")
    return df