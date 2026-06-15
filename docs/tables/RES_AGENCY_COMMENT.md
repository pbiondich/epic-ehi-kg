# RES_AGENCY_COMMENT

> This table contains the extract for the Resulting Agency's Comment (I ORD 71) item, which contains any additional comments made by the lab tech on a lab result. Comments might include further description of the lab results, or any other information such as malfunctioning lab equipment.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 3

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `RES_AGENCY_COMMENT` | VARCHAR |  | This free text field contains information entered by a lab tech on how a lab result was processed. It may include notes on any equipment or procedures that are not clinically relevant. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

