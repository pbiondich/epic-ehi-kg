# V_BIL_ALL

> This view contains all bill area records in the system, regardless of record type.

**Primary key:** `BILL_AREA_ID`  
**Columns:** 3  
**Joined by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `BILL_AREA_ID` | NUMERIC | PK | The unique identifier for the bill area, financial subdivision, or financial division. |
| 2 | `BILL_AREA_ID_BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |
| 3 | `BILL_AREA_NAME` | VARCHAR |  | The record name of this bill area, financial subdivision, or financial division. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (5)

| From | Column | Confidence |
|------|--------|------------|
| [ARPB_TRANSACTIONS](ARPB_TRANSACTIONS.md) | `BILL_AREA_ID` | high |
| [CLM_EDIT_WQ_CLM](CLM_EDIT_WQ_CLM.md) | `BILL_AREA_ID` | high |
| [INVOICE](INVOICE.md) | `BILL_AREA_ID` | high |
| [ORDER_PROC_5](ORDER_PROC_5.md) | `BILL_AREA_ID` | high |
| [PRE_AR_CHG](PRE_AR_CHG.md) | `BILL_AREA_ID` | high |

