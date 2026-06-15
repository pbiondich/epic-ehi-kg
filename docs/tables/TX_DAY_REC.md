# TX_DAY_REC

> This table contains a history of all reconcilable changes made to orders in a treatment day, as well as how the user reconciled those changes. For example, if a medication order was discontinued, the discontinuation would appear in this table, as well as any actions taken on that modification (such as acknowledging it, or removing the order from future days).

**Primary key:** `EVENT_ID`, `LINE`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `EVENT_ID` | VARCHAR | PK FK→ | The unique identifier for the event record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `TX_REC_OTP_ID` | NUMERIC |  | This item contains the ID of the order template that this action refers to. |
| 4 | `TX_REC_ORD_ID` | NUMERIC |  | This item contains the ID of the order that this action refers to. |
| 5 | `TX_REC_EVENT_LINE` | NUMERIC |  | This item contains the line number of the event where this action occurred. This corresponds to the LINE column in the table ED_IEV_EVENT_INFO. |
| 6 | `TX_REC_CHANGE_TYP_C_NAME` | VARCHAR |  | This item contains the type of change documented on this line. |
| 7 | `TX_REC_RVW_BY_LINE` | NUMERIC |  | This item contains the line number of the action that reviewed this action. |
| 8 | `TX_REC_REVIEW_CMT` | VARCHAR |  | For review actions, this item contains the comment entered by the user during the review process. |
| 9 | `TX_REC_OLD_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 10 | `TX_REC_NEW_ERX_ID_MEDICATION_NAME` | VARCHAR |  | The name of this medication record. |
| 11 | `TX_REC_MESSAGE` | VARCHAR |  | For treatment plan reconciliation events, will hold the reconciliation message |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `EVENT_ID` | [EVENT](EVENT.md) | name_stem | high |

