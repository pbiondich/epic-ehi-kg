# RXA_RESPONSE_DUR

> The Drug Utilization Review (DUR) response section received from the payor.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `I_REASON_FOR_SVC_ID` | NUMERIC |  | NCPDP code identifying the type of utilization conflict detected or the reason for the pharmacists professional service. |
| 6 | `I_REASON_FOR_SVC_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 7 | `I_CLIN_SIG_CODE_ID` | NUMERIC |  | NCPDP code identifying the significance or severity level of a clinical event as contained in the originating database. |
| 8 | `I_CLIN_SIG_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 9 | `I_PHRM_RESP_DUR_ID` | NUMERIC |  | NCPDP code indicating the pharmacy responsible for the previous event involved in the DUR conflict. |
| 10 | `I_PHRM_RESP_DUR_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 11 | `I_QTY_PREV_FILL` | NUMERIC |  | Previously filled amount expressed in metric decimal units |
| 12 | `I_DRUG_INFO_SRC_ID` | NUMERIC |  | NCPDP code identifying the source of drug information used for DUR processing or to define the database used for identifying the product. |
| 13 | `I_DRUG_INFO_SRC_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 14 | `I_PRESC_COMP_ID` | NUMERIC |  | NCPDP code comparing the prescriber of the current prescription to the prescriber of the previously filled conflicting prescription. |
| 15 | `I_PRESC_COMP_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 16 | `I_DUR_ALERT_ADDL_TX` | VARCHAR |  | Text that provides additional detail regarding a DUR conflict. |
| 17 | `I_PRSC_PREV_FILL_DT` | DATETIME |  | The date the prescription was previously filled. |
| 18 | `I_DUR_CNFLT_ADDL_TX` | VARCHAR |  | Descriptive information that further defines the referenced DUR alert. |
| 19 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

