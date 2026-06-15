# DEFAULT_PAYOR_PLAN

> This table contains documentation about the default payor plan. It contains the default payor ID and the default list of benefit plans for a patient. The items that this table extracts are used in the standalone Ambulatory EMR.

**Primary key:** `PAT_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ID` | VARCHAR | PK FK→ | The unique ID of the patient record for this row. This column is frequently used to link to the PATIENT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DEFAULT_PAYOR_ID_PAYOR_NAME` | VARCHAR |  | The name of the payor. |
| 4 | `DEFAULT_PLAN_ID_BENEFIT_PLAN_NAME` | VARCHAR |  | The name of the benefit plan record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

