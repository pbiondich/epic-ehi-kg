# APPT_REQ_RELEVANT_DEPTS

> This table contains departments relevant to appointment requests. It includes currently and previously responsible departments, visit departments, the creation department, and the current referred-to department in the linked referral.

**Primary key:** `REQUEST_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REQUEST_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RELEVANT_DEPARTMENT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REQUEST_ID` | [APPT_REQUEST](APPT_REQUEST.md) | sole_pk | high |

