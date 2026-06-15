# OR_CASE_SPEC_GI_TM_SLOT

> This table is used for the Case Planned in Specific GI Surgical Service Timeslot (I ORC 7912) item.

**Primary key:** `CASE_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CASE_ID` | VARCHAR | PK shared | The unique identifier for the case request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CASE_GI_TM_SLOT_C_NAME` | VARCHAR | org | List with all the Gastrointestinal (GI) surgical services assigned to the surgeon record (I SER 5030). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

