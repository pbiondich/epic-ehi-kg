# PAT_ENC_BCB_HST

> Extracts information regarding the bed charge billing history for a patient's encounter.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 15  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `BED_CHARGE_DATE` | DATETIME |  | The dates that bed charges have been generated for this patient. |
| 6 | `HTR` | VARCHAR |  | Link to the transaction that represents the bed charge on the hospital account record (HAR). |
| 7 | `BED_CHARGE_BCC_ID` | NUMERIC |  | The unique ID of the cost center record associated with the bed charge. |
| 8 | `BED_CHARGE_BCC_ID_COST_CENTER_NAME` | VARCHAR |  | The name of the cost center. |
| 9 | `BED_CHARGE_UNIT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 10 | `BED_CHARGE_PROC_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 11 | `BED_CHARGE_DTTM` | DATETIME (Local) |  | Contains the instant for which the bed charge was dropped. |
| 12 | `BED_CHARGE_ROOM_ID_ROOM_NAME` | VARCHAR |  | The name of the Room record. |
| 13 | `BED_CHARGE_BED_ID` | VARCHAR |  | The unique ID of the bed where the patient is charged for. |
| 14 | `BED_CHARGE_BED_ID_BED_LABEL` | VARCHAR |  | The name of the bed. |
| 15 | `BED_CHARGE_ACCOMMODATION_C_NAME` | VARCHAR | org | The accommodation code category ID the patient is charged for. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

