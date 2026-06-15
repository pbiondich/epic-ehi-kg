# DISCRETE_PAT_INSTRUCTIONS

> This table contains the insulin treatment instructions for patients.

**Primary key:** `DISCRETE_PAT_INSTR_ID`  
**Columns:** 5  
**Joined by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DISCRETE_PAT_INSTR_ID` | NUMERIC | PK | The unique identifier (.1 item) for the instructions name record. |
| 2 | `RECORD_STATUS_C_NAME` | VARCHAR |  | Stores the record status (hidden, soft-deleted, etc...) |
| 3 | `PAT_ID` | VARCHAR | FK→ | Stores the patient ID |
| 4 | `DISCRETE_PAT_INSTR_TYPE_C_NAME` | VARCHAR |  | The type of patient instructions stored in this record |
| 5 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (3)

| From | Column | Confidence |
|------|--------|------------|
| [DISCRETE_PAT_INSTR_CMT](DISCRETE_PAT_INSTR_CMT.md) | `DISCRETE_PAT_INSTR_ID` | high |
| [DISCRETE_PAT_INSTR_EDIT](DISCRETE_PAT_INSTR_EDIT.md) | `DISCRETE_PAT_INSTR_ID` | high |
| [INSULIN_INSTRUCTIONS](INSULIN_INSTRUCTIONS.md) | `DISCRETE_PAT_INSTR_ID` | high |

