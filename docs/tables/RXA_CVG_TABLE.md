# RXA_CVG_TABLE

> Table that holds coverage information for an adjudication. Adjudication records are used by Ambulatory Pharmacy during prescription copay adjudication.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique, internal contact date in decimal format. The integer portion of the number indicates the date of the contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 5 | `CVG_ID` | NUMERIC | FK→ | The unique ID of the coverage for which the adjudication record was created. |
| 6 | `TX_TYPE_C_NAME` | VARCHAR |  | Transaction Type category ID of the adjudication message |
| 7 | `PAYOR_SHEET_ID` | NUMERIC | FK→ | The payor sheet that is used during adjudication. Each time an adjudication occurs on a prescription the payor sheet to use is determined based on setup in the payor and plan records. |
| 8 | `PAYOR_SHEET_ID_RECORD_NAME` | VARCHAR |  | The name of this payor sheet |
| 9 | `ACTION_INSTANT_DTTM` | DATETIME (UTC) |  | Date and time when the adjudication action was performed on the prescription fill. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CVG_ID` | [COVERAGE](COVERAGE.md) | sole_pk | high |
| `PAYOR_SHEET_ID` | [APS_PAYOR_SHEET](APS_PAYOR_SHEET.md) | sole_pk | high |

