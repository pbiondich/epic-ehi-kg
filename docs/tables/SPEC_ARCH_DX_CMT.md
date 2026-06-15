# SPEC_ARCH_DX_CMT

> This table extracts the related multiple response Archived Order Associated Diagnosis Comment (I OVS 33009) item, which contains the diagnosis comment for diagnoses associated with an archived order.

**Primary key:** `SPECIMEN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `ARCH_ORD_DX_CMT` | VARCHAR |  | Diagnosis comment for a diagnosis associated with an order that has been archived as part of deceased patient archiving. Once the order is archived, all of the data from the order record is deleted and will not be available. This item is one of a group of items in the specimen record that are populated at the time of archiving by copying the most important pieces of information from the order record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

