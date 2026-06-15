# DOCS_RCVD_MAPPING_MISC

> This table stores mapping information associated with discrete data received from outside sources. This table only contains types of mappings which are not in the tables specific to their data type.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `MAP_DATA_REF_ID` | VARCHAR |  | This item stores the data reference ID. |
| 6 | `MAP_DATA_TYPE_C_NAME` | VARCHAR |  | This item stores the mapping data type. |
| 7 | `MAP_CODE` | VARCHAR |  | This item stores the mapping code associated with the coding system to represent the data. |
| 8 | `MAP_CODING_SYSTEM` | VARCHAR |  | This item stores the mapping coding system associated with the code to represent the data. |
| 9 | `MAP_DISPLAY_NAME` | VARCHAR |  | The display name of the mapping code in its code system |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

