# PAT_LIFEDOSE

> This is the patient life time dose total information for tracked chemicals in Medication Options. Detail history tracking information is in life time dose history table, PAT_LIFEDOSE_HX.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s security utility. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHEMICAL_C_NAME` | VARCHAR | org | The chemical category ID for the chemical that needs to be tracked for lifetime dosing for this patient. |
| 4 | `SIMP_DOSE_AMT` | NUMERIC |  | The dose in simplified unit that has been given to the patient in their lifetime for the tracked chemical. |
| 5 | `SIMP_DOSE_UNIT_C_NAME` | VARCHAR | org | The simplified dose unit category ID for the chemical that needs to be tracked for lifetime dosing for this patient. |
| 6 | `CALC_DOSE_AMT` | NUMERIC |  | The total dose given to the patient in their lifetime in the unit used to check for lifetime dose checking. |
| 7 | `CALC_DOSE_UNIT_C_NAME` | VARCHAR |  | The calculated dose unit category ID for the chemical needing to be tracked for lifetime dosing for this patient. |
| 8 | `LAST_EDIT_INST` | DATETIME (Local) |  | The last instant that the data in this line was edited. |
| 9 | `LIFE_DOSE_ERRORS` | NUMERIC |  | Indicates the number of errors for the chemical. If it is empty, we haven't calculated the total number of errors. If the value is zero, there are no errors for the chemical. |
| 10 | `REVIEW_STATUS_YN` | VARCHAR |  | Indicates whether the chemical should be reviewed. 'Y' means the chemical should be reviewed. Default is 'N'. |
| 11 | `LIFE_DOSE_WARNINGS` | INTEGER |  | This item counts the number of manual lifetime dose entries which are missing a simple dose |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

