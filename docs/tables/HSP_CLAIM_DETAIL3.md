# HSP_CLAIM_DETAIL3

> This table contains detailed claim print record information for claims associated with the hospital liability bucket.

**Primary key:** `CLAIM_PRINT_ID`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the claim print record. |
| 2 | `CH_SENT_DATE` | DATETIME |  | This item holds the last reported date the claim was sent out of the clearinghouse. |
| 3 | `PAYER_RECEIVED_DATE` | DATETIME |  | This item holds the last reported date the payer received the claim. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

