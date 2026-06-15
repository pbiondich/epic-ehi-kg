# V_EHI_AUDIT_ORD_RXITEMS

> This table provides information on changes to specified no-add items in the order (ORD) master file formatted for the EHI export.

**Primary key:** `ORDER_MED_ID`, `LINE`, `VALUE_LINE`, `CHANGED_DATA_ELEMENT`  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_MED_ID` | NUMERIC | PK FK→ | The unique ID of the medication order (prescription) record. NOTE: This is an internal unique identifier for ORD master file records in this table and cannot be used to link to CLARITY_MEDICATION. |
| 2 | `LINE` | INTEGER | PK | The line number for each change. |
| 3 | `VALUE_LINE` | INTEGER | PK | A value is needed. For multiple response item, it is the line number for each real data or 0 for total count line. For single response item, it is 1. |
| 4 | `AUDIT_LOCAL_DTTM` | DATETIME (Local) |  | The instant of change. |
| 5 | `OLD_VALUE_INTERNAL` | VARCHAR |  | For audited items which store a networked record ID, this column will extract the CID of the linked record in OLD_VALUE. For other items this will extract the same value as OLD_VALUE. |
| 6 | `NEW_VALUE_INTERNAL` | VARCHAR |  | For audited items which store a networked record ID, this column will extract the CID of the linked record in NEW_VALUE. For other items this will extract the same value as NEW_VALUE. |
| 7 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | The old value of the item in external format. Dates, categories, and networked items will display meaningful information instead of the internal value. |
| 8 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | The new value of the item in external format. Dates, categories, and networked items will display meaningful information instead of the internal value. |
| 9 | `CHANGED_DATA_ELEMENT` | VARCHAR | PK | The Clarity table and column which corresponds to the data which changed. |
| 10 | `CHANGE_USER_ID` | VARCHAR |  | The unique user ID who made the change. |
| 11 | `CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ORDER_MED_ID` | [ORDER_MED](ORDER_MED.md) | name_stem | high |

