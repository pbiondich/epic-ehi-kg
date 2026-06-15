# OR_LNLG_CDP

> This table contains the CDP information for the Surgical Log (ORL). CDP stands for Catheter, Drains, and Packings which has been replaced by LDAs (Lines, Drains, and Airways) post Summer 2009.

**Primary key:** `RECORD_ID`  
**Columns:** 14  
**Org-specific columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | VARCHAR | PK shared | The unique ID of the line record. |
| 2 | `CDP_TYPE_C_NAME` | VARCHAR | org | The category ID for the type of CDP for the surgical log. |
| 3 | `CDP_ACTION_C_NAME` | VARCHAR | org | The action taken on the catheter, drain, or packing (CDP). |
| 4 | `CDP_AREA_C_NAME` | VARCHAR | org | The category ID for the area in which the CDP was applied. |
| 5 | `CDP_SIZE` | NUMERIC |  | The size of the catheter, drain, or packing (CDP). |
| 6 | `CDP_REMOVAL_DATE` | DATETIME |  | The date the CDP was removed. |
| 7 | `CDP_NUM_USED` | INTEGER |  | The number of CDPs used. |
| 8 | `CDP_LATERALITY_C_NAME` | VARCHAR | org | The laterality of the CDP. |
| 9 | `CDP_AMOUNT` | NUMERIC |  | This column is a numeric value that stores the amount of CDPs. CDPs have been replaced by Lines, Drains, and Airways (LDAs) as of 2009. |
| 10 | `CDP_UNITS_C_NAME` | VARCHAR | org | The units of measure category number for the CDP. |
| 11 | `CDP_INV_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 12 | `CDP_CC_INFLATION` | NUMERIC |  | Stores the amount, in CCs, needed for inflation. |
| 13 | `CDP_DIFF_INSRT_YN` | VARCHAR |  | Stores whether insertion was difficult. |
| 14 | `CDP_URINE_RET_C_NAME` | VARCHAR | org | The category number for the urine returned. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

