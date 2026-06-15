# ARPB_RSH_CHGREV_HX

> This table holds Research Charge Review stamps for PB transactions. When a user marks a PB transaction as reviewed from the Research Charge Review activity, a review stamp is added to the transaction. The stamp includes the instant of review, user reviewing, study reviewed for, the type of the review user and the ID of a note that contains a comment. A single charge line may have multiple such stamps, with different stamps on the same line being distinguished by the VALUE_LINE column.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the professional billing transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RSH_REV_USER_ID` | VARCHAR |  | This item stores the user who performed research charge review. |
| 4 | `RSH_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RSH_REV_COMMENT_ID` | VARCHAR |  | This item stores a research charge review comment, in the form of a note ID. |
| 6 | `REV_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

