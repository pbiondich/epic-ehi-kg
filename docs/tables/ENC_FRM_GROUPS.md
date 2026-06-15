# ENC_FRM_GROUPS

> This table holds the list of Form Groups that were used in this patient contact. The table holds ID and Chronicles Date (DAT) pointers to these Form Groups (from the LFG master file) because they are storing the version of that Form Group that was in use when this patient contact occurred.

**Primary key:** `PAT_ENC_CSN_ID`, `LINE`  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `PAT_ENC_CSN_ID` | NUMERIC | PK FK→ | This is the unique contact serial number for this contact. This number is unique across all patient encounters in your system. If you use IntraConnect, this is the Unique Contact Identifier (UCI). |
| 2 | `LINE` | INTEGER | PK | This is the line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 3 | `PAT_ENC_DATE_REAL` | FLOAT |  | This is a unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 4 | `CONTACT_DATE` | DATETIME |  | This is the date of this contact in calendar format. |
| 5 | `CM_CT_OWNER_ID` | VARCHAR |  | This is the Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |
| 6 | `FRM_GROUP_IDS` | NUMERIC |  | To maintain an accurate history of the forms that were used to document on this patient encounter, this item holds a list of record IDs for the Form Group master file. |
| 7 | `FRM_GROUP_IDS_RECORD_NAME` | VARCHAR |  | Stores the form group record name. |
| 8 | `FRM_GROUP_DATS` | VARCHAR |  | To maintain an accurate history of the forms and versions of forms that were used to document on this patient encounter, this item holds a list of contact dates (DATs) that, together with column FRM_GROUP_IDS, point to the Form Groups master file. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | name_stem | high |

