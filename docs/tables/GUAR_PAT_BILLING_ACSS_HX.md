# GUAR_PAT_BILLING_ACSS_HX

> This table keeps an audit trail of changes made to the list of MyChart accounts that have billing access to the guarantor account. Every time an account is added or revoked, a row will be added to this table.

**Primary key:** `ACCT_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ACCT_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the guarantor record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `BILL_ACSS_MYPT_ID` | VARCHAR |  | Item to store history for MyChart accounts that have billing access to the guarantor account |
| 4 | `BILL_ACSS_ACTION_C_NAME` | VARCHAR |  | The action associated with changes to MyChart accounts that have billing access to the guarantor account |
| 5 | `BILL_ACSS_USER_ID` | VARCHAR |  | EMP ID of user who added or revoked a MyChart account that has billing access to the guarantor account |
| 6 | `BILL_ACSS_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 7 | `BILL_ACSS_INST_UTC_DTTM` | DATETIME (UTC) |  | The action time instant associated with changes to MyChart accounts that have billing access to the guarantor account |
| 8 | `BILL_ACSS_REV_RSN_C_NAME` | VARCHAR | org | Item to store the reason for revocation whenever an end user manually revokes a MyChart account that has billing access to the guarantor account |
| 9 | `BILL_ACSS_REV_CMT` | VARCHAR |  | Item to store the comment entered whenever an end user manually revokes a MyChart account that has billing access to the guarantor account |
| 10 | `BILL_ACCS_INV_CODE` | VARCHAR |  | History item tracking the invite code when tracking an invite from MyChart |
| 11 | `BILL_ACCS_INV_STS_C_NAME` | VARCHAR |  | History item to track the invite status when a tracking an invite from MyChart or Hyperspace |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

