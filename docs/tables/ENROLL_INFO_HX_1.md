# ENROLL_INFO_HX_1

> The ENROLL_INFO_HX_1 contains a history of changes to the study coordinators assigned to a patient's enrollment in a research study. This table should be linked to ENROLL_INFO_HX in order to determine additional information like when the change was made and who made the change.

**Overflow of:** [ENROLL_INFO_HX](ENROLL_INFO_HX.md)  
**Primary key:** `ENROLL_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ENROLL_ID` | NUMERIC | PK FK→ | The unique ID of the patient enrollment record for this row. This column is frequently used to link to the ENROLL_INFO table. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated study coordinators history in this enrollment record. Together with ENROLL_ID, this forms the foreign key to the ENROLL_INFO_HX table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple study coordinators that are associated with the enrollment modification from the ENROLL_INFO_HX table. |
| 4 | `HX_MOD_COORD_ID` | VARCHAR |  | The user ID of the study coordinators for the enrollment. |
| 5 | `HX_MOD_COORD_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ENROLL_ID` | [ENROLL_INFO](ENROLL_INFO.md) | sole_pk | high |

