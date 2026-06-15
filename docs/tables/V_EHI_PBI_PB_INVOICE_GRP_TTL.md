# V_EHI_PBI_PB_INVOICE_GRP_TTL

> This view filters out invoice data that is not appropriate for member level EHI exports when group billing is used.

**Primary key:** `PB_INVC_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PB_INVC_ID` | VARCHAR | PK FK→ | The unique ID of the premium billing invoice. |
| 2 | `LINE` | INTEGER | PK | Line counter for the group on the invoice. |
| 3 | `PLAN_GRP_ID` | VARCHAR | FK→ | The unique ID of the employer group associated with the invoice. |
| 4 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 5 | `GROUP_TOTAL` | NUMERIC |  | Total amount for the group on the invoice. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PB_INVC_ID` | [PB_INVOICE](PB_INVOICE.md) | sole_pk | high |
| `PLAN_GRP_ID` | [PLAN_GRP](PLAN_GRP.md) | sole_pk | high |

