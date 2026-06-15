# HSP_BDC_WO_ADJ_TX

> This table contains write-off adjustment information for Denial/Correspondence (BDC) records.

**Primary key:** `BDC_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BDC_ID` | NUMERIC | PK FK→ | This column stores the unique identifier for the denial or correspondence record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `WRITE_OFF_ADJ_TX_ID` | NUMERIC |  | This column stores the hospital write-off adjustment transactions posted onto this denial record. Write-off adjustments posted onto a bucket with an open denial record on it will be linked here from this denial record and the total amount of these adjustments will be calculated by the system and put into the item Write-off Amount-System of this denial record. |
| 4 | `WRITE_OFF_ADJ_AMT` | NUMERIC |  | The amount of the corresponding write off adjustment posted onto this denial record. |
| 5 | `PB_WRITE_OFF_ADJ_TX_ID` | NUMERIC |  | This column stores the professional billing non-contractual insurance adjustment transactions posted onto this denial record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `BDC_ID` | [BDC_INFO](BDC_INFO.md) | sole_pk | high |

