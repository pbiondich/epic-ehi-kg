# SPEC_HOLD_INFO

> The SPEC_HOLD_INFO table contains information pertaining to holds placed on a specimen.

**Primary key:** `SPECIMEN_ID`, `LINE`  
**Columns:** 11  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `SPECIMEN_ID` | VARCHAR | PK shared | The unique identifier for the specimen record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `HOLD_C_NAME` | VARCHAR | org | The hold category number for the test specified in column HOLD_TEST_ID. |
| 4 | `HOLD_TEST_ID_TEST_NAME` | VARCHAR |  | The name of the test record. |
| 5 | `HOLD_BEGIN_INS_DTTM` | DATETIME (Local) |  | The instant when the hold took effect. |
| 6 | `HOLD_BEGIN_CMT_ID` | VARCHAR |  | The unique identifier of the note that was made (if any) when the hold was placed. |
| 7 | `HOLD_CLEAR_INS_DTTM` | DATETIME (Local) |  | The instant when the hold was cleared. A blank value here means the hold is still active. |
| 8 | `HOLD_CLEAR_USER_ID` | VARCHAR |  | The unique ID of the user who cleared the hold. If this is empty and column HOLD_CLEAR_INS_DTTM has a value, it means the system automatically cleared the hold. |
| 9 | `HOLD_CLEAR_USER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |
| 10 | `HOLD_CLEAR_RSN_C_NAME` | VARCHAR | org | The category number for the reason the hold was cleared. This should only have a value if column HOLD_CLEAR_INS_DTTM also has a value. |
| 11 | `HOLD_CLEAR_CMT_ID` | VARCHAR |  | The unique identifier of the note that was made (if any) when the hold was cleared. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

