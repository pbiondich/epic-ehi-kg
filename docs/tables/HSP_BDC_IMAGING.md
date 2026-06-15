# HSP_BDC_IMAGING

> This table contains related imaging information for the Denial/Correspondence (BDC) master file.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 6  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record the related imaging information is associated with. |
| 2 | `LINE` | INTEGER | PK | Line number of related imaging information that is being extracted by enterprise reporting. |
| 3 | `BDC_IMAGE_MNE_C_NAME` | VARCHAR | org | The image mnemonic associated with this group of related denial/correspondence imaging information. |
| 4 | `IMAGE_KEY` | VARCHAR |  | The image key associated with this group of related denial/correspondence imaging information. |
| 5 | `IMAGE_PAGE_NUMBER` | VARCHAR |  | The image page number associated with this group of related denial/correspondence imaging information. |
| 6 | `BDC_PB_IMG_MNE_C_NAME` | VARCHAR | org | This column stores the professional billing image mnemonic that may be associated with this group of related correspondence imaging information. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

