# REI_DAILY_CYCLE_COMMENTS

> Stores daily cycle comment information.

**Primary key:** `CYCLE_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CYCLE_ID` | NUMERIC | PK FK→ | Cycle ID (ICF .1) of the cycle that this comment belongs to. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `COMMENT_DATE` | DATETIME (UTC) |  | The cycle date that this comment was added to. |
| 4 | `COMMENT_PAT_ID` | VARCHAR | FK→ | Stores the EPT ID of the patient that the comment is on. (Multiple patients can be linked to a single ICF) |
| 5 | `COMMENT_VALUE` | VARCHAR |  | Stores the value of the saved comment. Comments will be limited to a maximum of 500 characters. |
| 6 | `COMMENT_USER_ID` | VARCHAR |  | EMP ID of the provider that added/updated the comment. |
| 7 | `COMMENT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 8 | `COMMENT_INST_UTC_DTTM` | DATETIME (UTC) |  | Instant in which the comment was added/updated |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `COMMENT_PAT_ID` | [PATIENT](PATIENT.md) | alias_pat_id | low |
| `CYCLE_ID` | [INFERTILITY_CYCLE](INFERTILITY_CYCLE.md) | sole_pk | high |

