# ORD_LDA_LINK_AUDIT

> Audit table for links between the Order and LDAs.

**Primary key:** `ORDER_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The order ID. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: ORDER_ID |
| 2 | `LINE` | INTEGER | PK | The line in the chronicles item. This is extracted from the LINE_COUNT column. |
| 3 | `AUDIT_LDA_ID` | VARCHAR |  | Audit trail for Line/Drain/Airway (LDA) ID. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_ID |
| 4 | `AUDIT_LDA_PORT_C_NAME` | VARCHAR | org | Audit trail for Line/Drain/Airway (LDA) Port. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_PORT_C |
| 5 | `AUDIT_LDA_INSTLK_TM` | DATETIME (Local) |  | Audit trail for the line linkage instant. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_INST_LINK |
| 6 | `AUDIT_LDA_COMMENT` | VARCHAR |  | Audit trail of the comment for the line linkage. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_COMMENT |
| 7 | `AUDIT_LDA_INSTRC_TM` | DATETIME (Local) |  | Audit trail for the instant the line link was recorded. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_INST_REC |
| 8 | `AUDIT_LDA_USER_ID` | VARCHAR |  | Audit trail of the user that recorded the line linkage. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_USER_ID |
| 9 | `AUDIT_LDA_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `AUDIT_LDA_EDITED` | INTEGER |  | The line that was edited to create this entry in the audit trail. KB SQL Table: AUDIT_LDA_LINK KB SQL Column: AUDIT_LDA_EDITED |
| 11 | `AUDIT_ENC_CSN` | NUMERIC | FK→ | The audit trail of the encounter identifier that the Line/Drain/Airway (LDA) link was documented from. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `AUDIT_ENC_CSN` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

