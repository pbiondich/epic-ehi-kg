# MED_DISP_ALL_DX_CODE_SYS

> The coding system used for all diagnosis codes for the medication in the medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface. This table is replacing columns MED_DIS_PRIM_DX_SYS and MED_DIS_SEC_DX_SYS in table DOCS_RCVD_MED_DISP.

**Primary key:** `DOCUMENT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `MED_DIS_ALL_DX_SYS` | VARCHAR |  | The coding system used for all diagnosis codes for the medication int he medication dispensed segment of the external e-prescription, received through the incoming e-prescribing interface. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

