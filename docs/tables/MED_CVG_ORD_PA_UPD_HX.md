# MED_CVG_ORD_PA_UPD_HX

> This table stores the history of attempts to update the prior authorization required flag on a medication order from a medication estimate record. Each row represents one attempt, including whether the update succeeded, was skipped, or failed, the reason if it did not succeed, and the date and time of the attempt.

**Primary key:** `MED_ESTIMATE_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `ORD_PA_UPD_HX_C_NAME` | NUMERIC |  | The prior authorization required status category ID that was attempted to be set on the medication order during this update attempt. |
| 6 | `ORD_PA_UPD_OUTC_C_NAME` | NUMERIC |  | The outcome category ID for this prior authorization required flag update attempt on the medication order. |
| 7 | `ORD_PA_UPD_REASON_C_NAME` | NUMERIC |  | The error or skip reason category ID for this prior authorization required flag update attempt on the medication order. This is only populated when the update was not successful. |
| 8 | `ORD_PA_UPD_UTC_DTTM` | DATETIME (UTC) |  | The UTC date and time of the prior authorization required status update attempt on the medication order. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MED_ESTIMATE_ID` | [MED_CVG_INFO](MED_CVG_INFO.md) | sole_pk | high |

