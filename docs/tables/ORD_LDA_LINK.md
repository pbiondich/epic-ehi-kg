# ORD_LDA_LINK

> Links between Orders (ORD) and LDAs.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The order ID KB SQL Table: CURRENT_LDA_LINK KB SQL Column: ORDER_ID |
| 2 | `LINE` | INTEGER | PK | The chronicles item line. This does not actually have a KB SQL column. Extracted from LINE_COUNT |
| 3 | `LDA_ID` | VARCHAR |  | The ID of the currently linked Line/Drain/Airway (LDA) KB SQL Table: CURRENT_LDA_LINK KB SQL Column: LDA_ID |
| 4 | `LDA_PORT_C_NAME` | VARCHAR | org | Currently linked Line/Drain/Airway (LDA) port. KB SQL Table: CURRENT_LDA_LINK KB SQL Column: LDA_PORT_C |
| 5 | `LDA_INST_LINKED_TM` | DATETIME (Local) |  | The instant when the current line linkage occurred. |
| 6 | `LDA_COMMENT` | VARCHAR |  | A comment for the current Line/Drain/Airway (LDA) link. KB SQL Table: CURRENT_LDA_LINK KB SQL Column: LDA_COMMENT |
| 7 | `LDA_INST_RECORD_TM` | DATETIME (Local) |  | The instant that the current linkage was recorded. KB SQL Table: CURRENT_LDA_LINK KB SQL Column: LDA_INST_RECORDED |
| 8 | `LDA_USER_ID` | VARCHAR |  | The user that recorded the current Line/Drain/Airway (LDA) link. KB SQL Table: CURRENT_LDA_LINK KB SQL Column: LDA_USER_ID |
| 9 | `LDA_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `LDA_EDITED` | INTEGER |  | Points to a line in the audit trail if the LDA linked to the order is edited. |
| 11 | `ENC_CSN` | NUMERIC |  | The encounter identifier that the Line/Drain/Airway (LDA) link was documented from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

