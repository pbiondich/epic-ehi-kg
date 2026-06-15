# CAL_REFERENCE_CRM

> The Customer Relationship Management record that is referenced by the communication.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | VARCHAR | PK shared | The unique ID for the Communication Tracking record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `REF_CRM_ID` | NUMERIC |  | The unique ID of the Customer Relationship Management (CRM) that is reference by the communication. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

