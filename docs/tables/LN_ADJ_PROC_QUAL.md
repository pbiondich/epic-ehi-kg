# LN_ADJ_PROC_QUAL

> This table holds codes identifying the type of procedure codes reported on the line. The LN_ADJ_OTH_PYR_ID, LN_ADJ_AMT_PAID, LN_ADJ_PROC_QUAL, LN_ADJ_PROC_CD, LN_ADJ_PROC_DESC, LN_ADJ_PROC_MOD, LN_ADJ_QTY, LN_ADJ_BUND_LN_NUM, LN_ADJ_PMT_DT, LN_ADJ_REV_CD, LN_ADJ_PAT_DUE, and LN_ADJ_OTH_PYR_SEQ_CD tables are related to one another. The number of lines in these tables will always be the same and values on the same line in each table will correspond to one another.

**Primary key:** `RECORD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the claim values record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this contact. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this contact. |
| 4 | `LN_ADJ_PROC_QUAL` | VARCHAR |  | This item holds a code identifying the type of procedure code reported on the line. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

