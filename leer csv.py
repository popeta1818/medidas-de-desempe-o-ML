def leer_csv(filepath):
    y_true = []
    y_pred = []
    with open(filepath, 'r') as file:
        next(file)  # Saltar la primera línea (encabezado)
        for i, line in enumerate(file):
            valores = line.strip().split(',')
            
            # Imprimir las primeras 5 líneas para inspeccionar los datos
            if i < 5:
                print(f"Línea {i + 1}: {valores}")
            
            # Mapear etiquetas categóricas a valores binarios para "survival_status"
            if valores[3].strip() == ' <=50K':
                y_true.append(0)
            elif valores[3].strip() == ' >50K':
                y_true.append(1)
            
            # Mapear otra columna a valores binarios (por ejemplo, "nodes" o "sex")
            # Ajusta el índice o valor según el contenido del archivo
            if valores[2].strip() == ' Male':
                y_pred.append(1)
            elif valores[2].strip() == ' Female':
                y_pred.append(0)
            else:
                # En caso de que no se pueda mapear, omitir el registro
                continue
    
    # Imprimir los primeros valores leídos para verificar
    print("Ejemplo de y_true:", y_true[:10])
    print("Ejemplo de y_pred:", y_pred[:10])
    
    return y_true, y_pred

def calcular_matriz_confusion(y_true, y_pred):
    TP = FP = FN = TN = 0
    for true, pred in zip(y_true, y_pred):
        if true == 1 and pred == 1:
            TP += 1
        elif true == 1 and pred == 0:
            FN += 1
        elif true == 0 and pred == 1:
            FP += 1
        elif true == 0 and pred == 0:
            TN += 1
    return TP, FP, FN, TN

def calcular_metricas(TP, FP, FN, TN):
    # Precision
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    # Recall
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    # Positive Predictive Value (PPV)
    ppv = precision
    # True Positive Rate (TPR)
    tpr = recall
    # True Negative Rate (TNR)
    tnr = TN / (TN + FP) if (TN + FP) > 0 else 0
    # False Positive Rate (FPR)
    fpr = FP / (FP + TN) if (FP + TN) > 0 else 0
    # False Negative Rate (FNR)
    fnr = FN / (FN + TP) if (FN + TP) > 0 else 0
    # F1-Score
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return precision, recall, ppv, tpr, tnr, fpr, fnr, f1_score

# Ruta del archivo CSV
filepath = 'c:/Users/Alejandro/Documents/datasets csv/adult.csv'

# Leer los datos del archivo CSV
y_true, y_pred = leer_csv(filepath)

# Verificar si las listas están vacías
if not y_true or not y_pred:
    print("No se encontraron datos válidos para y_true o y_pred.")
else:
    # Calcular la matriz de confusión
    TP, FP, FN, TN = calcular_matriz_confusion(y_true, y_pred)

    # Calcular las métricas
    precision, recall, ppv, tpr, tnr, fpr, fnr, f1_score = calcular_metricas(TP, FP, FN, TN)

    # Imprimir los resultados
    print(f"Matriz de Confusión: TP={TP}, FP={FP}, FN={FN}, TN={TN}")
    print(f"Precisión: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"Positive Predictive Value (PPV): {ppv:.2f}")
    print(f"True Positive Rate (TPR): {tpr:.2f}")
    print(f"True Negative Rate (TNR): {tnr:.2f}")
    print(f"False Positive Rate (FPR): {fpr:.2f}")
    print(f"False Negative Rate (FNR): {fnr:.2f}")
    print(f"F1-Score: {f1_score:.2f}")
