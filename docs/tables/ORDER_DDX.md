# ORDER_DDX

> This table will allow reporting on the associated differential diagnosis entries for each medication on an encounter. Note that this is different than ORDER_DX_MED which contains the encounter diagnosis associations.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 8  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `ASSOC_DDX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |
| 4 | `ASSOC_DDX_DESC` | VARCHAR |  | Stores the free text description for the associated differential diagnosis. |
| 5 | `ASSOC_DDX_COMMENT` | VARCHAR |  | Stores the associated differential diagnosis comment. |
| 6 | `ASSOC_DDX_QUAL_C_NAME` | VARCHAR | org | Stores the ID of the qualifier associated with the diagnosis. |
| 7 | `ASSOC_DDX_CHRONI_YN` | VARCHAR |  | Indicates whether the associated diagnosis is chronic. |
| 8 | `ASSOC_DDX_STATUS_C_NAME` | VARCHAR |  | Stores the status of the associated differential diagnosis (e.g. In Progress, Final, etc.) |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

