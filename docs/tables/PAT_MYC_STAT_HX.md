# PAT_MYC_STAT_HX

> This table keeps an audit trail of web-based chart system status changes made to a patient. This table can be used to determine when, who, and how a status was changed for a patient account. Every time the status is modified, a new row is added to this table.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MYC_STAT_HX_C_NAME` | VARCHAR |  | The activation status category number for the patient. |
| 4 | `MYC_STAT_HX_EMP_ID` | VARCHAR |  | The unique ID of the employee that has changed status. |
| 5 | `MYC_STAT_HX_EMP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `MYC_STAT_HX_CMT` | VARCHAR |  | Item to store comments for status changes |
| 7 | `MYC_STAT_HX_MTHD_C_NAME` | VARCHAR | org | The method of the status change for patients. This can be used to determine how or why the status was changed. For example, this could be used to find the method of activation code generation that is most successful for patient signup. |
| 8 | `DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `WORKSTATION_ID_WORKSTATION_NAME` | VARCHAR |  | This is the internal workstation name. |
| 10 | `MYC_PROXY_ACTIVATION_YN` | VARCHAR |  | Flag indicating whether an activation status is due to a proxy or not. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

