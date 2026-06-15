# AUDIT_ORD_RXNOADD

> This table provides general information on changes to specified no-add items in the order (ORD) master file. The detail item information is saved in AUDIT_ORD_RXITEMS table.

**Primary key:** `ORDER_MED_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `LINE` | INTEGER | PK | The line number for each change. |
| 3 | `AUDIT_EMP_USER_ID` | VARCHAR |  | The unique user ID who made the change. |
| 4 | `AUDIT_EMP_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `AUDIT_UPDATE_INST` | DATETIME (Local) |  | The instant of change. |
| 6 | `AUDIT_UPD_COMMENT` | VARCHAR |  | The comment for the change. |
| 7 | `AUDIT_ACTION_C_NAME` | VARCHAR |  | The action category to cause the change. |
| 8 | `AUDIT_OTX_PASS_NUM` | INTEGER |  | This item records the number of the order transmittal pass. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

