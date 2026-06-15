# FCC_SCORE_AUDIT

> This table can be used to recreate an audit trail for Facility Charge Calculator scores that were modified. Since old scores are saved into these items, a row isn't exactly a snapshot of the scores and user at that particular instant listed. Instead, a snapshot is created by pairing a row's user and instant to the scores of the next row. If it is the last row with that rule, the user and instant apply to the current scores in FAC_CHG_OVERRIDES.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | The unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `CALCULATED_TOTAL_SCORE` | INTEGER |  | The audit item for the calculated score in FAC_CHG_OVERRIDE. Whenever facility charge calculator items change, a new row is added to this item. If those changes include the calculated score, this item saves the original value. If it hasn't changed, the current value is saved to this item. |
| 6 | `OVERRIDE_TOTAL_SCORE` | INTEGER |  | The audit item for the override score in FAC_CHG_OVERRIDE. Whenever facility charge calculator items change, a new row is added to this item. If those changes include the override score, this item saves the original value. If it hasn't changed, the current value is saved to this item. |
| 7 | `EDIT_USER_ID` | VARCHAR |  | Facility Charge Calculator audit item. Whenever Facility Charge Calculator items change, a new line is added to this item, and this item records the current user's ID. |
| 8 | `EDIT_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 9 | `EDIT_UTC_DTTM` | DATETIME (UTC) |  | The instant of each set of facility charge calculator changes. Whenever Facility charge calculator items change, this item records the current instant on a new row, or the value of the override instant in FAC_CHG_OVERRIDE if available. |
| 10 | `AUTO_FILED_YN` | VARCHAR |  | The audit item for auto-filed scores in FAC_CHG_OVERRIDE. Whenever facility charge calculator items change, a new row is added to this item. If those changes include the "Auto Filed" item, the original value is stored in this item. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

