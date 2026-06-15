# OTHER_PROV

> All values associated with a claim are stored in the Claim External Value record. The OTHER_PROV table holds other provider values set by the system during claims processing or by user edits. These values are only filled for paper UB claims.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PPR_OTH_NAM_LAST` | VARCHAR |  | This item holds the other provider's last name. |
| 4 | `PPR_OTH_NAM_FIRST` | VARCHAR |  | This item holds the other provider's first name. |
| 5 | `PPR_OTH_NAM_MID` | VARCHAR |  | This item holds the other provider's middle name. |
| 6 | `PPR_OTH_NAM_SUF` | VARCHAR |  | This item holds the suffix to the other provider's name (Jr, III, etc). |
| 7 | `PPR_OTH_NPI` | VARCHAR |  | This item holds the other provider's National Provider ID (NPI). |
| 8 | `PPR_OTH_SEC_QUAL` | VARCHAR |  | This item holds a qualifier describing additional ID used to identify the other provider. |
| 9 | `PPR_OTH_SEC_ID` | VARCHAR |  | This item holds an additional ID for the other provider. |
| 10 | `PPR_OTH_TYP_QUAL` | VARCHAR |  | This item holds the other provider's provider type qualifier. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

