# TXP_CURRENT_MELD_PELD_HX

> This table contains the liver score history for a transplant episode. After 6/28/2022 exceptions will not be included due to changes in the OPTN liver allocation policy.

**Primary key:** `SUMMARY_BLOCK_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SUMMARY_BLOCK_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the episode record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CURRENT_SCORE` | INTEGER |  | The most advantageous active liver score. After 6/28/2022 exceptions will not be included due to changes in the OPTN liver allocation policy. |
| 4 | `CURRENT_STATUS_C_NAME` | VARCHAR |  | The status, when it is the most advantageous active liver score. |
| 5 | `CURRENT_SCORE_TYPE` | VARCHAR |  | The type of liver score that this line represents. That is, "MELD", "PELD" or "STATUS" |
| 6 | `CURRENT_EXCEPTION_C_NAME` | VARCHAR | org | The exception for this line. After 6/28/2022 exceptions will not be included due to changes in the OPTN liver allocation policy. |
| 7 | `CURRENT_START_DATE` | DATETIME |  | Start date of the associated score. |
| 8 | `CURRENT_END_DATE` | DATETIME |  | Expiration date of the associated score. |
| 9 | `CUR_EXCEPTION_OTHER` | VARCHAR |  | The other exception for the meld score. After 6/28/2022 exceptions will not be included due to changes in the OPTN liver allocation policy. |
| 10 | `SCORE_HISTORY_LINE` | INTEGER |  | Line in the HSB 30400 related group corresponding to this line in score history |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

