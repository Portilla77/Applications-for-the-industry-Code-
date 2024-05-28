
/*
CREATE DATABASE [DB Banco P2];
*/


USE [DB Banco P2];
GO

CREATE TABLE [Asesoramiento Financiero] (
    AsesoramientoID INT PRIMARY KEY,
    [Plan financiero] NVARCHAR(MAX)
);
GO

CREATE TABLE [Clientes] (
    ClienteID INT PRIMARY KEY,
    Nombre NVARCHAR(255),
    Direccion NVARCHAR(255),
    Telefono NVARCHAR(50)
);
GO

CREATE TABLE [Productos] (
    ProductoID INT PRIMARY KEY,
    Nombre NVARCHAR(255),
    Tipo NVARCHAR(50),
    Categoria NVARCHAR(50)
);
GO

CREATE TABLE [Tipo de Cambio] (
    [Fecha de operacion] DATE PRIMARY KEY,
    [Tasa de cambio] FLOAT,
    [Moneda de origen] NVARCHAR(3),
    [Moneda de destino] NVARCHAR(3)
);
GO

CREATE TABLE [Productos o Servicios contratados por los clientes] (
    TransaccionID INT PRIMARY KEY,
    ClienteID INT,
    ProductoID INT,
    Cantidad INT,
    [Fecha de contratacion] DATE,
    [Valor de transaccion] FLOAT,
    FOREIGN KEY (ClienteID) REFERENCES [Clientes](ClienteID),
    FOREIGN KEY (ProductoID) REFERENCES [Productos](ProductoID)
);
GO

CREATE TABLE [Operaciones en cuentas de cheques e inversiones] (
    OperacionID INT PRIMARY KEY,
    ClienteID INT,
    Monto FLOAT,
    AsesoramientoID INT NULL,
    ProductoID INT NULL,
    [Fecha de operacion] DATE,
    [Tipo de operacion] NVARCHAR(50),
    FOREIGN KEY (ClienteID) REFERENCES [Clientes](ClienteID),
    FOREIGN KEY ([Fecha de operacion]) REFERENCES [Tipo de Cambio]([Fecha de operacion]),
    FOREIGN KEY (AsesoramientoID) REFERENCES [Asesoramiento Financiero](AsesoramientoID),
    FOREIGN KEY (ProductoID) REFERENCES [Productos](ProductoID)
);
GO

CREATE TABLE [Operaciones en cr�dito] (
    CreditoID INT PRIMARY KEY,
    ClienteID INT,
    ProductoID INT,
    AsesoramientoID INT NULL,
    [Fecha de credito] DATE,
    [Monto de credito] FLOAT,
    [Estado de credito] NVARCHAR(50),
    FOREIGN KEY (ClienteID) REFERENCES [Clientes](ClienteID),
    FOREIGN KEY (ProductoID) REFERENCES [Productos](ProductoID),
    FOREIGN KEY (AsesoramientoID) REFERENCES [Asesoramiento Financiero](AsesoramientoID)
);
GO


CREATE TABLE [Clientes Asesoramiento] (
    ClienteID INT,
    AsesoramientoID INT,
    ProductoID INT,
    PRIMARY KEY (ClienteID, AsesoramientoID),
    FOREIGN KEY (ClienteID) REFERENCES [Clientes](ClienteID),
    FOREIGN KEY (AsesoramientoID) REFERENCES [Asesoramiento Financiero](AsesoramientoID),
    FOREIGN KEY (ProductoID) REFERENCES [Productos](ProductoID)
);
GO
