select patient_id, patient_name, conditions
from Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';