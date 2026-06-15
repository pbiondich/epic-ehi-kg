# MC_PRICER_DRG

> This table contains DRG grouping information returned by the Epic Pricer.

**Primary key:** `PRICER_MSG_ID`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PRICER_MSG_ID` | NUMERIC | PK shared | The unique identifier for the Epic Pricer message record. |
| 2 | `DRG_FINAL_DRG` | VARCHAR |  | The calculated DRG code returned by the Epic Pricer DRG grouping. |
| 3 | `DRG_FINAL_DIAG` | VARCHAR |  | The calculated diagnostic category returned by the Epic Pricer DRG grouping. |
| 4 | `DRG_RETURN_CODE_C_NAME` | VARCHAR |  | The return code from the Epic Pricer DRG grouping calculation. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

