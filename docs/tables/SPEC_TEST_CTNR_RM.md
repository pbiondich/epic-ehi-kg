# SPEC_TEST_CTNR_RM

> This table extracts the related multiple response Performing Containers (I OVS 51600) item.

**Primary key:** `SPECIMEN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `PERFORMING_OVC_ID` | VARCHAR |  | Specifies the list of performing containers associated with a particular test. A blank value indicates that any collection container or unassociated aliquot may be used as the performing container. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

