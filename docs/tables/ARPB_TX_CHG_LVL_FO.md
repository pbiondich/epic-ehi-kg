# ARPB_TX_CHG_LVL_FO

> Transaction charge level filing order information.

**Primary key:** `TX_ID`, `CHARGE_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique identifier for the transaction record. |
| 2 | `CHARGE_LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CHG_LVL_FO_CVG_ID` | NUMERIC |  | This item stores the charge level filing order coverage |
| 4 | `CHG_LVL_FO_EXP_PMT` | NUMERIC |  | This item stores the charge level filing order expected payment |
| 5 | `CHG_LVL_FO_AUTH_NUM` | VARCHAR |  | This item stores the charge level filing order authorization number |
| 6 | `CHG_LVL_FO_WO_AMT` | NUMERIC |  | This item stores the charge level filing order write-off amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

