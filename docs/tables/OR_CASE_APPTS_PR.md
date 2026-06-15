# OR_CASE_APPTS_PR

> The OR_CASE_APPTS_PR table contains OR management system case appointments. This table contains pre-operation information.

**Primary key:** `OR_CASE_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `OR_CASE_ID` | VARCHAR | PK FK→ | The unique ID of the case record. |
| 2 | `LINE` | INTEGER | PK | The number of the line of the pre-op and post-op appointment that need to be scheduled. |
| 3 | `UNIQUE_ID` | VARCHAR |  | The unique ID of the appointment that has been scheduled. |
| 4 | `APPT_PRC_ID_PRC_NAME` | VARCHAR |  | The name of the visit type. |
| 5 | `OR_PROC_ID` | VARCHAR | FK→ | The unique ID of the related surgical procedure for which the appointment needs to be scheduled. |
| 6 | `OR_PROC_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 7 | `PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 8 | `DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |
| 9 | `ASN` | NUMERIC |  | The unique appointment serial number associated with the appointment that is scheduled. |
| 10 | `PXPASS_TASK_ID` | NUMERIC |  | This item stores the Procedure Pass (PxP) record this appointment was automatically linked from (if any). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `OR_CASE_ID` | [OR_CASE](OR_CASE.md) | name_stem | high |
| `OR_PROC_ID` | [OR_PROC](OR_PROC.md) | sole_pk | high |

