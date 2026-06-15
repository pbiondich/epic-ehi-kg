# PAT_ENC_COMM_ORDER

> This table extracts the related multiple response Encounter Communication Order - Order ID (I EPT 19791) item, which stores the orders that communications are waiting for.

**Primary key:** `PAT_ENC_CSN_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with the communication record. Together with COMM_JOB_ID, this forms the foreign key to the PAT_ENC_COMM_WAIT table. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple orders to wait for before sending that are associated with the communication from the PAT_ENC_COMM_WAIT table. |
| 4 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 5 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 6 | `COMM_ORD_ID` | NUMERIC |  | The order IDs of the orders that were selected in Communication Management to wait for before sending the communication. |
| 7 | `COMM_JOB_ID` | VARCHAR |  | The job ID of communications that are waiting for results. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

