# DENT_ORD_NOADD

> No-add items for dental orders.

**Primary key:** `ORDER_ID`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record |
| 2 | `DENTAL_PROC_AREA_C_NAME` | VARCHAR |  | Specifies the area of the oral cavity that a dental procedure is performed on |
| 3 | `DENTAL_COMP_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `DEN_PROC_EXISTING_YN` | VARCHAR |  | Indicates whether a procedure existed as part of the patient's presenting condition. |
| 5 | `DENT_SRC_PRL_INST_DTTM` | DATETIME (Local) |  | The Instant the Dental Order was created from a PRL Dental Template |
| 6 | `DENT_PROC_DNF_ID` | NUMERIC |  | The linked procedure (RES) ID that was marked Did Not Finish, to be completed in a subsequent visit |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

