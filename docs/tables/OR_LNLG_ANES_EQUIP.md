# OR_LNLG_ANES_EQUIP

> This table contains the Anesthesia Equipment Information for the Surgical Log (ORL).

**Primary key:** `RECORD_ID`  
**Columns:** 3  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `ANESTH_EQUIP_TYPE_NAME` | VARCHAR | org | The anesthesia equipment type. |
| 3 | `ANESTH_EQUIP_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

