# MLS_OVERRIDE_TIME_HX

> Contains general information on override for multiline sig

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `MULTILINE_KEY` | VARCHAR |  | Holds key to guide finding override information specific to a multiline sig period & part |
| 4 | `MLS_OVRIDE_REL_LINE` | VARCHAR |  | Holds indices that will serve as guide to find override information associated with specific multiline period & part. Each index corresponds to a line in SI ORD 34635. |
| 5 | `MLS_EFQ_OVRIDE_DESC` | VARCHAR |  | Holds override description in human-readable format. Equivalent to ORD 34642 for a non-MLS order. |
| 6 | `MLS_OVRIDE_DAY_TYPE` | INTEGER |  | Specifies what the numeric values in the frequency override days columns represent. If it is 1 then the listed days are relative days. If it is 2 then the listed days are weekdays. Any other value has no meaning. |
| 7 | `MLS_OVRIDE_CYCLE_LEN` | INTEGER |  | If there is a frequency override specified, this item will contain the length of a relative specified type cycle. For all other specified types this value will be ignored (and should be empty). |
| 8 | `MLS_OVRIDE_UPD_TIME` | VARCHAR |  | Holds the formatted override string for the adjusted frequency. Equivalent to ORD 34670 for non-multiline sig order. |
| 9 | `MLS_OVRIDE_SCHD_INST_DTTM` | DATETIME (Local) |  | Override schedule time for "adjust times" of non-specified frequency. |
| 10 | `MLS_OVRIDE_SRC_DEPT_ID_EXTERNAL_NAME` | VARCHAR |  | The external name of the department record. This is often used in patient correspondence such as reminder letters. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

