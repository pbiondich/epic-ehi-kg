# INV_NUM_TX_PIECES

> Each line in this table corresponds to a transaction (ETR) composing a line on an invoice from item INV 381. Each line can contain a comma-delimited list of transactions composing a claim line. When a transaction is bundled, data will be split out to its own line via the TX_PIECE column. This table is used as a bridge between transaction- and invoice- based tables.

**Primary key:** `INV_ID`, `LINE`, `TX_PIECE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `INV_ID` | NUMERIC | PK | This column contains the internal invoice ID. |
| 2 | `LINE` | INTEGER | PK | This column contains the line number for any multiple-response item. |
| 3 | `TX_PIECE` | INTEGER | PK | This column contains the position of the transaction ID in the comma-delimited list of ETR ID's for a given line of INV-381. For example, if a certain line of INV-381 has three transactions, then TX_PIECE will contain 1, 2, and 3 for that line. |
| 4 | `TX_ID` | NUMERIC | shared | This column contains each individual transaction ID from the list of ETR ID's stored on each line of INV-381. So, if a given line of INV-381 has more than one transaction (separated by a comma-delimited list), then each ETR ID will appear on a separate row of the extract table. In other words, one and only one ETR ID will appear in each row of the TX_ID column. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

