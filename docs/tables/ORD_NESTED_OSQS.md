# ORD_NESTED_OSQS

> Contains nested panel information where each line represents one level of nesting.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `NESTED_PANEL_ID_ORDERSET_NAME` | VARCHAR |  | The SmartGroup record name. This is different from the display name, which is stored in CL_OSQ_OT.DISPLAY_NAME. |
| 4 | `NESTED_PANEL_CONTACT_DATE_REAL` | NUMERIC |  | Stores a list of grouped orders (OSQ) contact dates (DATs) corresponding to the nested (group within group) OSQ IDs. |
| 5 | `NESTED_PANEL_UNIQ_KEY` | VARCHAR |  | Stores a list of "panel info"s corresponding to the OSQ IDs above, which uniquely identify identical nested OSQs placed in the same ordering session. |
| 6 | `NESTED_GROUP_ID` | NUMERIC |  | For orders from clinical pathways (a method of placing many orders that are meant to take place over a period of time all at once), stores a list of TRG IDs representing the groups of orders which contain other groups of orders from which the order originated. |
| 7 | `NESTED_GROUP_CSN` | NUMERIC |  | Stores a list of Patient Order Groups and Treatment Days (TRG) Contact Serial Numbers (CSN) associated with the above TRG IDs. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

