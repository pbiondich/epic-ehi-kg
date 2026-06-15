# OTP_OPIMS_OVERRIDE_DOSE

> This group of tables stores information about the override that a clinician entered when they chose to not use the products chosen by outpatient Intelligent Medication Selection (IMS). This table stores the IMS suggested dose for the products that were overridden, found in the OPIMS Overridden Suggested Dose (I OTP 11604) item.

**Primary key:** `OTP_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OTP_ID` | NUMERIC | PK FK→ | The unique identifier for the patient order template record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `COMPONENT_DOSE` | VARCHAR |  | Stores the dose of the products that Intelligent Medication Selection (IMS) selected. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OTP_ID` | [OTP_INFO](OTP_INFO.md) | overflow_master | medium |

