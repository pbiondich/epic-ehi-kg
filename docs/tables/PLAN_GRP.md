# PLAN_GRP

> The PLAN_GRP table contains information about your employer groups. An employer group is a unit of a corporation or company made up of employees who share the same benefit plan.

**Primary key:** `PLAN_GRP_ID`  
**Columns:** 3  
**Joined by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PLAN_GRP_ID` | VARCHAR | PK | The unique ID assigned to the employer group. |
| 2 | `PLAN_GRP_ID_PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |
| 3 | `PLAN_GRP_NAME` | VARCHAR |  | The name of the employer group record |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (8)

| From | Column | Confidence |
|------|--------|------------|
| [ACCUM_GRP_GENERAL](ACCUM_GRP_GENERAL.md) | `PLAN_GRP_ID` | high |
| [CAP_PAYMENT](CAP_PAYMENT.md) | `PLAN_GRP_ID` | high |
| [CAP_PAY_REPL](CAP_PAY_REPL.md) | `PLAN_GRP_ID` | high |
| [COVERAGE](COVERAGE.md) | `PLAN_GRP_ID` | high |
| [LCI_CONTACT_DATA](LCI_CONTACT_DATA.md) | `PLAN_GRP_ID` | high |
| [PB_ACCT_TX_PLN_GRP](PB_ACCT_TX_PLN_GRP.md) | `PLAN_GRP_ID` | high |
| [PB_TX_SET_PLAN_GRP](PB_TX_SET_PLAN_GRP.md) | `PLAN_GRP_ID` | high |
| [V_EHI_PBI_PB_INVOICE_GRP_TTL](V_EHI_PBI_PB_INVOICE_GRP_TTL.md) | `PLAN_GRP_ID` | high |

