# PCP_REF_PROV_SEC_ID

> All values associated with a claim are stored in the Claim External Value record. The PCP_REF_PROV_SEC_ID table holds secondary (legacy) identifiers for the PCP referring provider.

**Primary key:** `RECORD_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim value record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `PCP_REF_PROV_SEC_QUAL` | VARCHAR |  | This item holds a qualifier describing additional IDs used to identify the PCP referring provider. |
| 4 | `PCP_REF_PROV_SEC_IDENT` | VARCHAR |  | This item holds additional IDs for the PCP referring provider. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

