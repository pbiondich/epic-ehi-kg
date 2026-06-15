# ARPB_CHKIN_RFD_RSN

> The ARPB_CHKIN_RFD_RSN table contains information concerning the refund reason and comment for a refund performed at check-in/out. This table will only have data if your site has both Professional Billing and Scheduling applications.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | The unique key or identification number for a given refund transaction from check-in. |
| 2 | `LINE` | INTEGER | PK | The number used to identify a specific row of information in this table. It is used to associate various pieces of information from other sources of data to each row of this table. |
| 3 | `AR_REFUND_REASON_C_NAME` | VARCHAR | org | The AR refund reason code. |
| 4 | `AR_REFUND_CMT` | VARCHAR |  | The accounts receivable (AR) check-in refund comment. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

