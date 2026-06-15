# OTP_ALERT_CSN

> The contact serial numbers (CSNs) of all alerts (ALT records) that have been shown for the linked patient order template (OTP) record.

**Primary key:** `OTP_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The order template ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number that corresponds to an alert contact serial number (CSN) in the order template in this row. |
| 4 | `CONTACT_DATE` | DATETIME |  | The contact date in external format of the showing of an alert contact serial number (CSN) in the order template in this row. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | The ID of the deployment owner for this contact. |
| 6 | `ALERT_CSN` | NUMERIC |  | The contact serial number (CSN) of an alert in the order template in this row. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

