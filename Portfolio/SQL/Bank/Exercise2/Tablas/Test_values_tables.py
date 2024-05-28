import os
from datetime import datetime
import pandas as pd

asesoramiento_financiero = pd.DataFrame({
    'AsesoramientoID': range(1, 11),
    'Plan financiero': [f"Plan {i}" for i in range(1, 11)]
})

clientes = pd.DataFrame({
    'ClienteID': range(1, 11),
    'Nombre': [f"Cliente {i}" for i in range(1, 11)],
    'Direccion': [f"Calle {i}, Ciudad {i}" for i in range(1, 11)],
    'Telefono': [f"555-000{i}" for i in range(10)]
})

productos = pd.DataFrame({
    'ProductoID': range(1, 11),
    'Nombre': [f"Producto {i}" for i in range(1, 11)],
    'Tipo': ["Financiero" if i % 2 == 0 else "Servicio" for i in range(1, 11)],
    'Categoria': ["Categoría A" if i % 2 == 0 else "Categoría B" for i in range(1, 11)]
})

tipo_cambio = pd.DataFrame({
    'Fecha de operacion': [datetime(2020, 1, 1) + pd.DateOffset(days=i*10) for i in range(10)],
    'Tasa de cambio': [1.1 + 0.01 * i for i in range(10)],
    'Moneda de origen': ["USD"]*10,
    'Moneda de destino': ["MXN"]*10
})

productos_servicios = pd.DataFrame({
    'TransaccionID': range(1, 11),
    'ClienteID': range(1, 11),
    'ProductoID': range(1, 11),
    'Cantidad': [10, 5, 15, 7, 20, 12, 3, 4, 11, 9],
    'Fecha de contratacion': [datetime(2020, 1, 1) + pd.DateOffset(days=i*15) for i in range(10)],
    'Valor de transaccion': [100.0 * i for i in range(1, 11)]
})

operaciones_cuentas = pd.DataFrame({
    'OperacionID': range(1, 11),
    'ClienteID': range(1, 11),
    'Monto': [1000.0 * i for i in range(1, 11)],
    'AsesoramientoID': [None, None, 1, 2, None, 3, None, 4, None, 5],
    'ProductoID': [None, 1, 2, None, 3, None, 4, None, 5, None],
    'Fecha de operacion': [datetime(2020, 1, 1) + pd.DateOffset(days=i*20) for i in range(10)],
    'Tipo de operacion': ["Cheque" if i % 2 == 0 else "Inversión" for i in range(10)]
})

operaciones_credito = pd.DataFrame({
    'CreditoID': range(1, 11),
    'ClienteID': range(1, 11),
    'ProductoID': range(1, 11),
    'AsesoramientoID': [None]*5 + [6, 7, 8, 9, 10],
    'Fecha de credito': [datetime(2020, 2, 1) + pd.DateOffset(days=i*25) for i in range(10)],
    'Monto de credito': [500.0 * i for i in range(10)],
    'Estado de credito': ["Activo" if i % 2 == 0 else "Pagado" for i in range(10)]
})

clientes_asesoramiento = pd.DataFrame({
    'ClienteID': range(1, 11),
    'AsesoramientoID': range(1, 11),
    'ProductoID': range(1, 11)
})

data_frames = {
    'Asesoramiento Financiero': asesoramiento_financiero,
    'Clientes': clientes,
    'Productos': productos,
    'Tipo de Cambio': tipo_cambio,
    'Productos o Serviciosn contratados': productos_servicios,
    'Operaciones cuentas': operaciones_cuentas,
    'Operaciones credito': operaciones_credito,
    'Clientes asesoramiento': clientes_asesoramiento
}

output_dir = "C:/Users/athan/Documents/Applications-for-the-industry-Code-/Portafolio/SQL/Bank/Exercise2/Tablas"

os.makedirs(output_dir, exist_ok=True)

for name, df in data_frames.items():
    df.to_csv(f"{output_dir}/{name}.csv", index=False)

os.listdir(output_dir)
