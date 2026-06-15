# PAT_NFC_DEVICES

> This table stores unique identifiers for each of a patient's Near-Field Communication (NFC) devices.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEVICE_IDENT` | VARCHAR |  | A unique identifier for a specific NFC tag. |
| 4 | `DEVICE_ACTION_C_NAME` | VARCHAR |  | An action taken on a specific NFC device (DEVICE_IDENT). |
| 5 | `ACTION_DTTM` | DATETIME (UTC) |  | This item stores the instant at which an action (DEVICE_ACTION_C) was taken on an NFC device (DEVICE_IDENT). |
| 6 | `NFC_USER_ID` | VARCHAR |  | The record ID of the user who performed an action (DEVICE_ACTION_C) on an NFC device (DEVICE_IDENT). |
| 7 | `NFC_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

