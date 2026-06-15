# HH_MED_ORD_POC_STATUS

> The status of whether the medication order is on the Plan of Care.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `EDIT_INST_DTTM` | DATETIME (UTC) |  | Stores the instant the plan of care flag was updated |
| 4 | `ON_PLAN_OF_CARE_YN` | VARCHAR |  | Stores whether the medication order is on the Plan of Care as of the related instant. |
| 5 | `PAT_ENC_CSN_ID` | NUMERIC | FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 6 | `USER_ID` | VARCHAR | FK→ | The unique ID associated with the user record for this row. This column is frequently used to link to the CLARITY_EMP table. |
| 7 | `USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |
| `USER_ID` | [CLARITY_EMP](CLARITY_EMP.md) | sole_pk | high |

