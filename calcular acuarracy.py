def calcular_accuracy(y_true, y_pred):
    aciertos = 0
    n = len(y_true)
    for i in range(n):
        if y_true[i] == y_pred[i]:
            aciertos += 1
    return aciertos / n

def calcular_error(y_true, y_pred):
    errores = 0
    n = len(y_true)
    for i in range(n):
        if y_true[i] != y_pred[i]:
            errores += 1
    return errores / n

# Ejemplo de uso
y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 1]

accuracy = calcular_accuracy(y_true, y_pred)
error = calcular_error(y_true, y_pred)

print(f"Precisión (Accuracy): {accuracy:.2f}")
print(f"Error: {error:.2f}")