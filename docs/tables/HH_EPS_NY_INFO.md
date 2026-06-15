# HH_EPS_NY_INFO

> Extracts information about NY Medicaid Episodic Payment System (EPS) from Outcome and Assessment Information Set (OASIS) data sets where Medicaid is a payor.

**Primary key:** `OASIS_SET_ID`, `CONTACT_DATE_REAL`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OASIS_SET_ID` | NUMERIC | PK FK→ | The unique identifier for the data set record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `EPS_GROUPER_CODE` | VARCHAR |  | Stores the NY Medicaid EPS Grouper Code as calculated from OASIS data. This grouper code is analogous to the OASIS HHRG. |
| 5 | `EPS_RATE_CODE` | VARCHAR |  | Stores the NY Medicaid EPS Rate Code as calculated from OASIS data. This rate code is analogous to an OASIS HIPPS code. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OASIS_SET_ID` | [HH_OASIS_INFO](HH_OASIS_INFO.md) | sole_pk | high |

