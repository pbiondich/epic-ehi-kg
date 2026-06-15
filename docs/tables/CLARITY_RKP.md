# CLARITY_RKP

> The CLARITY_RKP table is the master table for risk panel information.

**Primary key:** `RKP_ID`  
**Columns:** 3  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RKP_ID` | VARCHAR | PK | The unique ID of the risk panel. |
| 2 | `RKP_ID_RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |
| 3 | `RISK_PANEL_NAME` | VARCHAR |  | The name of the risk panel. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [AP_CLAIM](AP_CLAIM.md) | `RKP_ID` | high |
| [CUST_SERVICE](CUST_SERVICE.md) | `RKP_ID` | high |
| [MEM_LIST_REPL](MEM_LIST_REPL.md) | `RKP_ID` | high |

