# MYC_MESG_RCP_STAFF

> This table holds the In Basket Staff Recipients (I WMG 196) item, which is the final staff (EMP) recipients for this Patient Access Message (WMG) record.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID used to identify a web based chart system message record. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of read data associated with an individual web based chart system message record. |
| 3 | `IB_STAFF_RECIP_ID` | VARCHAR |  | This stores the user (EMP) ID of the final recipient of this message. |
| 4 | `IB_STAFF_RECIP_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

