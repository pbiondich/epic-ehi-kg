# OR_LNLG_DIAGNOSIS

> This table contains the Diagnosis information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `DX_ORP_ID` | VARCHAR |  | Procedure associated with this diagnosis. |
| 3 | `DX_ORP_ID_PROC_NAME` | VARCHAR |  | The name of the surgical procedure record. |
| 4 | `DX_LATERALITY_C_NAME` | VARCHAR | org | Laterality for the corresponding procedure in the diagnosis information |
| 5 | `DX_PRIMARY_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 6 | `DX_PROC_PANEL` | INTEGER |  | The panel to which this procedure belongs |
| 7 | `DX_CPT_CODE_2_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 8 | `DX_CPT_CODE_3_ID_PROC_NAME` | VARCHAR |  | The name of each procedure. |
| 9 | `DX_QTY` | INTEGER |  | The quantity for this procedure-diagnosis combination. |
| 10 | `DX_PROC_TYPE_C_NAME` | VARCHAR | org | The procedure type for this diagnosis |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

