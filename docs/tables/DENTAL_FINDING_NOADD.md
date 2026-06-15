# DENTAL_FINDING_NOADD

> This table contains the items for dental finding records.

**Primary key:** `FINDING_ID`  
**Columns:** 9  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FINDING_ID` | NUMERIC | PK shared | The unique identifier for the finding record |
| 2 | `DEN_TOO_FIND_TYPE_C_NAME` | VARCHAR |  | Indicates the type of finding, such as caries, fracture, etc. |
| 3 | `FINDING_STAT_NOAD_C_NAME` | VARCHAR |  | The current status the finding's status (unaddressed, resolved, removed, etc.) of the dental finding |
| 4 | `DENTAL_CARIES_CLS_C_NAME` | VARCHAR | org | Stores the caries classification of a caries finding |
| 5 | `DENTAL_CARIES_DEPTH` | NUMERIC |  | Stores the caries depth of a caries finding |
| 6 | `DENTAL_MOBI_CLASS_C_NAME` | VARCHAR | org | Stores information about the severity of mobility documented on a tooth. |
| 7 | `DENTAL_FURC_CLASS_C_NAME` | VARCHAR | org | Stores information about the severity of furcation documented on a tooth. |
| 8 | `DENT_CARIES_INCIP_C_NAME` | VARCHAR | org | This columns specifies the incipiency of a caries finding. |
| 9 | `DENT_FND_OVR_NAME` | VARCHAR |  | This item specifies the display name that will be used when users document a finding. If populated, this will be used in place of the finding type (I RES 17407) to describe the finding. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

