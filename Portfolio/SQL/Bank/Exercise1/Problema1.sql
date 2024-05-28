SELECT *
FROM Estudiantes Est

SELECT *
FROM Amigos am

SELECT *
FROM Salario sala

SELECT
    Est.Nombre AS [Nombre del estudiante],
    EstSal.Salario AS [Salario del estudiante],
    Am.Nombre AS [Nombre del amigo],
    AmSal.Salario AS [Salario del amigo],
    CASE
        WHEN AmSal.Salario > EstSal.Salario THEN Am.Nombre
        ELSE Est.Nombre
    END AS [Nombre de qui�n gana m�s]
FROM
    Estudiantes Est
JOIN
    Amigos A ON Est.ID = A.ID
JOIN
    Estudiantes Am ON A.Amigo_ID = Am.ID
JOIN
    Salario EstSal ON Est.ID = EstSal.ID
JOIN
    Salario AmSal ON Am.ID = AmSal.ID
WHERE
    AmSal.Salario > EstSal.Salario
ORDER BY
    AmSal.Salario ASC;
