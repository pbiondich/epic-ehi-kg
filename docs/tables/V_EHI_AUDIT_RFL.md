# V_EHI_AUDIT_RFL

> This view contains one row for each audited item changed on a referral record that corresponds to a column that is configured for EHI export.

**Primary key:** `REFERRAL_ID`, `LINE`, `VALUE_LINE`  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REFERRAL_ID` | NUMERIC | PK FK→ | The ID for the referral record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HX_USER_ID` | VARCHAR |  | The user tied to the audited action on the referral. |
| 4 | `HX_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 6 | `ACTION_UTC_DTTM` | DATETIME (UTC) |  | Store the UTC instant when an action took place. |
| 7 | `ITEM_CHANGE_LN` | INTEGER |  | The item line that was added or changed. |
| 8 | `ITEM_CHANGE_POS` | INTEGER |  | The item position that was added or changed. |
| 9 | `OLD_VALUE_INTERNAL` | VARCHAR |  | The previously stored value for an item change, as defined by the item changed value in RFL_HX_ITEM_CHANGE.ITEM_CHANGE. If you use IntraConnect, this is the CID of the previously stored value. |
| 10 | `OLD_VALUE_EXTERNAL` | VARCHAR |  | The previously stored value for an item change, as defined by the item changed value in RFL_HX_ITEM_CHANGE.ITEM_CHANGE, in an external format. This column shows the translated external value as of when the column was last extracted. |
| 11 | `NEW_VALUE_INTERNAL` | VARCHAR |  | The new stored value for an item change, as defined by the item changed value in RFL_HX_ITEM_CHANGE.ITEM_CHANGE. If you use IntraConnect, this is the CID of the new stored value. |
| 12 | `NEW_VALUE_EXTERNAL` | VARCHAR |  | The new stored value for an item change, as defined by the item changed value in RFL_HX_ITEM_CHANGE.ITEM_CHANGE, in an external format. This column shows the translated external value as of when the column was last extracted. |
| 13 | `CHANGED_DATA_ELEMENT` | VARCHAR |  | The column descriptor that contains the metadata to be associated with data stored in columns OLD_VALUE_INTERNAL and NEW_VALUE_INTERNAL |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `REFERRAL_ID` | [REFERRAL](REFERRAL.md) | name_stem | high |

