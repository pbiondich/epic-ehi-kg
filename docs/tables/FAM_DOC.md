# FAM_DOC

> This table stores data for a family document.

**Primary key:** `FAM_DOC_ID`  
**Columns:** 7  
**Org-specific columns:** 1  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `FAM_DOC_ID` | NUMERIC | PK | The unique identifier (.1 item) for the family document record. |
| 2 | `FAM_DOC_NAME` | VARCHAR |  | The name of the family document. |
| 3 | `LINKED_FAMILY_ID` | NUMERIC |  | The unique ID of the family for which the family document was created. |
| 4 | `ATTRIBUTED_TO_DATE` | DATETIME |  | The attributed to date for this family document. |
| 5 | `ATTRIBUTED_TO_USER_ID` | VARCHAR |  | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 6 | `ATTRIBUTED_TO_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `FAM_DOC_STATUS_C_NAME` | VARCHAR | org | The status category ID of the family document. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [DOC_INFORMATION_3](DOC_INFORMATION_3.md) | `FAM_DOC_ID` | high |
| [FAM_DOC_GEN_AUD_TRL](FAM_DOC_GEN_AUD_TRL.md) | `FAM_DOC_ID` | high |
| [FAM_DOC_PATS](FAM_DOC_PATS.md) | `FAM_DOC_ID` | high |

