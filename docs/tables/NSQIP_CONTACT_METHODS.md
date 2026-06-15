# NSQIP_CONTACT_METHODS

> This table contains the contact methods for patient follow-up for NSQIP registry data for the surgeries that are selected for NSQIP submission. It is used in conjunction with NSQIP_INFO table.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NSQIP_CONTACT_METHOD_C_NAME` | VARCHAR |  | The contact method that was used to follow the case. It is used only if the case was not followed for full 30 days. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

