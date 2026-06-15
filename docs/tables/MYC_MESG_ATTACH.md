# MYC_MESG_ATTACH

> This table stores information on files which have been attached to web based chart system (WMG) messages.

**Primary key:** `MESSAGE_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MESSAGE_ID` | VARCHAR | PK FK→ | The unique ID used to identify a web based chart system message record. |
| 2 | `LINE` | INTEGER | PK | The line number used to identify each row of read data associated with an individual web based chart system message record. |
| 3 | `DOC_ID` | VARCHAR |  | This item contains the IDs of the documents attached to this message. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `MESSAGE_ID` | [MYC_MESG](MYC_MESG.md) | sole_pk | high |

