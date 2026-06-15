# LN_CAS_CEV_ID

> This table holds a link to the claim value records that hold the claim adjustment reason code information for the service lines. A separate reason code record will exist for each combination of other coverage and service line.

**Primary key:** `RECORD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `LN_CAS_CEV_ID` | NUMERIC |  | This item holds a pointer to an additional claim external value (CEV) record used to hold reason code (CAS) information for the claim. Only line level values are stored in this reason code claim external value (CEV) record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

