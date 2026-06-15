# HL_REQ_REQUIREMENTS

> Hospital Logistics Request Requirements.

**Primary key:** `HLR_ID`, `LINE`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLR_ID` | NUMERIC | PK shared | The unique identifier for the request record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REQUIREMENT_C_NAME` | VARCHAR | org | This Logistics Request's requirements. Technicians need to adhere to these requirements to complete this Request. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

