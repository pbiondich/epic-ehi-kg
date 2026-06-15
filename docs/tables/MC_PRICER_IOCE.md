# MC_PRICER_IOCE

> Data returned from IOCE Editor.

**Primary key:** `PRICER_MSG_ID`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `IOCE_RTN_CODE_C_NAME` | VARCHAR |  | IOCE return code. |
| 3 | `IOCE_PROCESSD_C_NAME` | VARCHAR |  | IOCE processed flag. |
| 4 | `IOCE_CLM_DISP_C_NAME` | VARCHAR |  | IOCE claim disposition. |
| 5 | `IOCE_PAY_APC` | VARCHAR |  | IOCE payment APC. |
| 6 | `IOCE_STATUS_IND_C_NAME` | VARCHAR |  | IOCE status indicator. |
| 7 | `IOCE_PAYMENT_IND_C_NAME` | VARCHAR |  | IOCE payment indicator. |
| 8 | `IOCE_DISC_FLAG_C_NAME` | VARCHAR |  | IOCE discount flag. |
| 9 | `IOCE_DENY_REJECT_C_NAME` | VARCHAR |  | IOCE Deny or Reject flag. |
| 10 | `IOCE_PAYMENT_ADJ_FLAG_C_NAME` | VARCHAR |  | IOCE payment adjustment flag returned from IOCE. The released values are extracted from CMS code and ultimately owned by CMS. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

