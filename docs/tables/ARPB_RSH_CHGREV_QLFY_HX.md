# ARPB_RSH_CHGREV_QLFY_HX

> This table holds all of the research billing review timestamps and times that the charge qualified for research billing review.

**Primary key:** `TX_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TX_ID` | NUMERIC | PK shared | This column stores the unique identifier for the professional billing transaction record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RSH_REV_DTTM` | DATETIME (UTC) |  | This item stores the instant research charge review was performed. |
| 4 | `RSH_REV_USER_ID` | VARCHAR |  | This item stores the user who performed research charge review. |
| 5 | `RSH_REV_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 6 | `REV_RESEARCH_ID_RESEARCH_STUDY_NAME` | VARCHAR |  | The name of the research study record. |
| 7 | `RSH_REV_NOTE_ID` | VARCHAR |  | This item stores a research charge review comment. |
| 8 | `RSH_REV_TYPE_C_NAME` | VARCHAR |  | This item stores a research charge review user type. |
| 9 | `RSH_REV_EXPIRE_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant research charge review expired and re-review is needed in Coordinated Universal Time (UTC). |
| 10 | `RSH_REV_QLFY_UTC_DTTM` | DATETIME (UTC) |  | This item stores the instant research charge review is needed in Coordinated Universal Time (UTC). |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

