# PO_STATUS_GROUP

> This table displays PO (per os) status information for patients (EPT).

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `PO_STATUS_C_NAME` | VARCHAR |  | The category number for the PO Status in this patient encounter. |
| 6 | `START_DTTM` | DATETIME (Local) |  | The start instant of this PO Status for the patient. |
| 7 | `END_DTTM` | DATETIME (Local) |  | The end instant of this PO Status for the patient. |
| 8 | `PO_CHANGE_USER_ID` | VARCHAR |  | The unique user (EMP) ID of the user who changed the PO Status for this patient. |
| 9 | `PO_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `PO_CHANGE_ORD_ID` | NUMERIC |  | The unique Order ID associated with the PO Status change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

