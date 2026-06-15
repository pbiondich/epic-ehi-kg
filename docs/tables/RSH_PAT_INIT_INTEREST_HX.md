# RSH_PAT_INIT_INTEREST_HX

> History of patient-initiated interest (I LAR 800) for the enrollment.

**Primary key:** `ENROLL_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the enrollment record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_PAT_INITIATED_INTEREST_C_NAME` | VARCHAR |  | A history of the patient-initiated interest category IDs for the enrollment. |
| 4 | `HX_PAT_INTEREST_MOD_UTC_DTTM` | DATETIME (UTC) |  | The UTC instant in which the patient-initiated interest for the enrollment was changed. |
| 5 | `HX_PAT_INTEREST_MOD_MYPT_ID` | VARCHAR |  | The unique ID of the patient access account who changed the patient-initiated interest. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

