# V_EHI_SMRTDTA_ELEM_VAL_EXT

> This view contains current values for SmartData elements, includes an external formatted value column, and an Electronic Health Information column descriptor column for values that reference records which can be used to join to tables with data related to that record.

**Primary key:** `HLV_ID`, `LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `HLV_ID` | NUMERIC | PK shared | The unique ID of the SmartData element value. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `SMRTDTA_ELEM_VALUE` | VARCHAR |  | The SmartData element value entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. If the value entered is a record ID or category value and you use IntraConnect, this is the Community ID (CID). Note: This column only extracts the first 3000 characters of data. |
| 4 | `SMRTDTA_ELEM_VALUE_EXTERNAL` | VARCHAR |  | The SmartData element value entered by a user through a SmartForm, SmartTool or other documentation tool that files discrete data to SmartData elements. This value is converted to an external format, depending on the value type. For database element category values, this column will contain the category title. For database element static record values, this will contain the record name as of value filing or initial extraction. For date values, this column will contain a date string in YYYY-MM-DD format. For time values, this column will contain a timestamp string in HH24:MM:SS format. For instant values this column will contain a string that uses both the aforementioned date and time formats. For all other value types this column will be NULL. |
| 5 | `COLUMN_DESCRIPTOR` | VARCHAR |  | The name of a column that can be used to join from a raw database-type networked record ID in the SMRTDTA_ELEM_VALUE column to the corresponding data table for that record type, specifically for use in the Electronic Health Information export process. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

