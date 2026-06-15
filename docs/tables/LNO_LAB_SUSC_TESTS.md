# LNO_LAB_SUSC_TESTS

> Stores the test keys that were included when result routing to a submitter recipient. The corresponding isolate is in LNO_LAB_SUSC_ISOLATES.

**Primary key:** `RECORD_ID`, `GROUP_LINE`, `VALUE_LINE`  
**Columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the extract record. |
| 2 | `GROUP_LINE` | INTEGER | PK | The line number for the information associated with this record. |
| 3 | `VALUE_LINE` | INTEGER | PK | The line number of one of the multiple values associated with a specific group of data within this record. |
| 4 | `LAB_SUSC_TEST_KEY_IDENT` | VARCHAR |  | Stores the test keys that were included when result routing to a submitter recipient. The corresponding isolate is in LNO_LAB_SUSC_ISOLATES. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

