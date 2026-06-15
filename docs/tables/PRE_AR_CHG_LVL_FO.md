# PRE_AR_CHG_LVL_FO

> Charge level filing order information. Note: temporary accounts receivable (TAR) records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `CHG_LVL_FO_LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the subject record. |
| 2 | `CHG_LVL_FO_LINE` | INTEGER | PK | Some charge lines may have charge line filing order. This field allows for each charge line filing order to be unique. |
| 3 | `CHG_LVL_FO_CHG_LINE` | INTEGER |  | This item stores the line number for the charge procedure which corresponds to this charge level filing order line. |
| 4 | `CHG_LVL_FO_CVG_ID` | NUMERIC |  | This item stores the charge level filing order coverage. |
| 5 | `CHG_LVL_FO_EXP_PMT` | NUMERIC |  | This item stores the charge level filing order expected payment. |
| 6 | `CHG_LVL_FO_WO_AMT` | NUMERIC |  | This item stores the charge level filing order write-off amount. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

