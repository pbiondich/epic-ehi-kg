# ORD_CV_FINDING

> This table contains information about a single finding.

**Primary key:** `CV_FINDING_ID`  
**Columns:** 14  
**Org-specific columns:** 4  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CV_FINDING_ID` | NUMERIC | PK | The unique identifier for the finding record. |
| 2 | `FORM_DATE_REAL` | FLOAT |  | The contact date real (DTE) of the associated contact in the Forms (LQF) master file. This is a unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `WALL_STAGE` | INTEGER |  | The stage number for wall motion scoring. |
| 4 | `WALL_SCORE` | NUMERIC |  | The average of the wall motion scoring. |
| 5 | `WALL_NORMAL` | NUMERIC |  | The normal index of the wall motion scoring. |
| 6 | `WALL_MOTION_VIEW_C_NAME` | VARCHAR | org | The wall motion views select category ID for the finding record. |
| 7 | `FINDING_SEQUENCE` | NUMERIC |  | Defines a relative order among result records (RES) in a report segment. For instance, a record with a value of 5 in this item will appear earlier in the report segment than a record with a value of 7 in this item. |
| 8 | `EP_TYPE_C_NAME` | VARCHAR | org | The category number for the electrophysiology finding type. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 9 | `ENDOSCOPY_TYPE_C_NAME` | VARCHAR | org | The category number for the endoscopy finding type. This is usually the same as the internal ID. If you use IntraConnect, this is the Community ID (CID). |
| 10 | `SEC_FORM_ID` | VARCHAR |  | The unique identifier for the secondary SmartForm associated with the finding record. |
| 11 | `SEC_FORM_ID_FORM_NAME` | VARCHAR |  | The name of the form associated with the questionnaire. |
| 12 | `SEC_FORM_DATE_REAL` | FLOAT |  | The contact date real (DTE) of the associated contact of the secondary SmartForm. This is a unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 13 | `INTVN_BIFURC_TECHNIQUE_C_NAME` | VARCHAR | org | This item is used to store the technique used in the bifurcation of an intervention. |
| 14 | `HEMO_DATASET_FORM_COMP_ID_NESTCOMP_NAME` | VARCHAR |  | The record name for the component. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [ORD_CV_F_TEXT](ORD_CV_F_TEXT.md) | `CV_FINDING_ID` | high |
| [ORD_CV_F_WALL_MOTN](ORD_CV_F_WALL_MOTN.md) | `CV_FINDING_ID` | high |
| [ORD_FINDINGS](ORD_FINDINGS.md) | `CV_FINDING_ID` | high |

