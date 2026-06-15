# GOAL_OUTCOME_CNCT

> This table contains care plan goal records that have goal outcome documentation for a particular encounter.

**Primary key:** `GOAL_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `GOAL_ID` | VARCHAR | PK FK→ | The unique ID for the goal record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CP_IGO_OC_EPTCSN_N` | NUMERIC |  | The unique contact serial number for the encounter where the care plan goal outcome was documented. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 4 | `IP_CP_GOAL_OC_DAT` | NUMERIC |  | The contact date (DAT) for the encounter where the care plan goal outcome was documented. |
| 5 | `VISIT_NOTE_ID` | VARCHAR |  | Links to the note (HNO) record that stores the Home Health and Hospice goal visit note. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `GOAL_ID` | [GOAL](GOAL.md) | name_stem | high |

