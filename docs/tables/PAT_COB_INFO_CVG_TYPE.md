# PAT_COB_INFO_CVG_TYPE

> The type of coverage stored on the Coordination of Benefits (COB) information in the patient record.

**Primary key:** `PAT_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The line number of the associated coordination of benefits coverage type in the patient's record. This forms the foreign key to the PAT_COB_INFO table. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number of the associated coordination of benefits coverage type in the patient's record. Together with PAT_ID, this forms the foreign key to the PAT_COB_INFO table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple coordination of benefits coverage types associated with the patient from the PAT_COB_INFO table. |
| 4 | `COB_INS_TYPE_C_NAME` | VARCHAR | org | Coordination of benefits insurance coverage types. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

