# ASSIGNMENT_DATA_MSG_HX

> Table for holding historical AMS IDs for Assignment records.

**Primary key:** `ASGN_DATA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ASGN_DATA_ID` | NUMERIC | PK FK→ | The unique identifier (.1 item) for the assignment data record record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BLK_DTA_MESSAGE` | NUMERIC |  | The historical bulk data messages that created or updated this assignment record. |
| 4 | `BLK_DATA_MSG_TYPE_C_NAME` | VARCHAR |  | The type of message that impacted this ASN record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ASGN_DATA_ID` | [ASSIGNMENT_DATA](ASSIGNMENT_DATA.md) | sole_pk | high |

