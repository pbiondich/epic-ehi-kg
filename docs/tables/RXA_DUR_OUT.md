# RXA_DUR_OUT

> Clarity extract of the DUR OUT group.

**Primary key:** `RECORD_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `RECORD_ID` | NUMERIC | PK shared | The unique identifier for the adjudication record. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | A unique contact date in decimal format. The integer portion of the number indicates the date of contact. The digits after the decimal distinguish different contacts on the same date and are unique for each contact on that date. For example, .00 is the first/only contact, .01 is the second contact, etc. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `CONTACT_DATE` | DATETIME |  | The date of this contact in calendar format. |
| 5 | `O_REAS_SERV_CODE_ID` | NUMERIC |  | Code identifying the type of utilization conflict detected by the prescriber or the pharmacist or the reason for the pharmacist's professional service. |
| 6 | `O_REAS_SERV_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 7 | `O_PROF_SERV_CODE_ID` | NUMERIC |  | The code that identifies the pharmacist intervention taken when a conflict code has been identified or service has been rendered. |
| 8 | `O_PROF_SERV_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 9 | `O_RES_SERV_CODE_ID` | NUMERIC |  | Action taken by a pharmacist or prescriber in response to a conflict or as the result of a pharmacist's professional service. |
| 10 | `O_RES_SERV_CODE_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 11 | `O_DUR_LEVEL_EFF_ID` | NUMERIC |  | Code indicating the level of effort as determined by the complexity of decision-making or resources utilized by a pharmacist to perform a professional service. |
| 12 | `O_DUR_LEVEL_EFF_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 13 | `O_DUR_COAGENT_Q_ID` | NUMERIC |  | The code that qualifies the value in 'DUR Co-Agent ID' (476-H6). |
| 14 | `O_DUR_COAGENT_Q_ID_EXT_CODE_LST_NAME` | VARCHAR |  | The name of the list value. |
| 15 | `O_DUR_COAGENT_ID` | VARCHAR |  | Identifies the co-existing agent contributing to the DUR event (drug or disease conflicting with the prescribed drug or prompting pharmacist professional service). |
| 16 | `CM_CT_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this contact. This is only populated if you use IntraConnect. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

