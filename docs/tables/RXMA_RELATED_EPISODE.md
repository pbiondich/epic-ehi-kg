# RXMA_RELATED_EPISODE

> Medication access items linking to an ongoing monitoring episode for the therapy.

**Primary key:** `SUMMARY_BLOCK_ID`  
**Columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `EPISODE_CLASS_HOME_CARE_TYPE_C_NAME` | VARCHAR |  | Episode class for the linked clinical program or service |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

