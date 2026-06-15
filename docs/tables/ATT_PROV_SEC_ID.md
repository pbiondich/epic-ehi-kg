# ATT_PROV_SEC_ID

> All values associated with a claim are stored in the Claim External Value record. The ATT_PROV_SEC_ID table holds secondary (legacy) identifiers for the attending provider.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `ATT_PROV_SEC_QUAL` | VARCHAR |  | This item holds a qualifier describing additional IDs used to identify the attending provider. |
| 4 | `ATT_PROV_SEC_ID` | VARCHAR |  | This item holds additional IDs for the attending provider. |
| 5 | `ATT_PROV_SEC_QUAL_OID` | VARCHAR |  | The ID for the list of possible attending provider ID types. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

