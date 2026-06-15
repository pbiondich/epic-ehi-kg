# ORDER_MYC_RELEASE

> When a clinician (or interface) releases/unreleases a lab result to/from a web based chart system patient, tracking data for that action is stored in this table.

**Primary key:** `ORDER_PROC_ID`, `LINE`  
**Columns:** 6

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_PROC_ID` | NUMERIC | PK FK→ | The unique ID of the procedure order record that is released/unreleased. |
| 2 | `LINE` | INTEGER | PK | Since an order can be released/unreleased multiple times, the line number identifies a particular release instance. |
| 3 | `RELEASE_USER_ID` | VARCHAR |  | The ID of the Hyperspace user who released/unreleased the lab result to the web based chart system patient. |
| 4 | `RELEASE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `RELEASE_ACTION_C_NAME` | VARCHAR |  | This item indicates the action taken on the lab result. The data stored is a category value. 1 corresponds to Released. 2 corresponds to Unreleased. A null value also corresponds to Unreleased. |
| 6 | `MYC_REL_UTC_DTTM` | DATETIME (UTC) |  | Contains the instant when a result was released to MyChart in UTC. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_PROC_ID` | [ORDER_PROC](ORDER_PROC.md) | name_stem | high |

