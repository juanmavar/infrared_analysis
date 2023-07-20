Title: Conclusiones
Date: 2023-07-03
Category: Page
Ordinal: 005


# PRINCIPALES RESULTADOS

En este proyecto se ha desarrollado en Python, una función de procesamiento de imágenes infrarrojas que genera una lookup table para asociar el color de cada píxel con una temperatura específica. La función demostró ser capaz de correlacionar con suficiente precisión el color de los píxeles de la imagen con valores de temperatura.

El código de procesamiento de imágenes probó su eficacia para manipular y analizar los datos de la imagen infrarroja, lo que permitió la generación de una LUT detallada y precisa. Esto constituye una herramienta valiosa para analizar imágenes infrarrojas capturadas con esta cámara y extraer información de temperatura de fácil interpretación.

A continuación se muestra el código de la función, que toma como entrada una imagen infrarroja y un diccionario con la base de imágenes de dígitos a identificar.

``` python
def lut_temperatura(img, base_digitos):
    # Recorte de dígitos
    _ , t_max_1=cv2.threshold(I[46:60,282:295].mean(axis=2),190,255,cv2.THRESH_BINARY_INV) 
    _ , t_max_2=cv2.threshold(I[46:60,291:304].mean(axis=2),190,255,cv2.THRESH_BINARY_INV) 
    _ , t_max_3=cv2.threshold(I[46:60,304:317].mean(axis=2),190,255,cv2.THRESH_BINARY_INV) 
    _ , t_min_1=cv2.threshold(I[179:193,282:295].mean(axis=2),190,255,cv2.THRESH_BINARY_INV) 
    _ , t_min_2=cv2.threshold(I[179:193,291:304].mean(axis=2),190,255,cv2.THRESH_BINARY_INV) 
    _ , t_min_3=cv2.threshold(I[179:193,304:317].mean(axis=2),190,255,cv2.THRESH_BINARY_INV)
    
    # Detección de dígitos con template matching
    d1_max=match_digit(t_max_1)
    d2_max=match_digit(t_max_2)
    d3_max=match_digit(t_max_3)
    d1_min=match_digit(t_min_1)
    d2_min=match_digit(t_min_2)
    d3_min=match_digit(t_min_3)
    
    #Recomposición de temperatura
    t_max = float(d1_max + d2_max + '.' + d3_max)
    t_min = float(d1_min + d2_min + '.' + d3_min)
    
    #Generación de la LUT
    perfil= I[72:167,310,:].astype(np.float32)
    saltos= perfil.shape[0]-1
    deltaT= (t_max-t_min)/saltos
    lista_temperatura = np.round(t_max - np.arange(saltos+1) * deltaT, 2)
    temp_dic={"Color RGB": perfil.astype(np.uint8).tolist(),
          "Temperatura (°C)": lista_temperatura}
    df_temperatura = pd.DataFrame(temp_dic)
    
    return df_temperatura

```

# TRABAJOS FUTUROS

En cuanto a los trabajos futuros, existen varias direcciones para la mejora y expansión de este proyecto. Primero, se puede trabajar en la optimización del algoritmo para mejorar aún más la precisión de la tabla generada. Segundo, se podrían explorar diferentes métodos para correlacionar los colores de los píxeles con las temperaturas, lo que podría llevar a la generación de LUT más precisas. Además, se podría crear una función más general, que permita ser aplicada a imágenes infrarrojas cuya escala esté en otro formato, o tenga temperaturas que excedan los 99.9°C.

Por último, se podría tomar las tablas generadas como base para continuar con trabajos de segmentación y extracción de temperaturas de plantas con el fin de determinar la presencia de enfermedades.