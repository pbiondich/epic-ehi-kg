# CL_LNK_CONTACT

> This table contains the overtime single items in the Linked Order Groups (LNK) master file.

**Primary key:** `LNK_ID`, `CONTACT_DATE_REAL`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `LNK_ID` | NUMERIC | PK FK→ | The unique ID for the linked order group. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 4 | `CONTACT_SERIAL_NUM` | NUMERIC | shared | The unique contact serial number (CSN) of the linked order group contact. |
| 5 | `CONTACT_NUM` | INTEGER |  | The contact number in the linked order group record. |
| 6 | `CNCT_TYPE_C_NAME` | VARCHAR |  | The contact type category ID for the linked order group record, which describes the action taken on the linked order group. |
| 7 | `INST_OF_ENTRY_TM` | DATETIME (Local) |  | The last instant this linked order group record was edited. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `LNK_ID` | [CL_LNK_ORDERS](CL_LNK_ORDERS.md) | sole_pk | high |

