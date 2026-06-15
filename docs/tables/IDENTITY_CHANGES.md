# IDENTITY_CHANGES

> This table contains information regarding the identity (demographic) changes that are made to the guarantor. The identity changes include changes to a guarantor's name, sex, social security number and/or date of birth. Whenever user tries to change the identity information in Hyperspace this table will log the action.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique ID of the guarantor account record for this row. This column is frequently used to link to the ACCOUNT table. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ID_CHANGE_USER_ID` | VARCHAR |  | User that chose to change the guarantor's identity despite being warned by overlay detection. |
| 4 | `ID_CHANGE_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 5 | `ID_CHANGE_REASON_C_NAME` | VARCHAR | org | Reason why the user chose to change the guarantor's identity. |
| 6 | `ID_CHG_OLD_NAME` | VARCHAR |  | Guarantor name prior to the identity change. |
| 7 | `ID_CHG_OLD_SEX_C_NAME` | VARCHAR | org | Guarantor sex prior to the identity change. |
| 8 | `ID_CHG_OLD_DOB_DT` | DATETIME |  | Guarantor date of birth prior to the identity change. |
| 9 | `ID_CHG_NEW_NAME` | VARCHAR |  | Guarantor name after the identity change. |
| 10 | `ID_CHG_NEW_SEX_C_NAME` | VARCHAR |  | Guarantor sex after the identity change. |
| 11 | `ID_CHG_NEW_DOB_DT` | DATETIME |  | Guarantor date of birth after the identity change. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

