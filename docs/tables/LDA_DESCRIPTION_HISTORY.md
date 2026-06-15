# LDA_DESCRIPTION_HISTORY

> Holds the history of the various LDA descriptions that have been generated for this LDA overtime.

**Primary key:** `IP_LDA_ID`, `LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `IP_LDA_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the line/drain record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `DESCRIPTION_CREATED_UTC_DTTM` | DATETIME (UTC) |  | Stores the instant an LDA name was updated. To be used with LDA 106 which stores the name that was generated at the instant stored in this item. |
| 4 | `LDA_DESCRIPTION_HISTORY` | VARCHAR |  | Stores the LDA description at a specific instant. To be used with LDA 105 which stores the instant that the description was generated. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

