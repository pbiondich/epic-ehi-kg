# IDENTITY_ID_HX

> The IDENTITY_ID_HX table contains the system master person index ID History for your patients. Each patient may have multiple master person index IDs; therefore, a line number is used to identify each identification number for a patient.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID assigned to the patient record. This ID may be encrypted if you have elected to use enterprise reporting’s encryption utility. |
| 2 | `LINE` | INTEGER | PK | The line number of the patient ID within the patient’s record. |
| 3 | `ID_HX` | VARCHAR |  | The old master person index ID for the patient record. |
| 4 | `ID_TYPE_HX` | NUMERIC |  | The old master person index ID Type for the patient record. |
| 5 | `ID_TYPE_HX_ID_TYPE_NAME` | VARCHAR |  | The name of the ID Type. |
| 6 | `IDENTITY_NEW_ID` | VARCHAR |  | The ID that is now active for this ID Type. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

