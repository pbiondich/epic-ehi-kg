# OR_LOG_PNDS_IND

> The OR_LOG_PNDS_IND table contains OR management system log PNDS indicator information.

**Primary key:** `LOG_ID`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LOG_ID` | VARCHAR | PK shared | The unique ID of the surgical log that the PNDS indicators refer to. |
| 2 | `LINE` | INTEGER | PK | The line number of the PNDS indicator in the log. |
| 3 | `PNDS_INDICATOR_ID` | VARCHAR |  | The unique ID of the PNDS indicator. |
| 4 | `PNDS_INDICATOR_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |
| 5 | `PNDS_IND_ACHVD_YN` | VARCHAR |  | Yes/no flag indicating whether or not this indicator was achieved. |
| 6 | `PNDS_IND_NOTES` | VARCHAR |  | Free text comments about the indicator. |
| 7 | `PNDS_IND_ADDED_YN` | VARCHAR |  | Yes/no flag indicating whether or not this indicator was added by a user. |
| 8 | `PNDS_IND_OUT_ID` | VARCHAR |  | The unique ID of the PNDS outcome associated with this indicator. |
| 9 | `PNDS_IND_OUT_ID_ELEMENT_NAME` | VARCHAR |  | The name of the PNDS record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

