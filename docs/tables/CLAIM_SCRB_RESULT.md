# CLAIM_SCRB_RESULT

> Store claim scrubber information.

**Primary key:** `CLAIM_PRINT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_PRINT_ID` | NUMERIC | PK shared | The unique identifier for the Claim Info record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CLM_SCRB_ERR_MSG` | VARCHAR |  | Store claim scrubber error message. |
| 4 | `CLM_SCRB_ADJ_AMOUNT` | NUMERIC |  | Store claim scrubber adjusted amount. |
| 5 | `CLM_SCRB_FIX_TYPE_C_NAME` | VARCHAR |  | Store claim scrubber type of fix. |
| 6 | `CLM_SCRB_FIX_VALUE` | VARCHAR |  | Store claim scrubber fixed value. |
| 7 | `CLM_SCRB_ATFIX_YN` | VARCHAR |  | Store whether this was an auto fix. |
| 8 | `CLM_SCRB_ERR_LEVEL` | INTEGER |  | Store claim scrubber error level. |
| 9 | `CLM_SCRB_ACTION` | VARCHAR |  | Store claim scrubber action performed. |
| 10 | `CLM_SCRB_GROUP_C_NAME` | VARCHAR | org | Store claim scrubber group information. |
| 11 | `CLM_SCRB_EACTION_C_NAME` | VARCHAR |  | Store what action was performed by Epic. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

