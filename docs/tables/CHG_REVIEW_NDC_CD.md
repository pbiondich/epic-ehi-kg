# CHG_REVIEW_NDC_CD

> This table contains Medical National Drug Code (NDC) ID for a temporary accounts receivable (TAR) record that is or has been in a Charge Review workqueue. Because one procedure in a TAR record can be associated with multiple NDC codes, each row in this table represents one NDC ID and is identified by the transaction ID (TAR_ID), procedure line number (GROUP_LINE), and line number (VALUE_LINE). The data for this table is extracted using a KB_SQL query. Note: TAR records in Chronicles are purged periodically depending on your system setting. Be aware that old data in this table might be lost if you truncate the table.

**Primary key:** `TAR_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 5

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `TAR_ID` | NUMERIC | PK shared | The unique identifier for the subject record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple NDC associated with a specific group of data within this record. |
| 4 | `NDC_CODES_ID` | VARCHAR |  | Internal ID of Medical National Drug Code (NDC) |
| 5 | `NDC_CODES_ID_NDC_CODE` | VARCHAR |  | The external code for the National Drug Code (NDC). An NDC represents packages of medications. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

