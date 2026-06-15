# REI_CYCLE_PAT_COMMENTS

> Stores a patient's fertility cycle-level comment. Each line corresponds to a patient and an update to the comment.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | Cycle ID of the cycle that this comment belongs to. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CYCLE_COMMENT_PAT_ID` | VARCHAR | FK→ | Stores the patient ID of the patient that the comment is for. |
| 4 | `CYCLE_COMMENT_VALUE` | VARCHAR |  | Stores the value of the saved cycle comment. Cycle comments are limited to 4000 characters. |
| 5 | `CYCLE_COMMENT_UTC_DTTM` | DATETIME (UTC) |  | Instant in which the cycle comment was added or updated. |
| 6 | `CYCLE_COMMENT_USER_ID` | VARCHAR |  | User ID of the provider that added or updated the cycle comment. |
| 7 | `CYCLE_COMMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `COMMENT_IS_LATEST_YN` | VARCHAR |  | Stores whether this line is the latest cycle comment for this patient. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `CYCLE_COMMENT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

